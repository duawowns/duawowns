import os, re, json, pathlib

GITHUB_ENV = os.environ.get('GITHUB_ENV', '')
title = os.environ.get('ISSUE_TITLE', '')
body = os.environ.get('ISSUE_BODY', '') or ''
comment_path = pathlib.Path('.github/scripts/comment.md')

def write_comment(txt):
    comment_path.write_text(txt, encoding='utf-8')

def skip(msg):
    write_comment(f'🤖 {msg}')
    print(msg)
    raise SystemExit(0)

if not re.match(r'^\[(boggle|mine)\]', title.strip()):
    skip('이 이슈는 점수 등록 이슈가 아니에요. 자동으로 닫았습니다. 점수는 게임 안의 🏆순위 버튼으로 등록해주세요.')

m = re.search(r'```json\s*(\{.*?\})\s*```', body, re.S)
if not m:
    skip('점수 데이터(JSON 블록)를 찾지 못했어요. 게임 안의 🏆순위 버튼으로 등록해주세요.')

try:
    data = json.loads(m.group(1))
except Exception as e:
    skip(f'JSON 파싱 실패: {e}')

game = data.get('game', '')
name = str(data.get('name', '익명'))[:12].strip() or '익명'
name = re.sub(r'[\n\r`<>]', '', name)[:12] or '익명'

if game == 'boggle':
    val = data.get('score', 0)
    if not isinstance(val, (int, float)) or val < 0:
        skip('score 값이 올바르지 않아요.')
    entry = {'name': name, 'score': int(val), 'combo': int(data.get('combo', 0) or 0)}
    sort_key = lambda x: (-x.get('score', 0), -x.get('combo', 0), x.get('name', ''))
    match = lambda e: e.get('score') == entry['score'] and e.get('combo', 0) == entry['combo'] and e['name'] == entry['name']
    summary = f'**{name}** · **{int(val)}점**'
elif game == 'mine':
    val = data.get('time', 0)
    if not isinstance(val, (int, float)) or val <= 0:
        skip('time 값이 올바르지 않아요.')
    diff = str(data.get('diff', ''))[:6]
    entry = {'name': name, 'time': int(val), 'diff': diff}
    sort_key = lambda x: (x.get('time', 99999), x.get('name', ''))
    match = lambda e: e.get('time') == entry['time'] and e.get('diff') == diff and e['name'] == entry['name']
    summary = f'**{name}** · **{int(val)}초** ({diff})'
else:
    skip('알 수 없는 게임이에요.')

folder = {'boggle': 'boggle-boggle', 'mine': 'mine-friend'}[game]
fname = f'public/{folder}/leaderboard-{game}.json'
p = pathlib.Path(fname)
try:
    lst = json.loads(p.read_text(encoding='utf-8')) if p.exists() else []
except Exception:
    lst = []

lst.append(entry)
lst.sort(key=sort_key)
rank = 1
for i, e in enumerate(lst):
    if match(e):
        rank = i + 1
        break
lst = lst[:50]
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(lst, ensure_ascii=False, indent=2), encoding='utf-8')

total = len(lst)
medals = {1: '🥇 전 세계 1위!', 2: '🥈 전 세계 2위. 코앞이었는데', 3: '🥉 전 세계 3위. 시상대 등극'}
line = medals.get(rank, f'전 세계 {rank}위 (전체 {total}명)')
link = f"https://duawowns.github.io/duawowns/{'boggle-boggle' if game == 'boggle' else 'mine-friend'}/"
write_comment(f'✅ 순위 반영 완료!\n\n{summary} → {line}\n\n잠시 후 사이트에 반영돼요: {link}\n\n_(이 이슈는 봇이 자동으로 닫습니다)_\n')
if GITHUB_ENV:
    with open(GITHUB_ENV, 'a', encoding='utf-8') as f:
        f.write(f'lb_rank={rank}\nlb_total={total}\n')
print(f'ok rank={rank} total={total}')

# Design QA — Variant welcome loader

Date: 2026-08-14
Reference: https://variant.com/shared/0ccef068-d570-4de9-9cf9-470fd04a937f?t=1786694015623

## Comparison target

- Source visual truth: `.design-qa-loader/source-loader-desktop.png`
- Implementation screenshots: `.design-qa-loader/implementation-loader-desktop.png`, `.design-qa-loader/implementation-loader-mobile.png`
- Combined comparison: `.design-qa-loader/loader-comparison-desktop.jpg`
- Desktop viewport and pixels: 1440 × 900 CSS px, 1440 × 900 source and implementation pixels, density 1.
- Mobile implementation viewport and pixels: 390 × 844 CSS px and 390 × 844 pixels, density 1.
- State: initial full-screen loading overlay while progress is moving.

## Full-view comparison evidence

- Layout and spacing: the centered vertical stack, 40px gaps, 200px × 1px progress track, and viewport-filling overlay match the source. The implementation intentionally replaces the source copy with the requested welcome message.
- Fonts and typography: both use the locally bundled Satoshi family. The loader label matches the source at 12px, 400 weight, 1.4 line height, uppercase, and 0.2em tracking. The percentage matches at 14px, 500 weight, and tabular numerals.
- Colors and tokens: the implementation matches the source `#0a0a0a` background, `#888` label, `#222` track, and white progress/percentage.
- Image quality and assets: the loader contains no image, logo, icon, or decorative asset. No substitute or hotlinked asset is used.
- Copy and content: `SYSTEM INITIALIZING` was intentionally changed to `WELCOME TO JAEJUN'S PORTFOLIO`; progress remains numeric from 0% to 100%.

The combined desktop image was inspected as one side-by-side comparison input. A separate focused crop was unnecessary because the only visible component is the centered loader and every typographic and spacing detail is legible in the full-view comparison.

## Interaction and responsive verification

- Progress animates to 100%, then the overlay fades and becomes non-interactive.
- `aria-hidden` is set after completion, the document scroll lock is released, and the portfolio hero remains available.
- Reduced-motion mode shortens the artificial progress animation and removes the long transition through the existing motion override.
- At 390 × 844, the message, bar, and percentage remain centered with no horizontal overflow.
- The locally bundled Satoshi font loads successfully.
- Browser console errors: none.

## Findings

- No actionable P0, P1, or P2 mismatch remains.
- Expected difference: the requested welcome copy is wider than the source phrase.
- Expected difference: capture percentages differ because both loaders were captured while actively progressing.

## Comparison history

- First comparison: no actionable P0/P1/P2 issues found; no visual correction loop was required.

## Implementation checklist

- [x] Welcome copy applied.
- [x] Reference spacing, color, typography, and transition reproduced.
- [x] Desktop and mobile states verified.
- [x] Completion, accessibility state, font loading, overflow, and console checked.
- [x] Production build and dependency audit passed.

## Follow-up polish

- None required for this scope.

## Favicon update — Variant Archive 01

- Source visual truth: Variant frame `Favicon Design — Archive 01` and `.design-qa-loader/source-favicon.png`.
- Implementation screenshot: `.design-qa-loader/implementation-favicon.png`.
- Combined comparison: `.design-qa-loader/favicon-comparison.png`.
- Viewport and pixels: 512 × 512 CSS px, 512 × 512 source and implementation pixels, density 1.
- State: standalone favicon SVG on its native 512 × 512 artboard.
- Full-view and focused evidence: the favicon fills the entire comparison frame, so the combined full view also serves as the focused icon comparison.
- Typography and copy: not applicable; the mark contains no text.
- Spacing and layout: the outer `A` silhouette, apex, leg widths, and central 162 × 52 cutout match exactly.
- Colors and tokens: both use `#0A0A0A` and white with no gradient or transparency drift.
- Image quality and assets: the exact Variant SVG geometry was copied; no raster substitute, custom redraw, or hotlink was used.
- Interaction and responsiveness: the page head resolves the versioned SVG URL as `image/svg+xml`; a fresh browser tab reports no console errors.
- Findings: no actionable P0, P1, or P2 mismatch.
- Comparison history: the first normalized 512 × 512 side-by-side comparison passed; no visual correction loop was needed.

final result: passed

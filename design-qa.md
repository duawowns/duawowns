# Design QA - Variant 59395f52 redesign

Status: PASSED
Date: 2026-08-13
Reference: https://variant.com/shared/59395f52-be5c-4617-ae38-9f44e5fe7ecf?t=1786600805331

## Scope

- Rebuilt the Astro portfolio from the supplied Variant reference.
- Replaced placeholder portfolio copy with public-facing content derived from `이력서+경력기술서.pdf`.
- Excluded the phone number, portrait, and a downloadable copy of the source PDF from the public build.
- Verified at 1440 x 1000 and 390 x 844 in the in-app browser.

## Fidelity comparison

- Layout: matched the fixed centered pill navigation, 90vh hero, 12-column 8/4 and 4/8 project grid, ledger rows, two-column credentials grid, rounded contact surface, and fixed circular scroll progress.
- Typography: bundled the reference Satoshi font locally at weights 400, 500, 700, and 900. The display scale, tight line height, negative letter spacing, muted body copy, and uppercase micro-labels match the source hierarchy.
- Color and surfaces: matched `#0a0a0a` background, `#141414` surfaces, white foreground, gray secondary text, subtle `#242424` borders, 28px card radius, and translucent blurred navigation.
- Imagery: bundled four source-family Unsplash assets locally and verified their crop and sharpness inside the project card aspect ratios. No remote image or font hotlinks remain in the production page.
- Responsive behavior: converted the project grid to one column below 1024px, reduced mobile navigation and section spacing, stacked ledger data, and kept the 390px layout free of horizontal overflow.
- Content: project, career, education, certification, skill, email, and location copy is grounded in the supplied resume while omitting sensitive personal data from the public page.

## Interaction and accessibility

- Work, Career, Credentials, and Contact navigation links scroll to real sections and update the active state.
- Scroll percentage updates from 0% to 100% and remains legible on desktop and mobile.
- Primary email and GitHub links have real destinations.
- Arrow controls use Lucide icons rather than text-symbol or custom-drawn substitutes.
- Semantic headings, section labels, decorative image alt handling, skip link, visible focus states, reduced-motion handling, and mobile tap targets were checked.
- Browser verification confirmed the bundled Satoshi font loaded, the Career active state updated after navigation, two Lucide SVG icons rendered, and horizontal overflow was false at 390px.

## Verification

- `npm run build`: passed.
- `npm audit --omit=dev`: 0 vulnerabilities.
- `git diff --check`: passed.
- Desktop and mobile reference/implementation comparison sheets were inspected from `.design-qa-v3/`.

## Notes

- Astro reports informational build-time warnings for absolute `/duawowns/fonts/...` public URLs. The files are copied into `dist/fonts/`, and browser verification confirmed the font loads at runtime under the GitHub Pages base path.

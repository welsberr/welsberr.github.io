# MSU web guidance adaptation

Checked 25 September 2026 for this personal GitHub Pages presentation to the BEACON large group.

## Adopted

- **Colors:** official Spartan green `#18453B` and white `#FFFFFF`; the official lime accent `#7BBD00` is used on dark green. Neutral shades support borders and secondary text. Green/white remain dominant. Source: [MSU Color Palette](https://brand.msu.edu/visual/color-palette).
- **Typography:** Metropolis Regular and Bold for headings, diagrams, and navigation; Arial/Helvetica for body text and fallback. The two MSU-supplied font files are locally served as WOFF2, with font swapping rather than invisible text while loading. Headings retain sentence case to keep long scientific discussion titles readable within the existing columns. Source: [MSU Typography](https://brand.msu.edu/visual/typography).
- **Accessible presentation:** preserve semantic headings and lists, descriptive links, selectable HTML diagram text, labeled controls, normal document scrolling, and the reduced-motion preference. Strengthen focus visibility across both backgrounds and enlarge the fixed controls to at least 44 pixels high. The notes shortcut uses Alt+N instead of an unmodified letter. Sources: [MSU Basic Accessibility Checklist](https://webaccess.msu.edu/tutorials/basics/checklist) and [MSU Technical Guidelines](https://webaccess.msu.edu/policy/technical-guidelines).

MSU's current technical guideline is WCAG 2.2 AA, effective 1 January 2026. These changes and the recorded browser checks address relevant presentation behavior; they are not a complete conformance audit.

## Scope and preserved behavior

The [MSU institutional web standards](https://dxstudio.msu.edu/website-technology/web-standards/brand-design) prescribe a university masthead, search, and legal footer for institutional websites. This is Wesley R. Elsberry's personal presentation on GitHub Pages. Its author identity and BEACON audience label remain; no university ownership footer or official institutional masthead is asserted.

The sticky illustration columns, mobile reading flow, source anchors, keyboard section navigation, notes, interactive release gate, printing, and no-JavaScript reading remain available. The social preview illustration is retained. Runtime requests remain on the same origin; no remote font stylesheet or university search/analytics script is introduced.

## Verification

Local Chromium checks passed after the styling change: 20 sections and 20 source records; sticky-diagram changes and section navigation; all 16 policy-demo combinations; notes and printing; responsive widths from 320 to 1440 pixels; no JavaScript errors. Metropolis loads locally. The contrast check found no failing rendered text pairs and a minimum ratio of 4.67:1. The skip link moves focus to main content, Alt+N toggles notes while plain N is inactive, reduced motion disables panel animation, and fixed buttons meet a 44-by-44-pixel target minimum. Representative desktop and mobile screenshots were inspected.

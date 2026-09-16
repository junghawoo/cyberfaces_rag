---
title: "Unit 352"
unit_id: 352
---

# Unit 352

This module, "Accessibility in Map Design" (teaching: 50, exercises: 40), is delivered as two extracted resources with identical lesson content: a Jupyter notebook `accessibility.ipynb` (Markdown lesson converted to notebook-friendly format, with notes that code cells can be added for QGIS examples, color palette demos, or accessibility checks) and a Markdown file `accessibility.md`.

Guiding questions cover why accessibility matters in cartography, how color vision deficiency (CVD) affects map reading, designing maps readable for colorblind users, the roles of hue, saturation, and value, and which color palettes work best in QGIS. Learning objectives: understand why accessibility matters in map design, recognize major types of CVD, apply color-safe cartographic principles, select accessible color palettes in QGIS, and test maps for readability across audiences.

Sections include: Why Accessibility Matters in Maps (maps as communication tools; accessible maps reach wider audiences, improve readability, reduce bias, support inclusive science communication); Understanding Color Vision Deficiency (~8% of men, ~0.5% of women affected); Common Types of Colorblindness — Deuteranopia (green-blind, most common, confuses green/red and green/brown), Protanopia (red-blind, red appears darker), Tritanopia (blue-blind, rare, confuses blue/green and yellow/violet), and Achromatopsia (monochromacy, near-grayscale perception). A challenge asks why a red-green choropleth map fails many users.

Common mapping problems: red vs green comparisons, similar lightness values, too many low-contrast hues, relying only on color to encode meaning. The solution section covers hue (avoid red-green and blue-purple combinations), saturation (moderate, avoid oversaturated colors), and value/lightness (most important — vary lightness more than hue). Designing accessible maps means combining color with patterns, labels, symbols, and line styles (e.g., blue circles vs orange squares instead of red vs green).

Recommended colorblind-safe palettes: sequential — Blues, Viridis, Cividis, YlGnBu; diverging — Blue-Orange, Purple-Green (carefully tested); categorical — ColorBrewer Set2, Dark2, Tableau palettes. Rainbow palettes should be avoided. Best QGIS ramps: Viridis, Cividis, Plasma, Inferno, Blues, ColorBrewer Safe; avoid Rainbow, red-green diverging, and neon saturated ramps. Applying palettes in QGIS: right-click layer, Properties → Symbology, choose color ramp (Viridis/Cividis/Blues), preview contrast between adjacent classes.

Testing tools: QGIS Preview Modes, Color Oracle, and the Coblis Color Blindness Simulator. Accessibility beyond colorblindness includes readable font sizes, clear legends, sufficient contrast, and screen-reader compatible web maps. A good-vs-bad example contrasts a red-green choropleth with equal brightness against a blue-orange palette with strong value contrast. A pre-publication accessibility checklist and final takeaways (accessible maps are clearer, more inclusive, more professional) close the lesson, followed by discussion prompts on hard-to-read maps and accessibility in scientific communication.

## Summarized attachments
- **accessibility.ipynb** (accessibility.ipynb, ipynb): Jupyter notebook lesson (50 min teaching, 40 min exercises) on accessibility in map design covering why accessibility matters in cartography, types of color vision deficiency (deuteranopia/green-blind, protanopia/red-blind, tritanopia/blue-blind, achromatopsia), color design principles (hue, saturation, value/lightness), avoiding red-green comparisons, recommended colorblind-safe palettes (Viridis, Cividis, Blues, ColorBrewer, Tableau palettes), QGIS color ramp selection and application in Symbology properties, accessibility testing tools (QGIS Preview Modes, Color Oracle, Coblis Color Blindness Simulator), and checklist for pre-publication accessibility assessment.

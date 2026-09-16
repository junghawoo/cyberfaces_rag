---
title: "Unit 352"
unit_id: 352
---

# Unit 352

## Extracted resources (local files)

### accessibility.ipynb
*Source file:* `accessibility.ipynb`  ·  *type:* ipynb

# Accessibility in Map Design

Converted from the attached Markdown lesson into a notebook-friendly format.


---
title: "Accessibility in Map Design"
teaching: 50
exercises: 40
---

:::::::::::::::::::::::::::::::::::::: questions

- Why is accessibility important in cartography?
- How do different types of color vision deficiency affect map reading?
- How can we design maps that are readable for colorblind users?
- What role do hue, saturation, and value play in accessible design?
- Which color palettes work best in QGIS for accessible maps?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand why accessibility matters in map design
- Recognize major types of color vision deficiency (CVD)
- Apply color-safe cartographic principles
- Select accessible color palettes in QGIS
- Test maps for readability across audiences

::::::::::::::::::::::::::::::::::::::::::::::::

## Why Accessibility Matters in Maps

Maps are communication tools.  
If part of your audience cannot interpret your colors, your map fails to communicate effectively.

Accessible maps:
- Reach wider audiences
- Improve readability for everyone
- Reduce misunderstanding and bias
- Support inclusive science communication

::::::::::::::::::::::::::::::::::::: callout

### Key Idea
Accessibility is not optional — it is part of good cartographic design.

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Understanding Color Vision Deficiency (Colorblindness)

Color vision deficiency affects how some people distinguish colors.

Approximately:
- ~8% of men
- ~0.5% of women

experience some form of color vision deficiency.

---

## Common Types of Colorblindness

### 1. Deuteranopia (Green-Blind)

Most common form.

People may confuse:
- Green ↔ Red
- Green ↔ Brown

---

### 2. Protanopia (Red-Blind)

Reduced sensitivity to red light.

People may confuse:
- Red ↔ Green
- Red appears darker

---

### 3. Tritanopia (Blue-Blind)

Rare.

People may confuse:
- Blue ↔ Green
- Yellow ↔ Violet

---

### 4. Achromatopsia (Monochromacy)

Very rare.

Little or no color perception.

Maps may appear nearly grayscale.

::::::::::::::::::::::::::::::::::::: challenge

Why might a red-green choropleth map fail for many users?

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Common Mapping Problems for Colorblind Users

Poor design choices include:
- Red vs green comparisons
- Similar lightness values
- Too many hues with low contrast
- Relying only on color to encode meaning

Example bad pairing:
❌ Red and green categories on same map

---

## The Solution: Use Hue, Saturation, and Value Wisely

### Hue
The color family (red, blue, green)

Avoid:
- Red-green combinations
- Blue-purple confusion in tritanopia

---

### Saturation
Intensity or purity of color

Use:
- Moderate saturation
- Avoid oversaturated bright colors

---

### Value (Lightness)

Most important for accessibility.

If colors differ in brightness, they remain distinguishable even if hue is unclear.

::::::::::::::::::::::::::::::::::::: callout

### Best Practice
When in doubt, vary lightness more than hue.

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Designing Accessible Maps

### Use More Than Color

Combine color with:
- Patterns
- Labels
- Symbols
- Line styles

Example:
Instead of only red vs green, use:
- Blue circles
- Orange squares

---

## Recommended Colorblind-Safe Palettes

These palettes work well across most users.

### Sequential Data:
Best choices:
- Blues
- Viridis
- Cividis
- YlGnBu

### Diverging Data:
Best choices:
- Blue–Orange
- Purple–Green (carefully tested)

### Categorical Data:
Best choices:
- ColorBrewer Set2
- Dark2
- Tableau palettes

::::::::::::::::::::::::::::::::::::: callout

### Avoid Rainbow Palettes
Rainbow color ramps create misleading emphasis and poor accessibility.

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Best QGIS Palettes for Accessibility

In QGIS, use built-in ramps such as:

### Excellent Choices:
- Viridis
- Cividis
- Plasma
- Inferno
- Blues
- ColorBrewer Safe

### Avoid:
- Rainbow
- Red-Green diverging ramps
- Neon saturated ramps

---

## How to Apply Accessible Palettes in QGIS

### Step 1: Open Symbology

Right-click layer → **Properties → Symbology**

---

### Step 2: Choose Color Ramp

Select:
- Viridis
- Cividis
- Blues

---

### Step 3: Preview Contrast

Check:
- Are adjacent classes clearly distinguishable?
- Do values differ in brightness?

---

## Testing Your Map for Accessibility

Always test your design.

### Tools:
- QGIS Preview Modes
- Color Oracle
- Coblis Color Blindness Simulator

### Ask:
Can someone distinguish categories without relying only on hue?

---

## Accessibility Beyond Colorblindness

Remember:
Accessibility also includes:
- Readable font sizes
- Clear legends
- Sufficient contrast
- Screen-reader compatible web maps

---

## Example: Good vs Bad Design

### Bad:
❌ Red-green choropleth with equal brightness

### Good:
✅ Blue-orange palette with strong value contrast

---

## Accessibility Checklist for Maps

Before publishing:

- [ ] Avoid red-green contrasts
- [ ] Use colorblind-safe palettes
- [ ] Ensure brightness contrast exists
- [ ] Add labels or symbols beyond color
- [ ] Test using simulation tools
- [ ] Keep legends simple and readable

---

## Final Takeaways

Accessible maps are:
- Clearer
- More inclusive
- More professional

Good cartography means designing for all users.

::::::::::::::::::::::::::::::::::::: discussion

- Have you seen maps that were difficult to read because of color?
- How can accessibility improve scientific communication?

::::::::::::::::::::::::::::::::::::::::::::::::

## Notebook notes

- This notebook preserves the lesson content in Markdown cells.
- You can add code cells below for QGIS examples, color palette demos, or accessibility checks.

### accessibility.md
*Source file:* `accessibility.md`  ·  *type:* md

---
title: "Accessibility in Map Design"
teaching: 50
exercises: 40
---

:::::::::::::::::::::::::::::::::::::: questions

- Why is accessibility important in cartography?
- How do different types of color vision deficiency affect map reading?
- How can we design maps that are readable for colorblind users?
- What role do hue, saturation, and value play in accessible design?
- Which color palettes work best in QGIS for accessible maps?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand why accessibility matters in map design
- Recognize major types of color vision deficiency (CVD)
- Apply color-safe cartographic principles
- Select accessible color palettes in QGIS
- Test maps for readability across audiences

::::::::::::::::::::::::::::::::::::::::::::::::

## Why Accessibility Matters in Maps

Maps are communication tools.  
If part of your audience cannot interpret your colors, your map fails to communicate effectively.

Accessible maps:
- Reach wider audiences
- Improve readability for everyone
- Reduce misunderstanding and bias
- Support inclusive science communication

::::::::::::::::::::::::::::::::::::: callout

### Key Idea
Accessibility is not optional — it is part of good cartographic design.

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Understanding Color Vision Deficiency (Colorblindness)

Color vision deficiency affects how some people distinguish colors.

Approximately:
- ~8% of men
- ~0.5% of women

experience some form of color vision deficiency.

---

## Common Types of Colorblindness

### 1. Deuteranopia (Green-Blind)

Most common form.

People may confuse:
- Green ↔ Red
- Green ↔ Brown

---

### 2. Protanopia (Red-Blind)

Reduced sensitivity to red light.

People may confuse:
- Red ↔ Green
- Red appears darker

---

### 3. Tritanopia (Blue-Blind)

Rare.

People may confuse:
- Blue ↔ Green
- Yellow ↔ Violet

---

### 4. Achromatopsia (Monochromacy)

Very rare.

Little or no color perception.

Maps may appear nearly grayscale.

::::::::::::::::::::::::::::::::::::: challenge

Why might a red-green choropleth map fail for many users?

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Common Mapping Problems for Colorblind Users

Poor design choices include:
- Red vs green comparisons
- Similar lightness values
- Too many hues with low contrast
- Relying only on color to encode meaning

Example bad pairing:
❌ Red and green categories on same map

---

## The Solution: Use Hue, Saturation, and Value Wisely

### Hue
The color family (red, blue, green)

Avoid:
- Red-green combinations
- Blue-purple confusion in tritanopia

---

### Saturation
Intensity or purity of color

Use:
- Moderate saturation
- Avoid oversaturated bright colors

---

### Value (Lightness)

Most important for accessibility.

If colors differ in brightness, they remain distinguishable even if hue is unclear.

::::::::::::::::::::::::::::::::::::: callout

### Best Practice
When in doubt, vary lightness more than hue.

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Designing Accessible Maps

### Use More Than Color

Combine color with:
- Patterns
- Labels
- Symbols
- Line styles

Example:
Instead of only red vs green, use:
- Blue circles
- Orange squares

---

## Recommended Colorblind-Safe Palettes

These palettes work well across most users.

### Sequential Data:
Best choices:
- Blues
- Viridis
- Cividis
- YlGnBu

### Diverging Data:
Best choices:
- Blue–Orange
- Purple–Green (carefully tested)

### Categorical Data:
Best choices:
- ColorBrewer Set2
- Dark2
- Tableau palettes

::::::::::::::::::::::::::::::::::::: callout

### Avoid Rainbow Palettes
Rainbow color ramps create misleading emphasis and poor accessibility.

::::::::::::::::::::::::::::::::::::::::::::::::

---

## Best QGIS Palettes for Accessibility

In QGIS, use built-in ramps such as:

### Excellent Choices:
- Viridis
- Cividis
- Plasma
- Inferno
- Blues
- ColorBrewer Safe

### Avoid:
- Rainbow
- Red-Green diverging ramps
- Neon saturated ramps

---

## How to Apply Accessible Palettes in QGIS

### Step 1: Open Symbology

Right-click layer → **Properties → Symbology**

---

### Step 2: Choose Color Ramp

Select:
- Viridis
- Cividis
- Blues

---

### Step 3: Preview Contrast

Check:
- Are adjacent classes clearly distinguishable?
- Do values differ in brightness?

---

## Testing Your Map for Accessibility

Always test your design.

### Tools:
- QGIS Preview Modes
- Color Oracle
- Coblis Color Blindness Simulator

### Ask:
Can someone distinguish categories without relying only on hue?

---

## Accessibility Beyond Colorblindness

Remember:
Accessibility also includes:
- Readable font sizes
- Clear legends
- Sufficient contrast
- Screen-reader compatible web maps

---

## Example: Good vs Bad Design

### Bad:
❌ Red-green choropleth with equal brightness

### Good:
✅ Blue-orange palette with strong value contrast

---

## Accessibility Checklist for Maps

Before publishing:

- [ ] Avoid red-green contrasts
- [ ] Use colorblind-safe palettes
- [ ] Ensure brightness contrast exists
- [ ] Add labels or symbols beyond color
- [ ] Test using simulation tools
- [ ] Keep legends simple and readable

---

## Final Takeaways

Accessible maps are:
- Clearer
- More inclusive
- More professional

Good cartography means designing for all users.

::::::::::::::::::::::::::::::::::::: discussion

- Have you seen maps that were difficult to read because of color?
- How can accessibility improve scientific communication?

::::::::::::::::::::::::::::::::::::::::::::::::

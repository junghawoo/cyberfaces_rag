---
title: "Unit 359"
unit_id: 359
---

# Unit 359

QField Training: Mapping Grocery Stores to Identify Potential Food Deserts. Teaching: 35 minutes, Exercises: 0.

Learning objectives: See end-to-end QField/QGIS workflow using Lafayette grocery stores; understand point placement, attribute choices, GPS accuracy rules; learn what 'good' field data looks like before collecting own data.

Scenario: Lafayette-West Lafayette, Indiana community research team; goal: understand grocery access limitations; map potential food deserts using demographics and network/travel-time analysis; create clean, consistent dataset of grocery store locations and access attributes.

Data collection approach (QField in field, QGIS on computer): One point per store at main public entrance; standardized attributes; storefront photo; note documenting unusual observations; ready for food-access/food desert analysis.

Project setup (instructor preparation): Offline basemap, study area boundary (Lafayette-West Lafayette), editable layer (Grocery Stores), prebuilt data-entry form with dropdowns (domains) for consistency.

Data schema for Grocery Stores layer: store_name (text, deduplication/verification), store_type (dropdown: supermarket/convenience), address (text, location verification), city (dropdown, filtering/reporting), zip (text, neighborhood summaries), snap_accepted (Yes/No/Unknown, benefits access), wic_accepted (Yes/No/Unknown, additional access signal), produce_available (Yes/No/Unknown, healthy food proxy), hours_observed (text, access timing), notes (text, context preservation), photo_1 (attachment, QA evidence).

GPS rules: Preferred <10 meters accuracy; record anyway if accuracy worse, document in notes. Accuracy critical for food access (30-50m shift affects buffer/service area calculations, especially near boundaries/road networks).

Data collection examples: Supermarket (main entrance, visible produce, SNAP/WIC signage, storefront photo); Small Market/Convenience (may lack produce, assume nothing about benefits programs, use "Unknown" appropriately).

Edge cases: Duplicate risk (edit existing if same store name nearby), Poor GPS (record with note like "GPS ~22m; approximated at main entrance"), Closed/renovation (record location with status note, leave uncertain fields unknown).

QA process (QGIS): Completeness (required fields filled), Spatial sanity (points in study area, no impossible locations), Duplicates (same name, close geometry), Photo verification (accessible, match records).

Good output characteristics: One record per store (no duplicates), Consistent categories (dropdown-controlled), Minimal guessing (appropriate "Unknown" use), Supporting photos, Exception notes (without new categories).

Key points: Clear scenario and consistent schema make field data analyzable; demonstrations should explain why each step exists; QA is part of collection, not afterthought.

## Summarized attachments
- **QField Training: Mapping Grocery Stores to Identify Potential Food Deserts** (qfield.md, md): Markdown lesson file (Teaching: 35 min, Exercises: 0) demonstrating end-to-end QField/QGIS workflow for mapping grocery stores in Lafayette-West Lafayette, Indiana. Covers point placement at main entrances, standardized data schema with 10 fields (store_name, store_type, address, city, zip, snap_accepted, wic_accepted, produce_available, hours_observed, notes, photo_1), GPS accuracy rules (<10m preferred), data collection examples, edge cases (duplicates, poor GPS, closed stores), QGIS QA process (completeness, spatial sanity, duplicates, photos), and best practices for maintaining consistent, analyzable field datasets for food desert analysis.

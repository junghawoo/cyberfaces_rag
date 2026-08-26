---
title: "Unit 360"
unit_id: 360
---

# Unit 360

QGIS network analysis lesson: calculating grocery store accessibility using road network shortest paths and service areas, building on QField field data collection.

**Source:** qfield-network.md (lesson format). **Topic:** Network Analysis for Grocery Access in QGIS. **Timeframe:** Teaching 70 min, Exercises 35 min (total ~85 min suggested pacing: 10 intro + 15 projection + 20 shortest path + 15 service area + 10 discussion + 15 challenge).

## Lesson Goals and Key Question

**Scenario:** Assess grocery store accessibility from residence hall/apartment/neighborhood considering movement constraints imposed by road network.

**Central concept:** Network distance differs significantly from straight-line distance; network analysis reveals routing detours, disconnections, barriers.

**Three analytical tasks:** (1) Prepare grocery/road data; (2) Calculate routes from single origin to multiple stores; (3) Create service areas estimating reachable network streets within travel cost threshold.

## Data Setup and Layers

**Required:** grocery_stores (points, QField-collected), roads (line network), study_area (polygon boundary). **Projected CRS:** NAD 1983/UTM 16N for Indiana (critical for meaningful distance units). **Data quality checks:** Detect duplicate points, points outside study area, stores in parking lots vs entrance frontage, disconnected road segments, mismatched CRS.

## Analytical Workflow

**Step 1-2: Setup** — Load layers, inspect attributes (store name, type, verification status), reproject to UTM 16N.

**Step 3: Clip roads** — Processing Toolbox > Clip; roads_projected overlaid by study_area_projected → roads_clip (reduce processing time).

**Step 4: Origin point** — Create temporary point layer at chosen location (single origin first keeps analysis legible before multi-origin scaling).

**Step 5: Shortest path analysis** — Processing Toolbox > "Shortest path (point to layer)"; parameters: network=roads_clip, start=origin_point, endpoints=grocery_stores_projected; outputs: routes_to_grocery (line), non_routable_grocery (identify unreachable stores revealing data quality problems).

**Step 6-7: Route inspection** — Symbolize layers distinctly; Field Calculator creates route_m ($length) and route_km ($length/1000) fields; sort table by distance to identify nearest stores by network distance.

**Step 8-9: Service areas** — Processing Toolbox > "Service area (from layer)"; network=roads_clip, starts=grocery_stores_projected, travel cost=800m (walkable) or adjusted thresholds; output shows network segments reachable within cost limit.

## Interpretation and Extensions

**Discussion questions:** Which neighborhoods well-served? How does 400m, 800m, 1600m threshold change accessibility perception? **Caveats:** Road centerlines ≠ sidewalks; driving-oriented networks ≠ pedestrian access; missing factors (sidewalk quality, crosswalks, safety, hours, disability access).

**Extensions:** Compare shortest vs fastest paths, multi-housing origin workflow, variable service area thresholds, reproducible analysis via Processing Model Designer, final report/story map export.

**Outputs saved:** grocery_stores_projected, roads_clip, origin_point, routes_to_grocery, non_routable_grocery, grocery_service_area (reused in subsequent episodes on multi-neighborhood comparison, census integration, map design).

**Common problems:** Inconsistent projections, grocery points far from road layer, clipped networks breaking routes, confusing service areas with buffers, losing temporary layers.

## Summarized attachments
- **qfield-network.md** (qfield-network.md, md): QGIS network analysis lesson (70 min teaching, 35 min exercises) on calculating grocery store accessibility using road network shortest paths and service areas, covering data setup with QField-collected points and road network layers, projected coordinate system preparation (NAD 1983 UTM 16N), data quality inspection (duplicate points, disconnected roads), shortest path calculation from origin to multiple stores with field calculator for distance metrics, service area generation for walkable/drivable access thresholds, and interpretation of network-based accessibility compared to straight-line distance.

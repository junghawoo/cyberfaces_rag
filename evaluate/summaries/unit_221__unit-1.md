---
title: "Unit 1"
unit_id: 221
course_id: 0
slug: unit-1
is_course: 0
---

# Unit 1

Gateways22 Anvil Composable tutorial: hands-on introduction to Rancher Kubernetes platform deployment, database management, microservice architecture, and autoscaling at Purdue RCAC.

**Source:** Gateways22 Anvil Composable Tutorial.pdf. **Platform:** Anvil Composable Subsystem (composable.anvil.rcac.purdue.edu), Rancher UI, Kubernetes, RCAC. **Instructional format:** Four-part progressive exercises plus open-ended exploration.

## Part 1: Rancher Environment Access

**URL:** https://composable.anvil.rcac.purdue.edu. **Login:** Local User with tutorial account (username/password provided). **Navigation:** Select "anvil" cluster > TutorialXX project. **Key concepts:** Namespaces (Kubernetes virtual clusters with isolation/quotas), Projects (Rancher grouping), kubectl (command-line cluster interaction).

**Commands:** kubectl get ns tutorialXX (view namespace); kubectl describe ns tutorialXX (quota info); kubectl -n tutorialXX get services (verify services).

## Part 2: Database Deployment with Persistent Storage

**Application:** PostgreSQL/PostGIS database with GIS data (Michigan highway system). **Deployment steps:**
1. Create workload: name="roads", image=registry.anvil.rcac.purdue.edu/tutorial/postgis
2. Environment variable: POSTGRES_PASSWORD (tutorial only; use Kubernetes secrets in production)
3. Persistent volume: anvil-block (Ceph-based SSD storage), 2 GiB, mount point=/var/lib/postgresql/data, sub-path=data
4. Resource limits: CPU=2000 mCPU, Memory=2000 MiB
5. Database setup via shell: createdb gisdb; psql -U postgres -d gisdb -f /data/tutorial.sql

## Part 3: Microservice Exposure and Data Access

**Service creation:** Layer-4 LoadBalancer on port 5432 with MetalLB annotation (anvil-private-pool). **DNS:** servicename.namespace.anvilcloud.rcac.purdue.edu (auto-configured). **Client access:** JupyterHub (https://tutorial.anvilcloud.rcac.purdue.edu) with Jupyter notebooks querying postgis via SQL; example creates Michigan highway map and analyzes township highway coverage.

## Part 4: Science Gateway Deployment and Autoscaling

**Application:** CoExplorer (gene coexpression network visualization; maize dataset). **Deployment:** Image=registry.anvil.rcac.purdue.edu/tutorial/coexp-maize; CPU=1000 mCPU, Memory=4000 MiB; public LoadBalancer (anvil-public-pool) on port 8866. **HPA (Horizontal Pod Autoscaler):** Min replicas=1, Max=3, metric=CPU average utilization 10% threshold; automatically scales replicas based on load.

**Features:** Filter by Gene ID (Zm00001d002580), coexpression network graphs (decay denominator=5, module N005M00582), differential expression plotting.

## Part 5: Open Exploration

Remaining tutorial time for participants to deploy additional applications with presenter guidance.

## Key Technologies and Services

**Infrastructure:** Kubernetes, Rancher, MetalLB load balancing, Ceph block storage. **Services:** PostgreSQL/PostGIS (spatial database), JupyterHub (notebook interface), CoExplorer (science gateway), Docker containers. **Networking:** Private IP pool (internal), public IP pool (internet-facing), DNS auto-provisioning, Layer-4 load balancing.

**Learning outcomes:** Kubernetes deployment, namespace/project management, persistent storage, service exposure, autoscaling, science gateway deployment, database management via CLI and Jupyter.

## Summarized attachments
- **Gateways22 Anvil Composable Tutorial** (Gateways22 Anvil Composable Tutorial.pdf, file): Comprehensive hands-on tutorial for Purdue RCAC's Anvil Composable Kubernetes platform covering Rancher UI login and navigation, Kubernetes namespace and project management, PostgreSQL/PostGIS database deployment with Ceph persistent block storage, microservice exposure via LoadBalancer services with MetalLB annotations, DNS auto-configuration, data access via JupyterHub Jupyter notebooks with SQL queries for GIS analysis, science gateway deployment (CoExplorer gene coexpression network visualization), and horizontal pod autoscaling (HPA) configuration with CPU threshold-based replica management.

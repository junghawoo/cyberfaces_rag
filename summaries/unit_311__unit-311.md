---
title: "Unit 311"
unit_id: 311
---

# Unit 311

This comprehensive unit covers high-performance computing (HPC) and containerization basics, primarily delivered through tutorial presentations and practical examples for the Anvil supercomputing cluster and academic research computing environments.

**Instructors and Resources:** Materials authored by Christopher Thompson and Jungha Woo from Purdue University (dated August 2025 and July 2025). Multiple source files include: `Academic HPC Resources and Containers.pdf`, `HPC_Cloud_Anvil_tutorial.pdf`, `HPC_Cloud_Anvil_tutorial_07282025-1.pdf`, `HPC_Cloud_Anvil_tutorial_07282025.pdf`, `HPC_Cloud_Anvil_tutorial_07312025.pdf`, and `HPC_Cloud_Anvil_tutorial_08012025.pdf`.

**Core Topics:**

1. **Academic HPC Services** — Overview of campus cluster programs offered by RCAC (Purdue), SDSC, TACC, and others. Explains campus-based resource access models (free funding, node purchase/time-sharing, usage billing) and traditional access methods including SSH terminal access, remote desktop sessions, web-based services (Jupyter Notebooks, domain-specific gateways, Open OnDemand), scheduled job submission with queue waiting, and resource monitoring.

2. **NSF ACCESS Program** — National HPC resources for US researchers and educators. Purdue's Anvil cluster participates, with 90% of compute time available to ACCESS program users. Allocation tiers: Tier 1 EXPLORE (anyone can try), Tier 2 DISCOVER, Tier 3 ACCELERATE, Tier 4 MAXIMIZE. Service units (SUs) measure compute time; generally 1 SU = 1 CPU hour. Resource allocation process: proposal submission → committee review → award.

3. **Containers: Concepts and Comparison** — Explains traditional executables (bare metal, OS-controlled environment), Virtual Machines (complete OS simulation, portable but resource-heavy), and Containers (sandboxed, lightweight, shared kernel via Docker/Apptainer engines). Benefits: Portability (develop locally, run identically on HPC), Reproducibility (publish container image or Dockerfile for exact recreation). Container lifecycle: write blueprint script → build image → distribute → pull and run.

4. **Container Systems and Tools** — Linux Containers (LXC) history, Docker popularity and community growth, modern engines: Singularity/Apptainer, podman, containerd. **Docker vs. Singularity/Apptainer** — Docker for personal machines, local testing, learning; Singularity/Apptainer for supercomputers, Slurm-based schedulers, secure multi-user environments. Docker requires root access; Apptainer does not. Docker not allowed on Anvil for security; Apptainer is standard. Root requirement, file system mounting behavior, and security model differ.

5. **Anvil and Open OnDemand** — Apptainer containers supported on Anvil. Open OnDemand: open-source web-based HPC portal (ondemand.anvil.rcac.purdue.edu). Requires ACCESS account (created at https://operations.access-ci.org/identity/new-user). Features: file browser, terminal, job submission, file upload/download. Access guides and training at https://www.rcac.purdue.edu/knowledge/anvil/access/login/ood.

6. **Purdue Container Support for ACCESS Users** — Purdue Research Computing built popular Apptainer containers and Lmod module support for NVIDIA NGC containers to simplify HPC for new and educational ACCESS users. Goals: simplify NVIDIA GPU-accelerated software use, reduce Docker/Singularity learning curve, enable AI/ML/scientific computing with single command. Users load containers like standard software: `module load ngc pytorch`. Home/scratch directories auto-mounted, GPU-ready, supports batch and interactive jobs.

7. **Lmod Module System** — Software tool dynamically modifying environment (PATH, variables) via module files. Commands: `module load python`, `module purge`. Enables clean, safe environment management on shared systems. https://www.rcac.purdue.edu/knowledge/anvil/software/modules.

8. **NVIDIA NGC (NVIDIA GPU Cloud) Containers** — Ready-to-use containers for AI/ML and HPC (PyTorch, TensorFlow, RAPIDS, etc.). Available formats: Docker (native from NGC, provided by NVIDIA for Docker/Kubernetes setups), Singularity .sif (built via `apptainer build docker://nvcr.io/nvidia/pytorch:22.01-py3`). Users pull from nvcr.io registry. NGC Container Environment Modules (Lmod integration) enable loading as regular software. Containers auto-start, mount directories, set up GPU support.

9. **Available NGC Containers on Anvil** — autodock, chroma, gamess, gromacs, julia, lammps, milc, namd, nvhpc, parabricks, paraview, pytorch, qmcpack, quantum_espresso, rapidsai, relion, tensorflow, torchani.

10. **Practical Examples:**
    - **Matrix Multiplication** — PyTorch example: device detection (GPU CUDA or CPU fallback), 3000×3000 matrix initialization, torch.matmul multiplication, output summary. Submit via `sbatch submit.sh`, output file: `pytorch-matmul-{JobID}.out`.
    - **MNIST Digit Classification** — Modified National Institute of Standards and Technology dataset: 70,000 grayscale 28×28 images of handwritten digits (0–9). SimpleCNN architecture: Conv2d(1,32,3,1) → MaxPool2d(2) → Conv2d(32,64,3,1) → MaxPool2d(2) → Flatten → Linear(1600,128) → Linear(128,10). Key concepts: data loading/normalization, Conv/ReLU/Pool layer implementation, training loop (forward pass → loss → backprop → optimization), model saving for inference. Trains for three epochs, tests on digit seven. Test outputs show varying accuracy based on training epochs and input image preprocessing.
    - **Apptainer/Singularity Container Creation** — Build from NGC Docker images: `apptainer build pytorch.sif docker://nvcr.io/nvidia/pytorch:22.01-py3`. Does NOT require Docker Engine, NVIDIA Container Toolkit on host; requires Internet, Apptainer install, optional NVIDIA drivers if using GPU (--nv flag). Process: HTTP layer-by-layer image pull, .sif conversion, Dockerfile metadata resolution via Apptainer user-space, skopeo and oci-image-tools. Submit Apptainer jobs on Anvil with submit file specifying allocation, wall time, node count. Output from `mnist_train_and_infer.py` saved in submission directory.

11. **Available Containers and Registries** — Pre-built examples: NVIDIA NGC (AI/ML/HPC), BioContainers (genomics, proteomics, bioinformatics: FSL, AFNI, FreeSurfer), Neurodocker (neuroimaging), GeoDocker (geospatial: GDAL, GeoServer, PostGIS), OpenFOAM (CFD), Quantum Chemistry (Gaussian, ORCA, Q-Chem). Registries: Docker Hub (widest use), GitHub Container Registry (GHCR, CI/CD integration), NVIDIA NGC (AI/ML/HPC optimization), Anvil Registry (curated for Anvil). Users can pull, share, version, and push containers for collaboration.

12. **Advanced Container Topics** — Dockerfile/Apptainer .def files (script specifying dependencies, setup steps, file copying, directories, commands, ports, mount paths). Extending existing containers: `FROM` base image declaration to add layers. Mounting in Docker: bind mounts (host directory) and volumes (Docker-managed); syntax: `docker ... -v {path/volume}:{container/path}`. Apptainer auto-mounts HOME, pwd; manual options more complex (https://apptainer.org/docs/user/main/bind_paths_and_mounts.html).

13. **Running Services with Containers** — Kubernetes concepts, Anvil Composable subsystem, Rancher orchestration. Example use case: JupyterHub deployment for community access. Potential for scaling multiple copies for large projects.

14. **Training Resources** — RCAC training at rcac.purdue.edu/training: Anvil 101, Anvil Open OnDemand 101, Containerized Bioinformatics Applications for HPC, Interactive Computing on Anvil Composable. Purdue courses: Unix 101/102/201, Jupyter Kernels and HPC, Running Bioinformatics Analyses in HPC, Open OnDemand 101. Comprehensive container slides: https://www.rcac.purdue.edu/training/containers101 (what containers are, Docker/Singularity comparison, Singularity basics, RCAC cluster usage, deployed containers), https://www.rcac.purdue.edu/training/biocontainers101 (biocontainers deployment and building).

**Guest Speaker:** Iman Haqiqi on HPC and container use case in GLASSNET project.

This unit equips learners with knowledge to choose appropriate HPC resources (campus vs. ACCESS), understand container advantages for reproducibility and portability, deploy containerized workflows on Anvil using Apptainer and NGC, and leverage Purdue's Lmod module system for simplified container management in educational and research settings.

## Summarized attachments
- **Academic HPC Resources and Containers** (`Academic HPC Resources and Containers.pdf`, file): Presentation slides by Christopher Thompson and Jungha Woo covering academic HPC service delivery models (campus clusters, NSF ACCESS program), access methods (SSH, remote desktop, web-based services like Open OnDemand), container fundamentals (Docker, Singularity/Apptainer differences), Anvil cluster resources, and NVIDIA NGC container system integration for educational users.
- **HPC and Cloud Computing on Anvil and Containerization Basics** (`HPC_Cloud_Anvil_tutorial.pdf`, pdf): Comprehensive tutorial by Christopher Thompson and Jungha Woo on research computing in academics, container concepts versus traditional executables and VMs, Apptainer usage on Anvil, container registries (Docker Hub, NVIDIA NGC, Anvil Registry), three practical examples (PyTorch matrix multiplication, MNIST digit classification CNN, building Apptainer/Singularity containers), Dockerfile extension techniques, file mounting strategies, Kubernetes/Rancher for service deployment, and RCAC training resources. Includes guest speaker content on GLASSNET containerization use case.

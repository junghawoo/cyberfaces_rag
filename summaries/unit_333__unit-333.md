---
title: "Unit 333"
unit_id: 333
---

# Unit 333

Guide on managing buckets and objects on Anvil Object Storage (S3-compatible). Adapted from RCAC documentation.

Anvil Supercomputer: NSF-funded (Purdue University, 2021). Partners: Dell, AMD. Specifications: 1 billion+ CPU core hours annually, 5.3 petaflops peak performance, 1,000 compute nodes (dual 64-core AMD Epyc "Milan" processors), 100 Gbps InfiniBand network, specialized GPU and large-memory nodes. Applications: high-performance computing, AI, scientific discovery, student learning, research computing training.

Anvil Object Storage: Highly scalable, durable, secure S3-compatible service based on Ceph. Designed for large-volume data storage and serving. Enterprise/cloud computing principles applied to scientific datasets.

Key concepts: Buckets (top-level containers, unlimited objects per bucket), Objects (files up to 5 TB, any format), Keys (unique object identifiers/filenames), Metadata (content type, size, modified date).

Access methods: Command-line (s3cmd: Linux/Mac/Windows), GUI (Cyberduck: Mac/Windows). Endpoint: s3.anvil.rcac.purdue.edu.

s3cmd installation: pip install s3cmd. Configuration: ~/.s3cfg file with host_base, host_bucket, access_key, secret_key. Run: s3cmd --configure.

Basic s3cmd commands: ls (list buckets), sync (sync directories), put (upload), get (download), mb (make bucket), rb (remove bucket — irreversible), setacl (set access control).

Bucket management: s3cmd mb s3://<bucket> (create), s3cmd rb s3://<bucket> (delete — use caution).

Object management: s3cmd put <file> s3://<bucket> (upload), s3cmd get s3://<bucket>/<object> (download), s3cmd sync s3://<bucket>/<prefix> ./local-folder (sync by prefix).

Public access: s3cmd setacl --acl-public --recursive s3://bucket (make public); access via browser: https://s3.anvil.rcac.purdue.edu/<bucket>/<object-key>. Note: bucket listing disabled via browser; requires full object path.

S3 structure: No real folders (slashes are key parts); download all objects under prefix; objects have unique keys. Example: projectA/2025/run1/output.csv is single object; projectA/2025/run1/ is prefix.

Cyberduck GUI: Download/install, launch, + Open Connection, select S3, enter server/credentials, connect, right-click for actions.

Documentation: Help (s3cmd --help), Download (https://s3tools.org/download), How-To (https://s3tools.org/s3cmd-howto), Cyberduck documentation, RCAC Depot Object Concepts.

Related: Authentication via rcac-help@purdue.edu (Access Key/Secret Key requests).

## Summarized attachments

- **Managing Buckets and Objects on Anvil Object Storage.pdf** (`Managing Buckets and Objects on Anvil Object Storage.pdf`, pdf): Comprehensive guide adapted from RCAC documentation covering Anvil Object Storage management, including Anvil Supercomputer overview (NSF-funded, 1,000 compute nodes, 5.3 petaflops peak), S3-compatible architecture, bucket/object/key/metadata concepts, s3cmd and Cyberduck tool setup and usage, bucket/object management commands, public access control via setacl, and S3 structure details with prefix-based downloading.
- **anvil_s3_logo.png** (`anvil_s3_logo.png`, image): Logo image with OCR text "S3 OBJECT STORAGE"
- **ChatGPT-Image-Aug-15-2025-11_40_02-AM.png** (`ChatGPT-Image-Aug-15-2025-11_40_02-AM.png`, image): Logo/branding image with OCR text "ANVIL S3 OBJECT STORAGE"

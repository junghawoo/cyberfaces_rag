---
title: "Unit 333"
unit_id: 333
---

# Unit 333

## Extracted resources (local files)

### Managing Buckets and Objects on Anvil Object Storage.pdf
*Source file:* `Managing Buckets and Objects on Anvil Object Storage.pdf`  ·  *type:* pdf

Managing Buckets and Objects on Anvil 
Object Storage 
This guide is adapted from RCAC’s documentation and explains how to access and manage 
Anvil’s S3-compatible object storage. 
 
Overview of Anvil Supercomputer 
Anvil is Purdue University’s NSF-funded supercomputer, launched in 2021 to support advanced 
computing for a broad range of research — from traditional high-performance computing to 
modern AI applications. Built in partnership with Dell and AMD, Anvil delivers over one billion 
CPU core hours annually, with a peak performance of 5.3 petaflops, and includes specialized 
GPU and large-memory nodes for machine learning and data-intensive workloads. Its 1,000 
compute nodes feature dual 64-core AMD Epyc “Milan” processors, connected by a 100 Gbps 
InfiniBand network. Beyond powering scientific discoveries, Anvil also serves as a hands-on 
learning platform for students and a training ground for the next generation of research 
computing professionals. 
Anvil Object Concepts 
Anvil Object Storage is a highly scalable, durable, and secure S3-compatible service 
based on Ceph, designed for storing and serving large volumes of data. S3 storage is 
widely used in enterprise and cloud computing, and the same principles apply to 
managing scientific datasets on Anvil. 
Key Concepts 
●​ Buckets: Top-level containers for storing objects. Each bucket has a unique 
name and can hold an unlimited number of objects.​
 
●​ Objects: Individual files (up to 5 TB each) stored in a bucket. Objects can be in 
any format—text, images, video, and more.​

●​ Keys: Unique identifiers for objects within a bucket, similar to filenames, used for 
locating and retrieving data.​
 
●​ Metadata: Additional information stored with an object, such as content type, 
size, and last modified date.​
 
For more details, see RCAC Depot Object Concepts. 
 
Accessing Anvil Object Storage 
The Anvil S3 endpoint can be accessed via command-line or GUI tools. Two common methods 
are: 
●​ Command line: s3cmd (Linux, Mac, Windows)​
 
●​ GUI: Cyberduck (Mac, Windows)​
 
Endpoint: s3.anvil.rcac.purdue.edu 
 
Using s3cmd 
s3cmd is a free command-line tool for managing data in S3-compatible storage. 
1. Installation 
pip install s3cmd 
 
2. Authentication 
You’ll need an Access Key and Secret Key (request from rcac-help@purdue.edu). 
Example .s3cfg file in your home directory: 
[default] 
host_base = s3.anvil.rcac.purdue.edu 
host_bucket = s3.anvil.rcac.purdue.edu

access_key = <your access key> 
secret_key = <your secret key> 
 
Run: 
s3cmd --configure 
 
Choose to save settings so they’re stored in ~/.s3cfg. 
 
3. Basic Commands 
Command 
Description 
s3cmd ls 
List all buckets in your account 
s3cmd sync 
Sync local and S3 directories 
s3cmd put <file> 
s3://<bucket> 
Upload a file 
s3cmd get 
s3://<bucket>/<object> 
Download a file 
 
4. Bucket Management 
s3cmd mb s3://<bucket>    # Create a bucket 
s3cmd rb s3://<bucket>    # Remove a bucket (and all objects inside)

⚠ Deletion is irreversible — use with caution. 
 
5. Object Management 
s3cmd put <file> s3://<bucket>           # Upload file 
s3cmd get s3://<bucket>/<object>         # Download file 
 
 
6. More Information 
●​ Help: s3cmd --help​
 
●​ Download: https://s3tools.org/download​
 
●​ How-To: https://s3tools.org/s3cmd-howto​
 
 
Using Cyberduck (GUI) 
1.​ Download and install Cyberduck​
 
2.​ Launch and click + Open Connection​

3.​ Select S3 from the dropdown​
 
4.​ Enter:​
 
○​ Server: s3.anvil.rcac.purdue.edu​
 
○​ Access Key ID and Secret Access Key​
 
5.​ Click Connect​
 
6.​ Right-click objects to see available actions​
 
 
For detailed instructions, see Cyberduck documentation. 
 
Making S3 Objects Public (s3cmd) 
To make a file or bucket publicly readable: 
s3cmd setacl --acl-public --recursive s3://sample-dataset 
 
A public object can be accessed by anyone with its URL.

Accessing Public Storage on Anvil S3 
Key points about S3 structure: 
●​ No real folders: An “object” is a single file. Slashes (/) in names are just part of the key.​
 
●​ You cannot download “all files in an object” — instead, download all objects under a 
key prefix (what looks like a folder).​
 
●​ Example: projectA/2025/run1/output.csv is one object; “projectA/2025/run1/” is 
a prefix.​
 
To download all objects under a prefix: 
s3cmd sync s3://<bucket>/<prefix> ./local-folder 
 
If the object is public, you can access it directly in a browser: 
https://s3.anvil.rcac.purdue.edu/<bucket>/<object-key> 
 
Note: Even if a dataset is public, Anvil S3 does not allow listing bucket contents via a browser 
— you must know the full object path.

I

## Image text (OCR)

### `anvil_s3_logo.png`
S3 OBJECT STORAGE

### `ChatGPT-Image-Aug-15-2025-11_40_02-AM.png`
ANVIL S3

OBJECT STORAGE

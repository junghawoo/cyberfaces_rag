---
title: "StreamCI tutorial"
unit_id: 288
course_id: 0
level: "Expert"
slug: streamci-tutorial
is_course: 0
objectives:
  - "Get hands on exercise on how to ingest data, configure data processing, and access data using StreamCI"
---

# StreamCI tutorial

**Description:** Placeholder for StreamCI tutorial

## Extracted resources (local files)

### CI4FAIR_StreamCI.pdf
*Source file:* `CI4FAIR_StreamCI.pdf`  ·  *type:* pdf

Enabling Scalable and Reliable Real 
Time Data Services for Sensors and 
Devices in StreamCI 
Jaewoo Shin
Purdue University
08/04/2025
NSF awards 1835822, 
2230092, 2513947

Introduction
• Large volumes of sensor/device data
• Internet of Things
• Smart City
• Precision Agriculture
• Effective management and utilization à enable significant advances 
in diverse areas
• Managing streaming sensor data brings a big challenge…
• Lack of resources and knowledge of DB/cloud services
2

What is StreamCI?
• Streaming sensor data analysis Cyber Infrastructure
• A scalable and flexible sensor data collection and analysis platform
• Help individual researchers to easily collect, process, store, and access 
large volumes of data on the cloud
• With minimal configuration steps
• Features 
• Data management portal
• Easy registration
• Real-time data ingestion 
• Processing pipelines
• Data query and access API
• Authentication
• Data access control
3

System Design and Implementation
4
Data Queue
Anvil Kubernetes Cluster
StreamCI
Portal
Admin/User
Portal
API Pods
...
Data
 processor
Data Pods
Management Pod
A
B
Metadata
api.streamci.org
Query Queue
...
Query processor
Query Pods
Resource 
Monitors
Auth. Pod
Auth Queue
Auth. Info.
Certbot
Mail Queue
Email

Feature Highlights
• Data providers
• Sensor data source registration
• Real-time data ingestion
• Data preprocessing if needed
• Data storage in a cloud database
• Data consumers
• Data access using API
• Data query using filters 
• e.g., date/spatial extent, or value range
• Data visualization 
5

Feature Highlights
6
• Data providers
• Sensor data source registration
• Real-time data ingestion
• Data preprocessing if needed
• Data storage in a cloud database
• Data consumers
• Data access using API
• Data query using filters 
• e.g., date/spatial extent, or value range
• Data visualization 
curl --request POST --data  \
    '{"auth":{"target":"<datasource-name>", \
                     "username":…, "token": …}, \
      "request":{"method": "insert", "data":{…}}}' \
    https://api.streamci.org/data

Feature Highlights
7
• Data providers
• Sensor data source registration
• Real-time data ingestion
• Data preprocessing if needed
• Data storage in a cloud database
• Data consumers
• Data access using API
• Data query using filters 
• e.g., date/spatial extent, or value range
• Data visualization 
curl --request POST --data  \
    '{"auth":{"target":"<datasource-name>", 
                      "username":…, "token": …}, \
      "request":{"method": "query", "query":{…}}}' \
    https://api.streamci.org/query

8
Use Cases

Use Case – StreamCI in a Classroom
• Purdue's "Ecological Sensors and Data" class 
• Environmental sensors were set up and 
the data were pushed to StreamCI 
endpoints in real time 
• the webhook mechanism provided 
by Particle.io 
• Jupyter Notebook for students to 
visualize data and/or analysis 
• Students learned…
• how to use/setup environmental 
sensors with backend system
• how to analyze data to understand 
ecosystems using sensor data from 
the StreamCI system.
9

Use Case – StreamCI in a Field
• For researchers and farmers using plant health sensor (LeafSpec)
• Innovative low-cost handheld hyperspectral image 
• scan a leaf non-destructively 
• provide measurements of the plant’s physiological features 
• Used by 
• Researchers to perform advanced plant phenotyping research 
• Farmers to monitor the health of their crops and to direct fertilizer and pesticide 
application in the field 
• StreamCI has been successfully used to provide a platform for real-
time crop growth
10

Use Case – StreamCI in a Field
11

Use Case – StreamCI in a Field
12

Use Case – StreamCI in a Field
13

Use Case – StreamCI for Manufacturing Environment
StreamCI streaming data processing pipeline with data access API, metadata linkage, libraries, and tools
JupyterHub online workspace for streaming data analytics, visualization, monitoring, and prediction
14
Lambda
S3
IoT Core
Sensor data
Purdue AnalytiXIN Data Lake 
Sensor Data 
Sources
EMC2
IMI
AWS Pipeline
StreamCI Data Pipeline/Repository
JupyterHub Analytics Workspace
CERIAS
Applications
Tools
Analytics Libraries
Streaming Data API
Metadata linking
Sensor Data
High Performance Computing

Use Case – StreamCI for Manufacturing Environment
15

Use Case – StreamCI for Manufacturing Environment
16

Use Case – StreamCI for Manufacturing Environment
17

Use Case – StreamCI for Manufacturing Environment
18
• A web platform that provides
• Real-time monitoring of facility 
operations
• Prediction of future energy usage
• Identification of conservation 
measures to improve energy 
performance and reduce negative 
environmental impacts
• Aim to make the platform 
available to manufacturers 
across Indiana and beyond
Sensors
EMC 2
Air Flow Rate
Temperature
Pump Status
……
Edge
On Site
Cloud
AXIN + Data Lake
Indoor Temperature 
Prediction
Data preprocessing
Feature selection
ML training and validation

Use Case – StreamCI for Manufacturing Environment
19

Use Case – StreamCI for Manufacturing Environment
20

Use Case - Anomaly Detection in Manufacturing Process
21
* The views expressed herein do not necessarily represent the views of the U.S. Department of Energy or the United States Government.

22
Future Work

Future Work
23
• New NSF CSSI Framework grant started in July 2025
• 5 years, $4 million
• Develop an AI-ready streaming data platform for a wide range of 
scientific applications
• Main capabilities
• High level data abstractions that allows data linkage and 
combination
• AI-readiness through novel tools for data preparation and processing 
pipelines
• Low-code application development and integration
• Scalable and seamless service deployment and delivery

Future Work
24
• Broad use cases
• Precision audiology to tackle untreated hearing loss (Dr. Heinz)
• Cross-species precision auditory neuroscience data and diverse auditory data
• Create real-time, individualized auditory profiles using ML/AI models
• Building energy analytics and smart control (Dr. Qu)
• Streaming data (e.g., weather, grid signals, control setpoints, HVAC 
conditions)
• Develop real-time building energy analytics model
• Enable energy prediction and optimal operation
• Plant health and smart corn nitrogen fertilization (Dr. Jin)
• Plant sensor data and environmental data
• Seamless pipeline from farms to researchers
• Predicting plant health and enabling timely decision making

Future Work
25
• Broad use cases (continued) 
• Revolutionizing road condition assessment (Dr. Jahanshahi)
• Diverse data generated by RGB-D sensors, accelerometers, and GPS devices
• Advanced AI-driven analytics for road defect detection
• Digital Twins for Advanced Manufacturing (Dr. Jun)
• Streaming data such as spindle load, axis positions, operating conditions, etc
• Develop a real-time AI model for smart monitoring of manufacturing machines 
and anomaly detection
• Understanding Wildlife Corridors (Dr. Bellisario)
• Acoustic data and camera trap footage
• Biodiversity presence and habitat suitability prediction using ML/AI analysis
• Environmental Sensing and Workforce Training (Dr. Hosen)
• Environmental sensors for water chemistry and air quality
• Education of cloud environmental sensing networks in ecology and environmental 
science fields

Future Work
26

27
Thank you!

Acknowledgement
28
This work was supported by the National Science Foundation 
grants # 1835822 and #2513947.

### CI4FAIR_StreamCI.pdf
*Source file:* `CI4FAIR_StreamCI.pdf`  ·  *type:* pdf

Enabling Scalable and Reliable Real 
Time Data Services for Sensors and 
Devices in StreamCI 
Jaewoo Shin
NSF awards 1835822, 
2230092, 2513947

Introduction
• Large volumes of sensor/device data
• Internet of Things
• Smart City
• Precision Agriculture
• Management and utilization à enable significant advances
• Managing streaming sensor data brings a big challenge…
• Lack of resources and knowledge of DB/cloud services
2

What is StreamCI?
• Streaming sensor data analysis Cyber Infrastructure
• A scalable and flexible sensor data collection and analysis platform
• Help individual researchers to easily collect, process, store, and access 
large volumes of data on the cloud
• With minimal configuration steps
• Features 
• Data management portal
• Easy registration
• Real-time data ingestion 
• Processing pipelines
• Data query and access API
• Authentication
• Data access control
3

System Design and Implementation
4
Data Queue
Anvil Kubernetes Cluster
StreamCI
Portal
Admin/User
Portal
API Pods
...
Data
 processor
Data Pods
Management Pod
A
B
Metadata
api.streamci.org
Query Queue
...
Query processor
Query Pods
Resource 
Monitors
Auth. Pod
Auth Queue
Auth. Info.
Certbot
Mail Queue
Email

Feature Highlights
• Data providers
• Sensor data source registration
• Real-time data ingestion
• Data preprocessing if needed
• Data storage in a cloud database
• Data consumers
• Data access using API
• Data query using filters 
• e.g., date/spatial extent, or value range
• Data visualization 
5

Feature Highlights
6
• Data providers
• Sensor data source registration
• Real-time data ingestion
• Data preprocessing if needed
• Data storage in a cloud database
• Data consumers
• Data access using API
• Data query using filters 
• e.g., date/spatial extent, or value range
• Data visualization 
curl --request POST --data  \
    '{"auth":{"target":"<datasource-name>", \
                     "username":…, "token": …}, \
      "request":{"method": "insert", "data":{…}}}' \
    https://api.streamci.org:8792

Feature Highlights
7
• Data providers
• Sensor data source registration
• Real-time data ingestion
• Data preprocessing if needed
• Data storage in a cloud database
• Data consumers
• Data access using API
• Data query using filters 
• e.g., date/spatial extent, or value range
• Data visualization 
curl --request POST --data  \
    '{"auth":{"target":"<datasource-name>", 
                      "username":…, "token": …}, \
      "request":{"method": "query", "query":{…}}}' \
    https://api.streamci.org:8792

Use Case – StreamCI in a Classroom
• Purdue's "Ecological Sensors and Data" class 
• Environmental sensors were set up the 
data were pushed to StreamCI endpoints 
in real time 
• the webhook mechanism provided 
by Particle.io 
• Jupyter Notebook for students to 
visualize data and/or analysis 
• Students learned…
• how to use/setup environmental 
sensors with backend system
• how to analyze data to understand 
ecosystems using sensor data from 
the StreamCI system.
8

Use Case – StreamCI in a Field
• For researchers and farmers using plant health sensor (LeafSpec)
• Innovative low-cost handheld hyperspectral imager 
• scan a leaf non-destructively 
• provide measurements of the plant’s physiological features 
• Used by 
• Researchers to perform advanced plant phenotyping research 
• Farmers to monitor the health of their crops and to direct fertilizer and pesticide 
application in the field 
• StreamCI has been successfully used to provide a platform for real-
time crop growth
9

Use Case – StreamCI in a Field
10

Use Case – StreamCI in a Field
11

Use Case – StreamCI in a Field
12

Use Case – StreamCI for Manufacturing Environment
StreamCI streaming data processing pipeline with data access API, metadata linkage, libraries, and tools
JupyterHub online workspace for streaming data analytics, visualization, monitoring, and prediction
13
Lambda
S3
IoT Core
Sensor data
Purdue AnalytiXIN Data Lake 
Sensor Data 
Sources
EMC2
IMI
AWS Pipeline
StreamCI Data Pipeline/Repository
JupyterHub Analytics Workspace
CERIAS
Applications
Tools
Analytics Libraries
Streaming Data API
Metadata linking
Sensor Data
High Performance Computing

Use Case – StreamCI for Manufacturing Environment
14

Use Case – StreamCI for Manufacturing Environment
15

Use Case – StreamCI for Manufacturing Environment
16

Use Case – StreamCI for Manufacturing Environment
17
• A web platform that provides
• Real-time monitoring of facility 
operations
• Prediction of future energy usage
• Identification of conservation 
measures to improve energy 
performance and reduce negative 
environmental impacts
• Aim to make the platform 
available to manufacturers 
across Indiana and beyond
Sensors
EMC 2
Air Flow Rate
Temperature
Pump Status
……
Edge
On Site
Cloud
AXIN + Data Lake
Indoor Temperature 
Prediction
Data preprocessing
Feature selection
ML training and validation

Use Case – StreamCI for Manufacturing Environment
18

Use Case – StreamCI for Manufacturing Environment
19

Use Case - Anomaly Detection in Manufacturing Process
20
* The views expressed herein do not necessarily represent the views of the U.S. Department of Energy or the United States Government.

Future Work
21
• New NSF CSSI Framework grant started in July 2025
• 5 years, $4 million
• Develop an AI-ready streaming data platform for a wide range of 
scientific applications
• Main capabilities
• High level data abstractions that allows data linkage and 
combination
• AI-readiness through novel tools for data preparation and processing 
pipelines
• Low-code application development and integration
• Scalable and seamless service deployment and delivery

Future Work
22
• New NSF CSSI Framework grant started in July 2025
• 5 years, $4 million
• Develop an AI-ready streaming data platform for a wide range of 
scientific applications
• Main capabilities
• High level data abstractions that allows data linkage and 
combination
• AI-readiness through novel tools for data preparation and processing 
pipelines
• Low-code application development and integration
• Scalable and seamless service deployment and delivery

Future Work
23

Acknowledgement
24
This work was supported by the National Science Foundation 
grants # 1835822 and #2513947.

### CI4FAIR_StreamCI_Tutorial.pdf
*Source file:* `CI4FAIR_StreamCI_Tutorial.pdf`  ·  *type:* pdf

StreamCI Tutorial
Jaewoo Shin
Purdue University
08/04/2025
NSF awards 1835822, 
2230092, 2513947

StreamCI Management Portal
• https://mygeohub.org/groups/
gabbs/saci
• Registration on MyGeoHub 
required (not, now)
• Data source registration, data 
viewer, and management
2

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
3

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
4
Database Type: Timeseries
Database Type: NoSQL

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
5

Data Source Management
• Data source management
• Change write permission
• Modify super users and 
data owners 
   (control write permissions)
• Manage schema
(for default and timeseries)
• Add/remove attributes
• Set index
6

Data Viewer
• See recent data
• Results with simple queries
• Display results on the map
7

User Manual
8
..and User Manual!
admin@streamci.org
shin152@purdue.edu

Hands-on experience
9
Open your browser and go to the workshop course page on cyberfaces:
https://www.cyberfaces.org/learn/course/289-cyberinfrastructure-for-
fair-science-workshop/materials

### CI4FAIR_StreamCI_Tutorial.pdf
*Source file:* `CI4FAIR_StreamCI_Tutorial.pdf`  ·  *type:* pdf

StreamCI Hands-on Experience
Jaewoo Shin
Purdue University
08/04/2025
NSF awards 1835822, 
2230092, 2513947

StreamCI Management Portal
• https://mygeohub.org/groups/
gabbs/saci
• Registration on MyGeoHub 
required (not, now)
• Data source registration, data 
viewer, and management
2

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
3

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
4
Database Type: Timeseries
Database Type: NoSQL

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
5

Data Source Management
• Data source management
• Change write permission
• Modify super users and 
data owners 
   (control write permissions)
• Manage schema
(for default and timeseries)
• Add/remove attributes
• Set index
6

Data Viewer
• See recent data
• Results with simple queries
• Display results on the map
7

User Manual
8
..and User Manual!
admin@streamci.org
shin152@purdue.edu

Hands-on experience
9
Open your browser and go to the workshop course page on cyberfaces:
https://www.cyberfaces.org/learn/course/289-cyberinfrastructure-for-
fair-science-workshop/materials

### CI4FAIR_StreamCI_Tutorial.pdf
*Source file:* `CI4FAIR_StreamCI_Tutorial.pdf`  ·  *type:* pdf

StreamCI Hands-on Experience
Jaewoo Shin
Purdue University
08/04/2025
NSF awards 1835822, 
2230092, 2513947

StreamCI Management Portal
• https://mygeohub.org/groups/
gabbs/saci
• Registration on MyGeoHub 
required (not, now)
• Data source registration, data 
viewer, and management
2

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
3

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
4
Database Type: Timeseries
Database Type: NoSQL

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
5

Data Source Management
• Data source management
• Change write permission
• Modify super users and 
data owners 
   (control write permissions)
• Manage schema
(for default and timeseries)
• Add/remove attributes
• Set index
6

Data Viewer
• See recent data
• Results with simple queries
• Display results on the map
7

User Manual
8
..and User Manual!
admin@streamci.org
shin152@purdue.edu

Hands-on experience
9
Open your browser and go to the workshop course page on cyberfaces:
https://www.cyberfaces.org/learn/course/289-cyberinfrastructure-for-
fair-science-workshop/materials

### CI4FAIR_StreamCI_Tutorial.pdf
*Source file:* `CI4FAIR_StreamCI_Tutorial.pdf`  ·  *type:* pdf

StreamCI Hands-on Experience
Jaewoo Shin
Purdue University
08/04/2025
NSF awards 1835822, 
2230092, 2513947

StreamCI Management Portal
• https://mygeohub.org/groups/
gabbs/saci
• Registration on MyGeoHub 
required (not, now)
• Data source registration, data 
viewer, and management
2

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
3

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
4
Database Type: Timeseries
Database Type: NoSQL

StreamCI Data Source Registration
• Register your data source
• Data source name
• Description
• Contact information
• Database type
• Default
• Timeseries
• NoSQL 
• Write permission
• SuperUserWrite
• DataProviderWrite
• PublicWrite
5

Data Source Management
• Data source management
• Change write permission
• Modify super users and 
data owners 
   (control write permissions)
• Manage schema
(for default and timeseries)
• Add/remove attributes
• Set index
6

Data Viewer
• See recent data
• Results with simple queries
• Display results on the map
7

User Manual
8
..and User Manual!
admin@streamci.org
shin152@purdue.edu

Hands-on experience
9
Open your browser and go to the workshop course page on cyberfaces:
https://www.cyberfaces.org/learn/course/289-cyberinfrastructure-for-
fair-science-workshop/materials

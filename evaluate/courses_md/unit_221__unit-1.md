---
title: "Unit 1"
unit_id: 221
course_id: 0
slug: unit-1
is_course: 0
---

# Unit 1

**Description:** Introduction

## Extracted resources (local files)

### Gateways22 Anvil Composable Tutorial
*Source file:* `Gateways22 Anvil Composable Tutorial.pdf`  ·  *type:* file

Part 1: Rancher UI Access
In this section we will login to a Rancher environment to verify account access is working, take a
look around the Rancher UI, and the namespace which we will use to contain our deployments
moving forward.
1.1 Navigate to and login to the Rancher UI
1.
Open the URL https://composable.anvil.rcac.purdue.edu in your web browser
2.
To login to Rancher, click Use a Local User
3.
Fill in your tutorial account information (find your username and password here:
) and click the Log In as Local User button
Gateways22 Anvil Tutorial Logins
1.2 Explore the Rancher UI
A guided tour of the Rancher web interface from tutorial presenter
1.3 View your namespace within your Rancher project
Each participant has been given access to a Rancher project and a namespace, both named to
correspond to their username. Each participant has been given access to a Rancher project that
contains a namespace, both named corresponding to your tutorialXX account. A namespace is
a Kubernetes concept that allows us to create a virtual cluster that can be used for cluster
isolation and allows individual access control and resource quotas. Projects are a Rancher
concept that allows namespaces to be grouped together in order to perform Kubernetes
operations on them as a group. We verify the details of the namespace using the interactive
shell in the Rancher UI to access kubectl.
1.
In your Rancher session in your web browser, select the “anvil” cluster and click your
Tutorial XX project name

2.
Get detailed info about your namespace using kubectl from the Rancher UI
a.
Click the top left menu and click “anvil” under Clusters
b.
Click Cluster
c.
Click Launch kubectl to start an interactive shell
d.
Enter the command kubectl get ns tutorialXX
i.
You should see output similar to the image below with details about your
namespace.
e.
More information about your namespace, including quota information, can be
obtained the with command kubectl describe ns tutorialXX
3.
Close the kubectl command line interface by clicking the Close button
1.4 Optional: Accessing the cluster via kubectl
The kubectl program can be used to interact with Kubernetes clusters via the command line and
is a more powerful tool than using the Rancher web-based UI. There are two ways to use
kubectl to manage Kubernetes resources; from a kubectl shell inside the Rancher UI, similar to
the previous exercise, and remotely via kubectl on a personal computer. Using kubectl on a
personal computer is outside the scope of this tutorial. However, some users may want to
investigate downloading kubectl and accessing Rancher from their laptop.
Part 2: Application Deployment Hands-on Exercise
In this exercise, we will use Rancher to deploy a Postgres database that uses persistent block
storage from Ceph. We will use the Rancher UI to populate the database with Geographical
Information System (GIS) data of the Michigan highway system.
2.1 Deploy the Database
1.
In your Rancher session in your web browser, select the “anvil” cluster and your Tutorial
XX project name.
2.
Select Resources -> Workloads and then click the
button in the right corner.
a.
Set the Name for your deployment, i.e. “roads”
b.
Set the Docker Image to registry.anvil.rcac.purdue.edu/tutorial/postgis
c.
Select the Namespace for your application, i.e. “tutorialXX”, the namespace
created for you.
d.
Set the postgres user password
i.
Select the Environment Variables drop down

ii.
Click the Add Variable button
1.
Use POSTGRES_PASSWORD as the variable
2.
Enter a password as the value
3.
You will need this password to connect to the database in Part 3,
so don’t forget it!
Note: Using an environment variable is ok for a tutorial. Kubernetes
secrets is the better way to do this for a production deployment.
e.
Select the Volumes drop down and click Add Volume…
i.
Select “Add a new persistent volume (claim)”
ii.
Set a unique volume name, i.e. “tutorialXX-volume”
iii.
For Storage Class, select “Use the default class”. The default storage
class for this Kubernetes cluster is “anvil-block”, Ceph-based block
storage on SSDs.
iv.
Request 2 GiB of storage
v.
Leave Single Node Read-Write checked under Customize
vi.
Click Define
f.
Provide the default postgres data directory as a Mount Point for the persistent
volume: /var/lib/postgresql/data
g.
Set Sub Path in Volume to data
3.
Click Show advanced options (bottom right of the page)
a.
Click Security & Host Config
b.
Under CPU Reservation select Limit to 2000 milli CPUs
c.
Under Memory Reservation select Limit to 2000 MiB
4.
Click the Launch button
5.
Wait a couple minutes while your persistent volume is created and the postgis container
is deployed. The “does not have minimum availability” message is expected. But, waiting
more than 5 minutes for your workload to deploy typically indicates a problem.

a.
You can check for errors by clicking your workload name (i.e. roads), then the
lower
button on the right side of your deployed pod and selecting View Logs
6.
If all goes well, you will see an
status for your deployment
a.
Reach out to tutorial presenters for troubleshooting help if all does not go well :)
2.2 Populate the database
To become familiar with shell access in Rancher, we will use the Rancher UI to import the
contents of the database. The database contents are located in the /data directory of the postgis
container and are named “tutorial.sql”.
1.
Create the database
a.
From the Rancher Workloads tab, click the
button next to the green status
bar on the right side of your deployed workload and select Execute Shell
b.
A shell interface on your running postgis container will open
i.
Use ctrl-shift and the + key to increase the shell font size
c.
Create a new database called “gisdb”
# createdb -U postgres gisdb
d.
Verify your database is available in the pod
# ls /data/tutorial.sql
e.
Load the database contents into your database
# psql -U postgres -d gisdb -f /data/tutorial.sql
f.
Verify database contents
i.
Connect to the gisdb database
# psql -U postgres -d gisdb
ii.
Show the tables
gisdb=# \dt ch11.*
g.
Close the container Shell window

Part 3: Accessing Applications Deployed in the Composable
Platform
The exercises in part 2 deployed a postgis database inside the Kubernetes cluster. While we
were able to interact with the database via the command line interface, we won’t be able to
access the application externally without deploying a Kubernetes Service to publish the
postgres port. In this exercise, we will use a LoadBalancer service to automatically assign an IP
address on a private network at Purdue and open the postgres port (5432). A DNS name will
automatically be configured for your service. We will then interact with the database via a
Jupyter notebook.
DNS name format: <servicename>.<namespace>.anvilcloud.rcac.purdue.edu
3.1 - Exposing the postgis database
1.
Mouse over the Resources menu and select Workloads in the Rancher UI
2.
Click the Service Discovery tab
3.
Click the Add Record button
a.
Provide a Name
i.
This will get mapped to <servicename> in your DNS record
b.
Select your Namespace
i.
This will get mapped to <namespace> in your DNS record
c.
Select “One or more workloads” for Resolves To
d.
Click Add Target Workload
e.
Select your postgis workload (i.e. roads)
f.
Click Show advanced options
g.
Select Layer-4 Load Balancer from the As a dropdown
h.
Under Port Mapping, click Add Port
i.
Name the port, i.e. postgres-port
ii.
Enter 5432 (the default postgres port) under Publish the service port
i.
Expand the Labels & Annotations section
i.
Click the Add Annotation button
ii.
Enter the following key/value pair:
metallb.universe.tf/address-pool = anvil-private-pool
j.
Click Create
Kubernetes will now automatically assign you an IP address from the private IP pool
reserved for this tutorial. You can check the IP address by hovering over the “5432/tcp” link on
the Service Discovery page or by viewing your service via the kubectl shell in the Rancher UI.
$ kubectl -n tutorialXX get services
You can also verify your DNS record was automatically provisioned via the kubectl shell:
$ nslookup <servicename>.<namespace>.anvilcloud.rcac.purdue.edu

3.2 Open a Jupyter Notebook via the Anvil Composable Subsystem
A JupyterHub instance has been deployed in the Anvil Composable Subsystem that users can
access to start a notebook and interact with their database. The notebook is provided in /data of
your Jupyter session.
1.
Open https://tutorial.anvilcloud.rcac.purdue.edu/ in your web browser and
log in
NOTE: This JupyterHub instance uses a basic authentication
mechanism. Do not use the username and password you used for
Rancher.
2.
Log into JupyterHub using your tutorialXX account for username and
“gateways2022” as the password.
3.
Make a copy the notebook to your home directory in Jupyter
a.
Open a terminal session in Jupyter by clicking the New > Terminal
link
b.
Copy the notebook: cp /data/tutorial-notebook.ipynb ~
4.
Click the notebook to open it in Jupyter
3.3 Run the contents of the notebook
Jupyter notebooks consist of cells that include descriptions and code blocks that can be
executed by selecting the cell and clicking the
button or by holding the Control or
Command (Apple) key and pressing Enter.
1.
Run the first cell to import the required python modules
2.
Update the values in the second cell to match how you configured your database in Part
2.1 and service in Part 3.1
3.
Run the remaining cells of the notebook to create a map of all the highways in Michigan
and determine which township has the most (and least) miles of highway.

Part 4: Science Gateway Deployment
In the fourth part of the tutorial, users will deploy a science gateway, make it accessible on the
Internet and use the Horizontal Pod Autoscaler to scale the application. The guides for this
section are less detailed, please refer to instructions from the previous exercises if you don’t
recall some steps.
4.1 - Deploy a Science Gateway
In this exercise, we will deploy CoExplorer, a science gateway used for interactive visualization,
filtering and analysis of gene coexpression network data. Since we’re from Indiana, we’ll deploy
a CoExplorer instance with gene expression data from maize.
1.
Create a Deployment using the following image:
registry.anvil.rcac.purdue.edu/tutorial/coexp-maize
2.
Persistent Storage is not needed for this container
3.
Under the Security & Host Config section in advanced options, set both a CPU
Reservation and CPU Limit of 1000 milli CPUs (setting the reservation is important for
exercise 4.2). Set both a Memory Reservation and Memory Limit of 4000 MiB
4.
Deploy an Layer-4 LoadBalancer service for this workload on port 8866
a.
In the Labels & Annotations section, tell Rancher to assign an IP address from
the public pool
metallb.universe.tf/address-pool = anvil-public-pool
b.
Your CoExplorer application will now be accessible on the public Internet at
<servicename>.<namespace>.anvilcloud.rcac.purdue.edu:8866
Note: Using a Kubernetes Ingress would be a more elegant solution than using a
non-standard port for this web application. In Part 5, participants can explore
defining an Ingress with a custom hostname.
5.
Use CoExplorer
a.
Click the Filter tab
b.
Under the Filter by Gene ID section, put Zm00001d002580 in the input field,
scroll down and hit the Apply Filter button under Filtered Gene List
c.
Click the Plot by Co-expression tab
i.
In the Select Network Graph section, select a decay denominator of 5
and then select the N005M00582 module
ii.
The network graph will automatically update
d.
Click the Plot Differential Expression tab
i.
Select a Gene and click the Create Plot(s) button to view the differential
expression plot

4.2 - Automatically Scale your Science Gateway
Let’s say the dataset you produced on Anvil and made available via CoExplorer becomes wildly
popular with many researchers across the world. A single instance of CoExplorer might not be
able to keep up with the demands for analyzing the data. Kubernetes provides the Horizontal
Pod Autoscaler (HPA) to automatically scale your application based on configurable criteria,
typically CPU or Memory utilization. As your CoExplorer application uses more resources,
Kubernetes can automatically increase the number of replicas in your deployment to meet the
increase in demand. The LoadBalancer service will automatically distribute new clients to
different instances of your application.
1.
Click Resources -> HPA
2.
Click the Add HPA button
a.
Provide a Name
b.
Select the CoExplorer workload for Workload
c.
Set Min Replicas to 1 and Max Replicas to 3
d.
Use “Resource” for Metric Type, “CPU” for Metric Name, “Average Utilization”
for Target Type and 10 for Quantity
i.
Setting a low threshold of 10% will make it easier to trigger the scaling
e.
Click Create
3.
Create some load on your science gateway
a.
The easiest way to do this is to click the Filter tab in CoExplorer, clear any filters
from the text boxes, scroll down to the Filtered Gene List section and click the
Apply Filter button. This will assemble a table of all the data in the dataset.
b.
Open multiple tabs of CoExplorer to generate even more load
4.
On the Workloads page, watch as your CoExplorer deployment automatically scales the
number of replicas to 2 or 3 to meet the increased demand.
5.
You can also check the status of your HPA by clicking Resources -> HPA and
expanding the Status section
6.
With multiple replicas, the LoadBalancer will automatically redirect and distribute new
clients to different replicas of your CoExplorer instance
7.
Once the load subsides, the HPA will automatically scale your application back down to
1, typically within a few minutes.
Part 5: Choose Your Own Composable Adventure
Please take the remaining time of the tutorial to investigate deploying other applications via the
Rancher UI. The tutorial presenters will be available to assist and answer questions along the
way.

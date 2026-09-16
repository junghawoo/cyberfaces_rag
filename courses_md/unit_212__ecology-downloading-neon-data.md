---
title: "Ecology: Downloading NEON Data"
unit_id: 212
course_id: 0
level: "Foundation"
slug: ecology-downloading-neon-data
is_course: 0
---

# Ecology: Downloading NEON Data

## Fetched resources (external URLs)

### Ecology- Download Neon Data (notebook)
*URL:* https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%201/NEON%20Data.ipynb

# Downloading NEON Data
NEON is a national network of research sites funded by the NSF. Each site has teams devoted to collecting a wide array of hydrology, biogeochemistry, and ecology data. A full list of the datasets available can be found at http://data.neonscience.org.

We will be using the R package neonUtilities, which is designed to download and combine datasets the NEON data repository. We will start by downloading a few example datasets and then give you an opportunity to download your own datasets.

```python
library(neonUtilities)
library(ggplot2)
library(dplyr)
```

Jupyter Lab and Jupyter Notebook have a default setting for the R kernel that limits the numbers of columns that can be viewed. In the case of data from NEON and other data repositories with extensive metadata, the limitation on columns can make it difficul to view your data. To change this setting, you can use the function below. This will set the maximum number of columns and rows displayed. Here the columns displayed have been set to 40 and the rows displayed has been set to 10, but these can be changed as desired.

```python
options(repr.matrix.max.cols=40, repr.matrix.max.rows=10)
```

## Setting up your data storage space.

We need a place to save the files that you're going to download. When using bash and related terminals, the directory address _~/_ indicates the home directory for a given user. The command below creates a new directory in that home directory called _neon_data_. If the directory already exists, nothing will be changed and the _dir.create_ function will deliver a warning unless _showWarnings=FALSE_ is included in the command. We're doing this in the function below.

```python
dir.create("~/neon_data", showWarnings=FALSE)
```

## Downloading hydrology data
We will start by downloading hydrology data including discharge, velocity, and channel geometry parameters. We will begin with discharge. Discharge. Each data product at NEON has its own unique [site](https://www.neonscience.org/field-sites/explore-field-sites) and [data](https://data.neonscience.org/data-products/explore) identifier codes that we use to specify the dataset we want to download in the code below.

We will begin by downloading hydrology data for the Arikee River (code ARIK) from the "Continuous Discharge" Data Product (DP4.00130.001).

We will use the function _loadByProduct()_ to download the data. If you have any questions about a given function, you can type _?functionName_, in this case _?loadByProduct_ into a code cell and press ctrl+Enter (or cmd+Enter for macOS users) to get help documentation for that function.

### Discharge

We will begin by loading discharge data from the Arikee River into the data object _Arik_Q_. We use the option _chec.size = FALSE_, which removes an interactive step that requires confirmation download confirmation downloading the requested data. NEON datasets are rarely more than 500 mb in size. If such datasets may cause space concerns, you can change the option to _check.size = TRUE_.

```python
?loadByProduct
```

```python
Arik_Q<-loadByProduct(dpID = "DP4.00130.001",site = "ARIK", check.size = FALSE, startdate = "2023-01", enddate = "2023-12")
```

_output:_
```
Finding available files
```

_output:_
```
|======================================================================| 100%
```

_output:_
```
Provisional data were excluded from available files list. To download provisional data, use input parameter include.provisional=TRUE.

Downloading files totaling approximately 49.510273 MB

Downloading 9 files
```

_output:_
```
|======================================================================| 100%
```

_output:_
```
Unpacking zip files using 1 cores.

Stacking data files
```

_output:_
```
|======================================================================| 100%
```

_output:_
```
Finished: Stacked 2 data tables and 4 metadata tables!

Stacking took 7.610836 secs
```

The dataset you've downloaded contains continuous discharge data as well as a large amount of ancillary metadata. To start unpacking your data, use the _names_ function in R.

Note that there is a lot of data here. This includes a lot of useful metadata, but we just want to look at the discharge estimates right now. See if you can figure out from the results of the structure command the location of the continuous discharge data.

```python
names(Arik_Q)
```

You can check the contents of each of these list elements by using the command _head_ and include the name of the list _Arik_Q_ and the names of the list element that you want to view followed by a dollar sign. The command _head_ will show the first six rows of the data frame or matrix.

```python
head(Arik_Q$csd_continuousDischarge)
```

The discharge time series is inclued in the dataframe "csd_continuousDischarge". Within this dataframe there are a number of columns, the one with the discharge data is called _maxpostDischarge_. The structure of online datasets from NEON and data repositories can sometimes be unintuitive. Fortunately, online repositories also include documentation. This includes a [metadata document from NEON](file:///Users/jdh/Downloads/NEON_continuousQ_userGuide_vD.1.pdf) that describes the nature of data product DP4.00130.001, continuous discharge,in detail. These can be found associated with each dataproduct at data.neonscience.org.

```python
Arik_Q_cD<-Arik_Q[["csd_continuousDischarge"]]
head(Arik_Q_cD)
names(Arik_Q_cD)
Arik_Q_cD$maxpostDischarge
```

Now that we've found the dataset, let's plot it using the ggplot package. Fortunately, this dataset includes a formatted date/time column so plotting is easy.

```python
ggplot(Arik_Q_cD,aes(endDate,maxpostDischarge))+
geom_point(size=2)+
geom_line()
```

#### Try downloading from another site of your choice. Save the continuous discharge dataset in the same directory as we saved the previous file.

### Channel Geometry
Channel geometry is a useful parameter for ecological analysis and some of the analyses that we will conduct in subsequent modules. We can use NEON's [Discharge Field Collection (DP1.20048.001)](https://data.neonscience.org/data-products/DP1.20048.001) to obtain these measurements.

```python
Arik_DFC<-loadByProduct(dpID = "DP1.20048.001",site = "ARIK", check.size = FALSE)
```

As before, we have to use the structure command to find the data we need. If you review the NEON documentation for this dataset, you will note that field surveys are conducted with the aid of an accoustic doppler current profiler (ADCP). The results of these surveys are summarized in the  list element _dsc_individualFieldData. This is the dataframe that has the hydraulic geometry parameters we're looking for!

```python
str(Arik_DFC)
Arik_HG<-Arik_DFC$dsc_fieldDataADCP
```

We can use these data to assess the relationship between different hydraulic parameters.

```python
names(Arik_HG)
head(Arik_HG)
Arik_HG$Channel_Width<-Arik_HG$sectionArea/Arik_HG$waterDepth
ggplot(Arik_HG,aes(waterDepth,sectionArea))+geom_point()
ggplot(Arik_HG,aes(Channel_Width,waterDepth))+geom_point()

```

### Rating Curve
Finally, we want to be able to download, view, and evaluate rating curves that were used to produce continuous discharge measurements from pressure transducers. These are obtained from the [Stage-Discharge Rating Curves (DP4.00133.001)](https://data.neonscience.org/data-products/DP4.00133.001) dataset.

```python
Arik_RC<-loadByProduct(dpID = "DP4.00133.001",site = "ARIK", check.size = FALSE)
```

```python
str(Arik_RC)
```

```python
Arik_DC<-Arik_RC$sdrc_gaugeDischargeMeas
names(Arik_DC)
str(Arik_DC)
head(Arik_DC)
```

```python
ggplot(Arik_DC,aes(gaugeHeight,streamDischarge))+geom_point()
```

## Water Chemistry Data
There are two types of water chemistry data available from NEON and other portals. There are individually collected grab samples as well as continuously collected sensor data. Both types of data have their own advantages and drawbacks and are most useful when collected side-by-side. NEON collects a variety of grab samples and also deploys a number of _in situ_ water sensors.

Grab samples collected include [water quality/chemistry (anions, cations, conductivity, pH, and various forms of carbon and
nutrients including total, dissolved and particulates)](https://data.neonscience.org/data-products/DP1.20093.001), dissolved gasses (nitrous oxide, methane, carbon dioxide), and surface water stable isotopes ()

Sensors deployed for _in situ_ data collection include a [YSI EXO 2 Multiparameter Sonde (temperature, conductance, pH, fluorescence dissolved organic matter (fDOM), dissolved oxygen)](https://data.neonscience.org/data-products/DP1.20288.001), [SUNA V2 Nitrate Sensor (nitrate, absorbance at 254 nm)](https://data.neonscience.org/data-products/DP1.20033.001).

### Grab Sample Data
We will download grab sample data, again using the Arikee River site as our example.

```python
Arik_WC<-loadByProduct(dpID = "DP1.20093.001",site = "ARIK", check.size = FALSE)
```

```python
str(Arik_WC)
```

Let's extract nitrate, chloride, and pH values and plot these over time!

There are two datasets of interest, the first contains data collected by the local NEON domain (swc_domainLabData), the second contains data collected by an externally contracted lab (swc_externalLabDataByAnalyte), we're going to extract both of these datasets.

```python
Arik_DomainWC<-Arik_WC$swc_domainLabData
Arik_ExternalWC<-Arik_WC$swc_externalLabDataByAnalyte
```

```python
names(Arik_DomainWC)
head(Arik_DomainWC)
names(Arik_ExternalWC)
head(Arik_ExternalWC)
```

As you can see, most of the water chemistry data are contained in the Arik_ExternalWC dataset. You can examine the analyte for each dataset by accessing the columns as shown in the cell below. Let's plot iron (Fe) and Nitrate/Nitrate (NO3+NO2 - N) values over time

```python
unique(Arik_ExternalWC$analyte)
```

```python
Arik_WC_Plot<-subset(Arik_ExternalWC,analyte=="Fe" | analyte =="NO3+NO2 - N")
ggplot(Arik_WC_Plot,aes(x=collectDate,y=analyteConcentration,color=analyte))+
    geom_point(size=2)+
    facet_wrap(.~analyte,ncol=1,scales="free_y")
```

### Photosynthetically Active Radiation Data
Photosynthetically active radiation (PAR) is a key input for many ecosystem models that involve photosynthesis. Given the importance of these data to future models, we will learn how to download these data here.

### Continuous Sensor Data
Now we will practice downloading, extracting, and plotting _in situ_ sensor data using the Water Quality (DP1.20288.001) dataset. First we will download the dataset and examine its structure. For the YSI EXO 2 water quality data, the dataframe is contained in the list as "waq_instantaneous"

```python
Arik_WQ<-loadByProduct(dpID = "DP1.20288.001",site = "ARIK", check.size = FALSE)
```

```python
str(Arik_WQ)
Arik_WQ_Data<-Arik_WQ$waq_instantaneous
```

```python
head(Arik_WQ_Data)
names(Arik_WQ_Data)
```

Now we can easily plot different parameters using ggplot or the plotting function of choice. In this example, we are plotting specific conductance (specificConductance) and dissolved oxygen percent saturation (localDissolvedOxygenSat). Remember, as always, you can reference the data product documentation if you are unsure about the meaning of a given variable. Caution, the dataset is large so if you plot the entire dataset this may take a moment.

```python
ggplot(Arik_WQ_Data,aes(x=startDateTime,y=specificConductance))+
    geom_point()

ggplot(Arik_WQ_Data,aes(x=startDateTime,y=localDissolvedOxygenSat))+
    geom_point()
```

## Biodiversity Data

### Macroinvertebrate Biodiversity Data
Macroinvertebrate diversity is a key dataset for water quality regulations. Many of the determinations regarding water quality under federal water protection laws in the United States are based on the diversity of benthic macroinvertebrates in streams and rivers.

[Macroinvertebrate collection](https://data.neonscience.org/data-products/DP1.20120.001) is conducted routinely at all NEON aquatic sites. We are going to download and extract macroinvertebrate species counts in preparation for 

```python
ARIK_MI<-loadByProduct(dpID = "DP1.20120.001",site = "ARIK", check.size = FALSE)
```

Again we want to look at the names of the dataset to see where the macroinvertebrate biodiversity data are located. Note the list element _inv_taxonomyProcessed_, this contains the processed taxonomy that you want to use.

```python
names(ARIK_MI)
```

As before we want to save the processed taxonomy data in a new dataframe so that it can easily be accessed in the future.

```python
ARIK_MI_Diversity<-as.data.frame(ARIK_MI$inv_taxonomyProcessed)
```

There are many variables included in this dataset. We are particularly interested in the macroinvertebrate taxonomy. This taxonomy information includes _phylum_, _subphylum_, _class_, _subclass_, _infraclass_, _superorder_, _order_, _suborder_, _infraorder_, _superfamily_, _family_, _subfamily_, _tribe_, _subtribe_, and _genus_. In addition, _individualCount_ is a useful variable

```python
names(ARIK_MI_Diversity)
```

We are going to select the important columns before we save this dataset.

```python
ARIK_MI_Taxonomy<-ARIK_MI_Diversity[,c('phylum','subphylum','class','subclass','infraclass','superorder','order','suborder','infraorder','superfamily','family','subfamily','tribe','subtribe','genus','individualCount')]
```

Now we're going to save our dataset as an rds file as before. We want to keep our data organized, so we're storing it in a new sub-directory of your _neon_data_ directory called _biodiversity_.

```python
dir.create("~/neon_data/biodiversity",showWarnings=FALSE)
```

```python
Then we can save the RDS file.
```

```python
saveRDS(ARIK_MI_Taxonomy,"~/neon_data/biodiversity/ARIK_MI_Taxonomy.rds")
```

### Fish Diversity Data

Now we want to download some fish diversity data. Referencing the [data codes](https://data.neonscience.org/data-products/explore), fish diversity data from field surveys are found in [DP1.20107.001](https://data.neonscience.org/data-products/DP1.20107.001). We will again download data from the ARIK site.

```python
ARIK_Fish<-loadByProduct(dpID = "DP1.20107.001",site = "ARIK", check.size = FALSE)
```

Now let's look at the structure of the fish dataset we just downloaded using the _names_ funciton as we've done before.

```python
names(ARIK_Fish)
```

Again we see a few possible options, but here _fsh_bulkCount_ is the 

```python
ARIK_Fish_Taxonomy<-as.data.frame(ARIK_Fish$fsh_bulkCount)
names(ARIK_Fish_Taxonomy)
```

Now let's take a look at the dataset of fish counts. Note that the format of this file is different and fish scientific names (genus and species only) are report as a single column rather than the entire taxonomy of each species with each attribute as a separate column.

```python
ARIK_Fish_Taxonomy
```

The code below will help quickly review the data you've downloaded. There are multiple rows with the same data in this dataset, so the first part of the code block below uses functions from dplyr to sum up the number of fish by scientific name. After that we plot the counts using a bar graph.

```python
arik_fish_data_plot <- ARIK_Fish_Taxonomy %>%
  group_by(scientificName) %>%
  summarize(Total_Count = sum(bulkFishCount))

# Create a bar plot using ggplot2
ggplot(arik_fish_data_plot, aes(x = scientificName, y = Total_Count)) +
  geom_bar(stat = "identity") +
  labs(title = "Species Counts", x = "Species", y = "Count") +
  theme(axis.text.x = element_text(angle = 60, vjust = 1, hjust=1))
```

Finally, we will save the taxonomic diversity dataframe as a RDS file as well have done before.

```python
saveRDS(ARIK_Fish_Taxonomy,"~/neon_data/biodiversity/ARIK_Fish_Taxonomy.rds")
```

### Microbial 

Now we want to download some microbial diversity data. Referencing the [data codes](https://data.neonscience.org/data-products/explore), aquatic benthic microbial diversity data from field surveys are found in [DP1.20086.001](https://data.neonscience.org/data-products/DP1.20086.001). Abundance data includes archaea, bacteria, and fungi. We will again download data from the ARIK site.

```python
ARIK_Microbe<-loadByProduct(dpID = "DP1.20086.001",site = "ARIK", check.size = FALSE)
```

Looking at the names of the different list elements in the downloaded microbial community composition dataset, there are two sents of sequences, _mcc_benthicSeqVariantMetadata_16S_, which contains sequences for prokaryotes and _mcc_benthicSeqVariantMetadata_ITS_, which contains sequences for fungi. Each of these datasets includes samples from many different substrates including sand (episammon) and benthic plants (epiphyton).

In this case these two dataframes (_mcc_benthicSeqVariantMetadata_16S_ and _mcc_benthicSeqVariantMetadata_ITS_) do not contain the actual abundance data, but instead contain urls to csvs containing the relevant datasets for each individual sample. We're going to take a look at both of these datasets and then we will use a script to download all the CSVs and combine them into a single dataframe.

```python
names(ARIK_Microbe)
```

```python
ARIK_Microbe$mcc_benthicSeqVariantMetadata_16S
```

```python
ARIK_Microbe$mcc_benthicSeqVariantMetadata_ITS
```

Now we're using a the urls to combine all the data into a single dataframe. We will do this separate for the 16S and ITS dataframes and then combine those.

```python
#downloadFileUrl
#geneticSampleID
read_csv_filename <- function(filename,dataname){
    ret <- read.csv(filename)
    ret$Source <- filename
    return(ret)
}
ARIK_bcc_urls<-ARIK_Microbe$mcc_benthicSeqVariantMetadata_16S
ARIK_fcc_urls<-ARIK_Microbe$mcc_benthicSeqVariantMetadata_ITS


combined_data_16s <- ARIK_bcc_urls$downloadFileUrl %>%
    lapply(read_csv_filename) %>%
    bind_rows

combined_data_ITS <- ARIK_fcc_urls$downloadFileUrl %>%
    lapply(read_csv_filename) %>%
    bind_rows

ARIK_combined_microbe_data<-bind_rows(combined_data_16s,combined_data_ITS)
```

Now let's take a look at the dataset that we've compiled and assembled:

```python
ARIK_combined_microbe_data
```

One thing you may notice is that this dataset is much larger than previous datasets. This is due to the understandably high individual count and species abundance of microbes in the environment. Also note that the taxonomic information is again formatted differently in this dataset. Here the variable _completeTaxonomy_ includes the entire taxonomy of an organisms from domain down to species, if that has been identified with _;_ separating the different levels of taxonomy. Each level of taxonomic identification is also included in its own column.

We will learn how to plot and analyze these data in future modules, so here we will only display the number of rows in the dataset, which indicates how complex the diversity of microbial samples are, alongside the unique number of operational taxonomic units (OTUs). The OTU concept is used in microbial ecology because the concept of a species in microbial diversity, particularly as it relates to archaea and prokaryotes, is difficult to define due to asexual reproduction and the prevalence of horizontal gene transfer.

```python
paste("Number of rows of dataset:",nrow(ARIK_combined_microbe_data))
paste("Number of unique OTUs:",length(unique(ARIK_combined_microbe_data$completeTaxonomy)))

```

Finally we're going to save the microbial diversity dataset for future use.

```python
saveRDS(ARIK_combined_microbe_data,"~/neon_data/biodiversity/ARIK_combined_microbe_data.rds")
```

## Assignment
### Now it's your turn to download some data!
For each of the data groups above, download datasets from two different NEON sites. For each of the following data groups, do the following to display the contents of the datasets you've downloaded:
* Present a graph o one year of data for each of the following data types (you choose the year):
    * Discharge
    * Channel Geometry
    * Rating Curve
    * Water quality sonde continuous data
    * Photosynthetically Active Radiation (PAR)
* For the following diversity metrics, down the data and present a figure with species taxonomic Order by counts:
    * Fish Biodiversity
    * Macroinvertebrate Biodiversity
* For microbial diversity, present a count of the unique number of OTUs present in your dataset:
    * Microbe Biodiversity

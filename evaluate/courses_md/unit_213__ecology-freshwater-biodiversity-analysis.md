---
title: "Ecology: Freshwater Biodiversity Analysis"
unit_id: 213
course_id: 0
level: "Expert"
slug: ecology-freshwater-biodiversity-analysis
is_course: 0
---

# Ecology: Freshwater Biodiversity Analysis

## Fetched resources (external URLs)

### JN-Freshwater Biodiversity Analysis (notebook)
*URL:* https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Freshwater%20Biodiversity%20Analysis.ipynb

# Setting up the R Environment

```python
library(neonUtilities)
library(ggplot2)
library(doBy)
library(lubridate)
library(dplyr)
library(reshape2)
library(stringr)
```

# Freshwater biodiversity analysis
For this module we are going to learn how to use the biodiversity data we accessed in module 1 to analyze the diversity and community composition for different types of aquatic organisms, from microbes to fish. The abundance and number of taxonomic groups (also known as richness) for each of these different types of organisms is different, so in some cases the most useful analytical tools will vary.

For this module we will primarily use data from the [National Environmental Observation Network (NEON) data portal](https://data.neonscience.org/). We will use the R package _neonUtilities_ to access NEON data. If you are unfamiliar with the workflows for downloading data from NEON, you can use the NEON data download beginner module to learn more. Also reference the [_neonUtilities_ package documentation](https://www.neonscience.org/resources/learning-hub/tutorials/neondatastackr), which will help you familiarize yourself with this process.

## Fish Diversity
We will start with relatively large organisms. Fish are higher on the foodweb than other groups organisms present on the food web, thus it is likely (though not assured) that the number and species richness (number of species) of fish in a give aquatic sampling site will be less than that of other groups such as macroinvertebrates and microbes.

We will begin by downloading fish diversity data from three sites. You can find [metadata about the NEON sites](https://www.neonscience.org/field-sites/explore-field-sites).

We'll start with three aquatic sites: King's Creek (KING), Lower Hop Brook (HOPB), and Mayfield Creek (MAYF).

Recall from the previous module that the data product ID for NEON fish survey data is DP1.20107.001. Note here that we are included recently collected "provisional" data.

```python
fish_survey <- loadByProduct(dpID="DP1.20107.001", 
                            site=c("KING","HOPB","MAYF"),
                            include.provisional=TRUE,
                            check.size=FALSE)
```

NEON datasets include a lot of metadata, so we will have to figure out where the data we need is located. To get the counts we want we are going to look in the list element named _fsh_bulkCount_.

```python
str(fish_survey)
```

Now that we've found where the data are located, we want to manipulate the data so that it is organized by site and sampling date. Since sampling campigns can last multiple days, we are going to use the function _lubridate_ to create columns for the month and year that fish were sampled. That way, we can compile all the data from a multi-day site visit into a single row. At the end we have a dataframe called _fish_counts_sum_ that reports, for each species, the counts for each site on each sampling date.

```python
fish_counts<-as.data.frame(fish_survey[["fsh_bulkCount"]])
fish_counts$date<-as.Date(fish_counts$passStartTime,tz="EST")

fish_counts$year<-year(fish_counts$date)
fish_counts$month<-month(fish_counts$date)

fish_counts_sum<-summaryBy(bulkFishCount ~ siteID + month + year + scientificName, fish_counts, FUN=c(sum))
fish_counts_sum
```

# Diversity metrics
Diversity metrics take several forms. The primary diversity metrics used are alpha diversity, beta diversity, and gamma diversity. 


<div>
<img src="images/DiversityGraphic.jpg" width="500"/>
</div>


Each of these three diversity metrics provides a different look at diversity in the environment. Alpha diversity is the diversity of an indvidual site or sampling location. In ecosystems, there are many sites/patches across the landscape, each of which has its own alpha diversity. The difference between the alpha diversity at individual sites is known as beta diversity, which allows us to compare how community composition differs between sites. Finally, there is gamma diversity that represents all of the diversity across all sites within a given ecosystem.



## Alpha Diversity
Alpha diversity can be captured in a variety of ways and there are a number of metrics and equations to capture these different aspects. The primary dimensions of alpha diversity are richness, eveness, and a set of "composite" diversity metrics that attempt to capture both richness and evenness.

Richness is defined as the total number of taxa in a system. This can be the total number of species, but it is appropriate to report alpha diversity based on other levels of taxonomic organization such as _genus_, _family_, or _order_.

The concept of Evenness is a little more nuanced. Evenness captures whether species counts are evenly distributed across across species or whether certain taxa are disproportionately represented in abundance.

We'll go through each of these different types of alpha diversity metrics and analyze our fish communities for each of these metrics.

### Richness
This is the easiest to calculate. We just need to determine the number of taxa (in this case species) for each sampling location on each sampling date. We can use the _summaryBy_ function to obtain the species richness. We can do this by summarizing each sampling date, sampling site, and species using the _length_ function to add up all unique species. _length_ works in this case, because we are counting the number of elements rather than summing up the number of fish counted.

```python
fish_counts_sum
```

```python
fish_counts_richness<-summaryBy(scientificName ~ siteID + month + year, fish_counts_sum, FUN=c(length))
fish_counts_richness
```

There you have it! the _scientificName.length_ variable is that one that represents species richness (the number of taxa at a site at a given time).

```python
#convert date and month to a date format.
fish_counts_richness$date<-paste(fish_counts_richness$year,"-",fish_counts_richness$month,sep="")
fish_counts_richness$Month_Yr <- as.Date(fish_counts_richness$date, format="%Y-%M")

str(fish_counts_richness)


```

```python
alpha_richness_line_plot<-ggplot(fish_counts_richness,aes(x = Month_Yr, y = scientificName.length, color = siteID))+
geom_point()+
geom_line()

alpha_richness_line_plot
```

Now we're going to try a different method that will help us visualize more easily the difference in diversity between each of the three groups. Here, we are using the _geom_jitter_ function to display each point in a given category with a slight jitter—or horizontal offset—randomly assigned to each point in a given category, which help visualize points that would otherwise be stacked together (try replacing _geom_jitter+ with _geom_point_ and see what happens).

You should also try replacing geom_jitter with [geom_boxplot](https://ggplot2.tidyverse.org/reference/geom_jitter.html), which will display standard boxplot formats that default to displaying the median, placing the box one standard deviation above and below the median, and whiskers that extend to two standard deivations from the median.

```python
alpha_richness_jitter_plot<-ggplot(fish_counts_richness,aes(x = siteID, y = scientificName.length))+
geom_jitter(width=0.2)+
stat_summary(fun.data = "mean_cl_boot", colour = "red", size = 2)+
xlab("Site ID")+
ylab("Species Richness (# of Taxa)")


alpha_richness_jitter_plot
```

It looks like King's Creek (KING) has greater overall richness than Mayfield Creek (MAYF) or Hop Brook (HOPB). There are many ways to test this and currently there is not agreement on the best and most accurate way to test these relationships. Here we will use a linear model to compare alpha richness at these three sites.

```python
## fit ordered logit model and store results 'm'
alpha_richness_site_anova <- lm(scientificName.length~siteID, data=fish_counts_sum)
summary(alpha_richness_site_anova)

```

The ANOVA table presented above shows that the differences between sites are highly significant (p<0.0001). We can't use the signifiance of the coefficients to actually say which sites are significantly greater or less than the other sites without correction. That is where the Tukey test comes in. When we have multiple comparisons within a given statistical test, this increases our risks of finding a significant result when one does not exist (this is known as Type II). Tukey tests and other mean comparison methods add a statistical punishment for each comparison made. This helps keep us honest, but if there are many comparisons being made the statistical power can decrease greatly, resulting in Type I error (wherein a significant difference is incorrectly identified as being non-significant). If you want to learn more about the Tukey Test and the mathematics behind it you can find this [information here](https://rpubs.com/aaronsc32/post-hoc-analysis-tukey).

To run this test, we'll use the output of the ANOVA model above (_alpha_richness_site_anova_). Here we are setting alpha, our significance level, to 0.05.

```python
library(agricolae)

alpha_richness_site_anova_tukey <- HSD.test(alpha_richness_site_anova, "siteID")

alpha_richness_site_anova_tukey
```

Now that we have run the Tukey test, we can see that there is a significan't difference between Kings Creek and the other two sites. Thus King's Creek is placed in group _a_, whereas the other two sites—Hop Brook and Mayfield Creek—are placed in group _b_.

We can use the code below to add these grouping labels to the plot we made above.

```python
# Here we are extracting the group IDs from the output above.
tukey_alpha_richness<-data.frame(alpha_richness_site_anova_tukey$groups)

#We're going to place the site IDs, which are currently only presented as row names, into a column called _siteID_ for consistency and to make our coding work easier.
tukey_alpha_richness$siteID<-row.names(tukey_alpha_richness)

#We want to place the group labebels in the plot above the points plotted, this places the points 20% above the greatest value in the dataset.
tukey_alpha_richness$position<-max(fish_counts_sum$scientificName.length) * 1.2


alpha_richness_jitter_plot + 
geom_text(data=tukey_alpha_richness,aes(x=siteID,y=position, label=groups),size=14)
```

### Diversity
Diversity is a metric that tries to capture not only the number of taxa, but also takes into account whether the degree to which counts are evenly distributed across taxa. There are many metrics that seek to do this, but we are going to focus on what is likely the most important metric, called Shannon Diversity. The equation is as follows:

H' = -∑(p<sub>i</sub> * ln(p<sub>i</sub>))

* _S_ is the total number of species in the community (species richness).
* _p<sub>i</sub>_ is the proportion of individuals belonging to the i-th species, calculated as the number of individuals of species i divided by the total number of individuals in the community.
* ln denotes indicates use of natural logarithm.

There are some packages that have functions for calculating Shannon Diversity, but for edification we're going to define the function ourselves.

```python
library(dplyr)
```

```python
shannon_diversity <- function(species_counts) {
  # Convert counts to proportions
  p <- species_counts / sum(species_counts)
  
  # Calculate Shannon diversity
  H <- -sum(p * log(p))
  
  return(H)
}

#In order to use dplyr to summarize our results efficiently, we have to create a variable that incorporates both site and date.
fish_counts_sum$site_date<-paste(fish_counts_sum$siteID,fish_counts_sum$year)

#Now we can the pipe function (_%>%_) combined with _group_by_ and _summarize_ to calculate Shannon Diversity for each site on each sampling date.
fish_counts_diversity <- fish_counts_sum %>%
    group_by(site_date) %>%
    dplyr::summarize(shannon_diversity = shannon_diversity(scientificName.length))


fish_counts_diversity
```

### Evenness
Last, we are going to look at Pielou's evenness index. Remember that Shannon Diversity (and similar diversity metrics) incorporate both richness and evenness. Pielou's evenness represents the ratio between the observed value of Shannon's Index and the value of Shannon's Index if all categories (R) had the same relative abundance. Calculation of Pielou's evenness is essentially Shannon diversity divided by taxonomic richness.

```python
fish_counts_year_richness <- summaryBy(scientificName ~ siteID + year, fish_counts_sum, FUN=c(length))


fish_counts_diversity$richness <- fish_counts_year_richness$scientificName.length

fish_counts_diversity$evenness <- fish_counts_diversity$shannon_diversity/fish_counts_diversity$richness

fish_counts_diversity
```

## Beta-Diversity
Beta-diversity is a more complicated concept than alpha diversity. Here, we are comparing the difference between two communities, but when there can be dozens of species at each site, how do we quantify the difference in community composition between two—or more—sites. To do this, we have to have a metric that tells us about the difference between two communities. This has been a subject of much work and there are many ways to determine this distance, we will focus on a few here. Three common measures of distance are Euclidean, Manhattan, and Bray-Curtis.


<div>
<img src="images/DistanceGraphic.png" width="500"/>
</div>


We'll start by looking at Euclidean distance, represented by the purple line in the figure above. This is likely familiar to most, as it is based on the Pythagorean Theorem. Let's take two points, A and B, that are located at (q<sub>1</sub>,q<sub>1</sub>) and (p<sub>2</sub>,p<sub>2</sub>). To find the Euclidean distance between the two points we can use the following equation:

$$ d\left( A,B\right) = \sqrt{(q_{1}-p_{1})^2 + (q_{2}-p_{2})^2}$$

In statistics, Euclidean distances can take on more dimensions, as many dimension as there are variables. Thus, the Euclidean distance equation can be generalized to:

$$  d\left( A,B\right)   = \sqrt {\sum _{i=1}^{n}  \left( q_{i}-p_{i}\right)^2 } $$

Where _i_ is the number of variables in the dataset.

By contrast, Manhattan distance is simply the distance between each variable between two points as depicted by the orange lines in the figure above. The equation for calculating this is as follows:

$$  d\left( A,B\right)   = \sum _{i=1}^{n}  \left| q_{i}-p_{i}\right|  $$

Finally, let's introduce Bray-Curtis dissimilarity. This distance metric was created with the explicit goal of created a dissimilarity metric that was specific designed to estimate the dissimilarity between communities at two sites.

$$ BC\left(A,B\right) = \frac{\sum _{i=1}^{n} min(N_{iA}, N_{iB})}{\sum _{i=1}^{n} (N_{iA}, N_{iB})} $$

Here  _N<sub>iA</sub>_ is the number of species i at site A, _N<sub>iB</sub>_ is the number of species i at site B, and _n_ is the number of species across the two sites.

We're going to use _fish_counts_sum_, the list of species count by site and date, to generate a dissimilarity matrix from our species counts. To do this, we first need to convert this dataset to a dissimiliarty matrix. We can use the R package _vegan_ for this, but first we need to create a dissimilarity matrix. Let's start with a basic Euclidean distance matrix. To get started, we have to convert our data from a "long" format to a "wide" format where each column is a different species and each row is a different sampling date at a given site.

```python
library(dplyr)
fish_counts_sum$site_date<-paste(fish_counts_sum$siteID,fish_counts_sum$month,fish_counts_sum$year,sep="-")

fish_counts_wide<-acast(fish_counts_sum, site_date ~ scientificName, value.var = "bulkFishCount.sum", fun=sum)

fish_counts_wide
```

Now we're going to use the package _vegan_ to get Euclidean and Bray-Curtis distance matrices (we will use each separately).

```python
library(vegan)
library(ecodist)

fish_counts_dissimiliarity_euc<-vegdist(fish_counts_wide, method = "euclidean")
fish_counts_dissimiliarity_euc

fish_counts_dissimiliarity_bc<-vegdist(fish_counts_wide, method = "bray")
fish_counts_dissimiliarity_bc
```

#### Ordination
Now that we have these distance matrices, we need a way to actually display the information that we have calculated. To do this, we need to use a multivariate ordination approach. These ordination approaches take datasets with many variables (also known as high dimensional data) and use a statistical approach to reduce the number of variables/dimensions. We will explore three of these approaches Principal Coordinate Analysis (PCoA), Non-Metric Multidimensional Scaling (NMDS), and Correspondence Analysis.

**PCoA** uses a method similar to Principal Component Analysis (PCA), except it is designed to work with distance matrices, rather than matrices of continuous numerical data.

**NMDS** uses a similar approach, but replaces continuous scaling with non-parametric ranking. This is beneficial because it can work with datasets that do not meet assumptions of normality and homogeneity of variance, but makes the exact placement of points on the ordination more difficult to interpret.

**Correspondance Analysis** is a special case similar to to PCoA wherein chi-square distance is used to differentiate between rows.

Thus, we will only use the distance matrices we calculated for analysis using PCoA. In other cases, we will input species counts directly into the scaling function.

```python
pcoa_euclidean <- pco(fish_counts_dissimiliarity_euc, negvals = "zero", dround = 0) # if negvals = 0 sets all negative eigenvalues to zero; if = "rm" corrects for negative eigenvalues using method 1 of Legendre and Anderson 1999.

#the output of the pco command displays the vectors produced by the eigenvalue decomposition
pcoa_euclidean

#use the str command to look at the contents of the file for plotting.
str(pcoa_euclidean)

#from this we can see that we need to extract the second list element to be used for plotting
pcoa_euclidean_vectors<-pcoa_euclidean[[2]]
```

as described above, one of the primary goals of ordination is to reduce the dimensionality of data so that difference across many variables can be viewed in 3 or fewer dimensions.
#thus, our next step is to plot the results of this analysis.

```python
euclidean_pcoa_plot<-ggplot(pcoa_euclidean_vectors,aes(x=X1,y=X2))+
geom_point(size=4)+
xlab("PCoA Dimension 1")+
xlab("PCoA Dimension 2")

euclidean_pcoa_plot

#Now we have some distances, but there is one problem: we don't know which site is which. Fortunately that information is contained within the rownames of the data frame weare using.
pcoa_euclidean_vectors$site_date<-row.names(pcoa_euclidean_vectors)

#Now we can separate the site and date information into separate columns using the _str_split_fixed_ function in _stingr_. There are many ways to do this in R, but this function is designed to work with character strings in dataframes, which is out use case here.
sample_information<-as.data.frame(str_split_fixed(pcoa_euclidean_vectors$site_date, "-", n = Inf))
pcoa_euclidean_vectors$site<-sample_information$V1
pcoa_euclidean_vectors$date<-paste(sample_information$V2,sample_information$V3,sep="-")

#now we can add site color coding to this dataset.
euclidean_pcoa_plot + geom_point(aes(color=site),size=4)
```

Now we can see the differences between the sites, but because these sites all have relatively low diversity, the results aren't all that exciting. Don't worry, we're going to look at macroinvertebrate data from these sites shortly and we will see a lot higher diversity in those datasets.

Now it's your turn to generate a plot like the one above using Bray-Curtis distances instead of Euclidean:

#### NMDS
First, we're going to try our hands at non-metric multidimensional scaling (NMDS). NMDS typically uses Bray-Curtis distances, but for these distances are calculated within these functions so we only have to provide the matrix of species counts. You can use the function below to specify the distance metric used for analysis.

Using NMDS, we can specify the number of dimensions we want using _k_. NMDS uses an iterative fitting solution that can vary depending on how starting conditions are selected. Thus, multiple NMDS analysis are usually run to bootstrap the results and confirm that a "stable solution" has been identified, rather than a local minimum solution. Here we are setting the number of repeates to 100 using _trymax_.

```python
fish_counts_nmds=metaMDS(fish_counts_wide,k=2,trymax=100)
fish_counts_nmds
```

We can assess the fit of the plot using the _stressplot_ funciton to display a Shephard plot, which shows the true dissimilarity of each pair of points, compared to the dissimilarity of the resulting NMDS ordination for each pair of samples/sites.

```python
stressplot(fish_counts_nmds)
```

Finally, we're going to plot the the ordination. Using the _str_ function we can see that the ordination information is stored under the list element called _points_.

```python
str(fish_counts_nmds)

fish_counts_nmds_points<-as.data.frame(fish_counts_nmds$points)

#Here we see that we have a set of coordinates for the two MDS axes generated by the NMDS analysis.
fish_counts_nmds_points
```

Now it's easy to plot our results using ggplot. Again we will extract sample from the rownames of the dataframe.

```python
fish_counts_nmds_points$site_date<-row.names(fish_counts_nmds_points)
sample_information<-as.data.frame(str_split_fixed(fish_counts_nmds_points$site_date, "-", n = Inf))
fish_counts_nmds_points$site<-sample_information$V1
fish_counts_nmds_points$date<-paste(sample_information$V3,sample_information$V2,sep="-")

ggplot(fish_counts_nmds_points,aes(x=MDS1,y=MDS2,color=site))+
geom_point(size=4)
```

## Gamma Diversity
Before we move onto a new type of data, we will look briefly at gamma diversity. Gamma diversity is an important concept and there are multiple ways to define it, but at its simplest, it's assessing the alpha diversity metrics we discuss above on an entire dataset. We'll go back to our old dataset _fish_counts_sum_. 

```python
#For richness, we need only to determine the total number of taxa.
#paste("gamma diversity (richness):",length(unique(fish_counts_sum$scientificName))
paste("gamma diversity (richness):",length(unique(fish_counts_sum$scientificName)))
```

Now try using what you have learned about Shannon Diversity and Evenness to calculate these statistics for gamma diversity:

# Macroinvertebrate Diversity
Now we're going to look at the same set of statistics and metrics using a different stream community: benthic macroinvertebrates. Like fish community composition, macroinvertebrate community composition is regularly collected by NEON. The NEON data product ID for macroinverbrates is [DP1.20120.001](https://data.neonscience.org/data-products/DP1.20120.001). We can download these data using the same approach that we used before, but this time we have changed the dpID to match the macroinvertebrate datatset.

```python
macroinvertebrate_survey <- loadByProduct(dpID="DP1.20120.001", 
                            site=c("KING","HOPB","MAYF"),
                            include.provisional=TRUE,
                            check.size=FALSE)
```

As before we are going to have to do some work to format this dataset. Using the _str_ function we find find a list element called _inv_taxonomyProcessed_. This contains our community composition data.

```python
str(macroinvertebrate_survey)

macroinvert_taxonomy<-as.data.frame(macroinvertebrate_survey[["inv_taxonomyProcessed"]])


```

## Organizing Macroinvertebrate Data
Macroinvertebrate diversity data is often analyzed at different taxonomic levels depending on the depth to which individuals were identified, as well as the application of the data. For example, for some metrics only order level taxonomy needs to be identified. Here we will start with a genus level analysis and then you will do the same analysis using order.

We will start by extracting the counts of each genus across each site and sampling date as we have done for fish diversity data.

```python
macroinvert_taxonomy$date<-as.Date(macroinvert_taxonomy$collectDate)
macroinvertebrate_genus_count<-summaryBy(individualCount~siteID+date+genus,macroinvert_taxonomy,FUN=c(sum))

macroinvertebrate_genus_count
```

We can already see that we have a lot more diversity than our fish dataset. You will notice that some individuals were not identified to genus level (represented by NA in the genus column). We will remove these data and then calculate our diversity indices as befre.

```python
#here we are counting the number of genuses at each site on each sampling day
macroinvertebrate_genus_richness<-summaryBy(individualCount.sum~siteID + date,macroinvertebrate_genus_count,FUN=c(length))

macroinvertebrate_genus_richness

#plotting this as before yields the following.
macroinvert_richness_jitter_plot<-ggplot(macroinvertebrate_genus_richness,aes(x = siteID, y = individualCount.sum.length
))+
geom_jitter(width=0.2)+
stat_summary(fun.data = "mean_cl_boot", colour = "red", size = 2)+
xlab("Site ID")+
ylab("Genus Richness (# of Taxa)")


alpha_richness_jitter_plot
```

The plot is similar to species richness for fish, but note that there is more difference between Hop Brook and Mayfield Creek for macroinvertebrates.

Now it's your turn: calculate an ANOVA and Tukey multiple mean comparison for the macroinvertebrate data as we've done above for the fish community data.

## Macroinvertebrate Shannon Diversity and Evenness
We have now returned to these alpha diversity metrics. Use what you've learned above to calculate the Shanon Diversity and Evenness metrics for macroinvertebrate genus level counts using what you've learned above.

### %EPT Taxa
For macroinvertebrates, there are a few specialized metrics that have been developed based on knowledge about the biology and ecology of this group of organisms. Specifically, research has identified a correlation between water quality and ecosystem health and the percentage of taxa in an aquatic macroinvertebrate community that are members of the taxonomic orders Ephemeroptera (Stoneflies), Plecoptera (Mayflies), and Trichoptera (Caddisflies. As the percentage of macroinvertebrates from these three orders increases, water quality is generally found to be better at a site. We'll take a moment to analyze the percentage of taxa that come from these three groups. 

```python
#macroinvertebrate_order_count<-summaryBy(individualCount~siteID+date+order,macroinvert_taxonomy,FUN=c(sum))
#macroinvertebrate_order_count

macroinvertebrate_order_count_wide<-as.data.frame(acast(macroinvertebrate_order_count,siteID+date~order,value.var=c("individualCount.sum"),FUN=c(sum)))

macroinvertebrate_order_count_wide

#we want to set all NAs to zero
macroinvertebrate_order_count_wide[is.na(macroinvertebrate_order_count_wide)] <- 0

macroinvertebrate_order_count_wide
```

Now to calculate the percentage of taxa that come from the EPT orders, we can use simple row-wise math.

```python
names(macroinvertebrate_order_count_wide)
macroinvertebrate_order_count_wide$EPT_count<-macroinvertebrate_order_count_wide$Ephemeroptera + macroinvertebrate_order_count_wide$Plecoptera + macroinvertebrate_order_count_wide$Trichoptera
macroinvertebrate_order_count_wide$total_ind_count<-rowSums(macroinvertebrate_order_count_wide)
macroinvertebrate_order_count_wide$Percent_EPT<-(macroinvertebrate_order_count_wide$EPT_count/macroinvertebrate_order_count_wide$total_ind_count)*100

macroinvertebrate_order_count_wide$site_date<-row.names(macroinvertebrate_order_count_wide)
macroinvertebrate_order_count_wide$site<-str_split_fixed(macroinvertebrate_order_count_wide$site_date,"_",n=2)[,1]


ggplot(macroinvertebrate_order_count_wide,aes(site,Percent_EPT))+
geom_jitter(width=0.2)+
stat_summary(fun.data = "mean_cl_boot", colour = "red", size = 2)+
xlab("Site ID")+
ylab("% EPT Taxa")
```

Now, the story is a bit different. Use the knowledge you've gained to determine whether Hop Brook has a significantly higher percentage of EPT taxa than the other two sites sampled.

In addition to using %EPT taxa, there are other specialized metrics for macroinvertebrate diversity. For example, identifying each taxon by its functional feeding group (e.g., Shredders, Scrapers, Collector/Gatherers, and Predators), can provide useful information about food webs. Functional feeding groups are not identified in this dataset and assigning them to each taxon in this dataset is beyond the time and scope of this assignment, but interested readers can learn more about the application of functional feeding groups from this open access review article, written by Kenneth W. Cummins, a top expert on this topic: [The Use of Macroinvertebrate Functional Feeding Group Analysis to Evaluate, Monitor and Restore Stream Ecosystem Condition](https://www.gavinpublishers.com/article/view/the-use-of-macroinvertebrate-functional-feeding-group-analysis-to-evaluate-monitor-and-restore-stream-ecosystem-condition).

## Macroinvertebrate Beta Diversity
We're going to use Bray-Curtis distances to conduct a Principal Coordinate Analysis (PCoA) ordination of macoinvertebrate diversity like we did before. This time, the results should be a little more interesting!


```python
macroinvertebrate_genus_count

macroinvertebrate_genus_count_wide<-as.data.frame(acast(macroinvertebrate_genus_count,siteID+date~genus,value.var=c("individualCount.sum"),FUN=c(sum)))

macroinvertebrate_genus_count_wide[is.na(macroinvertebrate_genus_count_wide)]<-0
macroinvertebrate_genus_count_wide
```

Now we're going to convert the taxa counts to a Bray-Curtis distance matrix and then will conduct the PCoA.

```python
macroinvert_genus_dissimiliarity_bc<-vegdist(macroinvertebrate_genus_count_wide, method = "bray")
pcoa_macroinvert_bc <- pco(macroinvert_genus_dissimiliarity_bc, negvals = "zero", dround = 0) # if negvals = 0 sets all negative eigenvalues to zero; if = "rm" corrects for negative eigenvalues using method 1 of Legendre and Anderson 1999.
pcoa_macroinvert_bc_vectors<-pcoa_macroinvert_bc[["vectors"]]

```

No we're going to plot the results of the PCoA as we have done above for the fish beta-diversity.

```python
pcoa_macroinvert_bc_vectors$site_date<-row.names(pcoa_macroinvert_bc_vectors)

site_date_info<-as.data.frame(str_split_fixed(pcoa_macroinvert_bc_vectors$site_date,"_",n=2))
pcoa_macroinvert_bc_vectors$site<-site_date_info[,1]
pcoa_macroinvert_bc_vectors$date<-site_date_info[,2]
pcoa_macroinvert_bc_vectors

```

Now we're finally ready to plot our results. We see that community composition for individual sampling dates (each point) tends to cluster by sampling site, which is expected if there are distinct macroinvertebrate communities in each of the three streams we're analyzing.

Now we want to see if these groups are statistically distinct. We'll start with a visual approach, plotting the 95% confidence ellipses for these three sites. 95% confidence ellipses are similar to 95% confidence intervals, but includes dispersivity of both the x and y dimensions for the data.

```python
pcoa_invert_bc_plot<-ggplot(pcoa_macroinvert_bc_vectors,aes(x=X1,y=X2,color=site))+
geom_point(size=4)

pcoa_invert_bc_plot

pcoa_invert_bc_plot + stat_ellipse(size=2)


```

### Beta-diversity statistical tests
We are going to introduce a pair of statistical approaches for testing whether these groups are distinct. Those approaches are:
* Analysis of similarity (ANOSIM): Uses the similarity between pairs of points to determine the strength of grouping.
* Adonis: A non-parametric multivariate analysis of variance (MANOVA) permutation test. Unlike ANOSIM, Adonis uses _dissimilarity_ to compare groupings.

Both methods use permutations to compute signficance, the number of permutations can be adjusted if computing time becomes an issue.

#### Anosim
In the case of ANOSIM, we get a statistic, _R_, that indicates the degree of similarity for a given grouping. The significance of that grouping is also assessed. To give context to the R statistic for a given grouping, researchers will calculate the ANOSIM _R_ for different groupings and compare the degree of similarity for these different groupings.

Here we will calculate ANOSIM group by Site only, grouped by Date only, and grouped by Site and Date combined. The result for site is highly significant and positive whereas the ANOSIM _R_ for grouping by date is negative (and the test is non-significant), indicating that this grouping is much weaker.

```python
anosim(macroinvertebrate_genus_count_wide, pcoa_macroinvert_bc_vectors$site, distance = "bray", permutations = 9999)

anosim(macroinvertebrate_genus_count_wide, pcoa_macroinvert_bc_vectors$date, distance = "bray", permutations = 9999)

anosim(macroinvertebrate_genus_count_wide, pcoa_macroinvert_bc_vectors$site_date, distance = "bray", permutations = 9999)
```

#### ADONIS
An ADONIS test is specified and interpreted very similarly to a non-parametric ANOVA test such as Kruskal–Wallis, but is not restricted to one explanatory variable as is the case for Kruskal-Wallis. The adonis function in the R package _Vegan_ has been updated recently so the function _adonis2_ is recommended as the most up-to-date version of this test.



```python

adonis(macroinvertebrate_genus_count_wide~site*date, data=pcoa_macroinvert_bc_vectors)


```

### Beta-Diversity Continued!
Now use the same dataset and select another multivarte ordination test (NMDS or Correspondence Analysis), generate a plot with 95% confidence ellipses, and then use ANOSIM or Adonis to test the signifiance of groupings!

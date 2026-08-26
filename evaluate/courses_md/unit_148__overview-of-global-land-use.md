---
title: "Overview of Global Land Use, Food Security and the Environment"
unit_id: 148
course_id: 5
level: "Foundation"
slug: overview-of-global-land-use
is_course: 0
---

# Overview of Global Land Use, Food Security and the Environment

## Extracted resources (local files)

### Jupyter Notebook
*Source file:* `Analytical Framework for Analysis of Long Run Land Use Change.pptx`  ·  *type:* link

### Slide 1
Thomas Hertel

AGEC 596/528
 Global Change and the Challenge of Sustainably
 Feeding a Growing Planet
Framework for Analysis of Long Run Land Use Change

### Slide 2
Outline of the Lecture
Analytical framework for characterizing long-run supply and demand for land
Using the theoretical framework to predict impacts of a population shock on commodity prices and land use

### Slide 3
Global 
Food, Fiber & Fuel 
Production
Farm
land
Non Land 
Inputs
Exploring the Agriculture-Environment-Land Nexus

### Slide 4
Theoretical Framework (see supplementary reading)
Consider global agriculture as a single sector
produces all food, fiber and fuel from agriculture
employs land and non-land inputs; the prices of the latter are determined by exogenous (nonfarm) considerations in long run
Farmers minimize costs, entry/exit results in zero economic profits

Examine the long run equilibrium % change in commodity prices and agricultural land as a function of three exogenous drivers: 
demand growth, includes food, fiber, fuel: 
“trend” yield growth, alters derived demand for land: 
reductions in supply of agr land (e.g., urbanization, national parks) 

Note: this is a comparative static exercise: E.g., what is the change in land use between today and 2050
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?

### Slide 5
Global 
Food, Fiber & Fuel 
Production
Farm
land
Non Land 
Inputs
Population, income & energy prices
Demand 
Growth
Demand growth is fueled exogenously by population, income and bioenergy growth

### Slide 6
Characterizing Food Demand
Consider global agriculture as a single sector, satisfying all demands for food, fiber and fuel from agriculture; of which there are two key components:
Exogenous % shocks (e.g., population, biofuel mandates): 
Endogenous (price-sensitive) component: 
So the demand relationship, expressed in percentage change terms    is given by:  


Search for key equations for this in SIMPLE tabfile (also, see Lab 1 Discussion)
E_QPC #  Per Capita Commodity Demand  #
E_CONS # Regional Commodity Demand #
E_PCROP # Crop demand and supply balance #

### Slide 7
Food Demand Schedule
Price of
 Food
Quantity of 
Food
0
Food Demand Schedule
P*
Q*
Given price level P*, consumers purchase Q*  quantity of food
See E_QCONS and E_QPC in SIMPLE

### Slide 8
Endogenous demand response to an exogenous reduction in price
Market price falls to  P**
Consumers purchase more food: Q*
In lower case (% chng) notation:
0
P*
Q*
P
Q
P**
Q**

### Slide 9
Econometric evidence on long run food demand response to price
Consumers take time to adjust; how much would demand adjust to permanently higher prices?

International cross-section studies use ICP data – designed to compare  cost of living across countries

Demand elasticities (abs value at constant income, from Mohammed et al., 2011):
Range: 0.86 to 0.30 for sample of 144 countries in 2005
Low income avg = 0.74; high income avg = 0.43
Global avg in 2005 = 0.53 
This is just ONE of the three margins of economic response
In SIMPLE, EOP becomes smaller as incomes increase

### Slide 10
Exogenous shift in Food Demand: Assuming Fixed Price
P
Q
0
P*
Q*
If price were unchanged, then new consumption quantity is Q**
If population increases, overall demand for food increases for each price level (i.e. regional demand curve shifts). Captured by 

Effect of per capita income growth is also treated as shifts in demand (i.e. per capita demand curve) => magnitude is governed by the income elasticity of food demand
Q**

### Slide 11
Global 
Food, Fiber & Fuel 
Production
Farm
land
Non Land 
Inputs
Food Supply Depends on Land and Non-land Inputs

### Slide 12
Supply response tied to land:
Intensive margin: ability to coax more production from available land (yields rise)
Extensive margin: ability to increase land available for crops 
Both contribute to positive quantity response when price rises
In SIMPLE, we have 3 food sectors, crops, livestock and processed foods. The description above applies to crops sector only
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?
Food Supply is tied to Land
P
Q
Q
QS
P
QD

### Slide 13
Yield growth is divided into exogenous (trend) and endogenous components
Exogenous growth in crop yields:
the difference in growth rates of crop output and cropland
‘trend growth’ is assumed to be a function of past investments in R&D
seems unlikely that is it insensitive to price, but we allow for this, as it is the most common assumption in land use projections; lag time can be multiple decades
In SIMPLE, we can capture this by targeting crop yields via technical change variable: AOCROP
Endogenous yield response depends on the relative scarcity of cropland and the ensuing incentive to increase yields by using more inputs

In this simple model, nonland inputs are assumed to be in perfectly elastic supply (price is set by nonfarm sector), so for any experiment, the key thing is what happens to land rents

### Slide 14
It can take a long time to develop the technology
Source: Alston, Pardey and Ruttan (2008) and Alston et al. (2010)

### Slide 15
And adoption also can occur with a significant lag
Source:  Beddow (2011 forthcoming)

### Slide 16
Yield growth is divided into exogenous (trend) and endogenous components
Exogenous growth in crop yields:
the difference in growth rates of crop output and cropland
‘trend growth’ is assumed to be a function of past investments in R&D
seems unlikely that is it insensitive to price, but we allow for this, as it is the most common assumption in land use projections; lag time can be multiple decades

Endogenous yield response depends on the relative scarcity of cropland and the ensuing incentive to increase yields by using more nonland inputs

In the theoretical model, nonland inputs are assumed to be in perfectly elastic supply (price is set by nonfarm sector), so for any experiment, the key thing is what happens to land rents – this is not the case in the SIMPLE model

### Slide 17
Endogenous Yield Response to Changing Scarcity of Land
Endogenous yield response depends on the relative scarcity of land and the incentive to increase yields by using more inputs
If fertilizer is relatively cheap, apply more per ha. of  land in order to boost yields – ‘land sparing’ intensification
If cropland is relatively abundant and fertilizer is expensive, apply less non-land input per ha., yields fall – pushes output expansion to extensive margin
Changes in the relative scarcity of land can be measured via %Δ land rents relative to an index of all input prices 
     where: 
The potential for intensification captured by the elasticity of substitution in agricultural production:
     or ECROP in the SIMPLE model

### Slide 18
Contrasting substitution possibilities between land and non-land inputs used in crop production
Land inputs
Non-land inputs
0
Land inputs
Non-land inputs
0
The solid lines above represent the isoquants of crop production        . If            input substitution is possible. If           , no input substitution is possible
The optimal mix of land and non-land inputs is determined by the intersection of the relative input price line (i.e. broken line denoted P)
P
P

### Slide 19
Potential for endogenous intensification under two alternative technologies
Land inputs
Non-land inputs
0
Land inputs
Non-land inputs
0
If non-land inputs become relatively cheaper and:
There is input substitution            , ↓ land inputs and ↑ non-land inputs
Without input substitution            , no change in optimal mix of land and non-land inputs
P
P
P*
P*

### Slide 20
Historical evidence: 86% of output growth over 1961-2005 period was due to increased yields or cropping intensity

Econometric estimation should be straightforward; however, difficulty lies in disentangling technological change ‘time trend’ from price effects; time trend influenced by prices

Statistical evidence for           : US Maize most heavily studied crop: estimates of yield elasticity has fallen from 0.76 in post-WWII studies to 0.15 in most recent ones

Suggests that intensive margin may be much larger in developing world where sector is heterogeneous; less commercialized
Could also estimate intensification parameter         directly: Estimates are surprisingly large: Why is this? Many farmers suggest that they do not vary the amount of fertilizer applied/hectare of land; however, there is also a compositional effect
Evidence on yield response to price

### Slide 21
Derived Demand for Agricultural Land
Combining the exogenous and endogenous potential for yield growth, we can get the derived demand for land in ag production:


There is an interaction between the exogenous and endogenous components of yield growth. Consider the following:
No exogenous yield growth                     and no scope for               intensification        
a 50% rise in output, requires a 50% rise in productivity adjusted land input, no economies of scale at the industry level
This doesn’t mean they do not arise at the farm level, but their effect is washed out through entry/exit at the industry level
When land becomes scarce, relative to other inputs                                 yields will increase endogenously
In SIMPLE, see Equation E_QLANDg  
p_QLANDg(g) + p_AFLANDg(g)  =  p_QCROPg(g) - p_AOCROPg(g)        - ECROP(g) * [p_PLANDg(g) - p_AFLANDg(g) - p_PCROP - p_AOCROPg(g)];

### Slide 22
As with other factors, changes in land supply depend on both exogenous and endogenous elements

Urbanization is largely driven by forces exogenous to global agriculture. Encroachment of urban areas into cropland represented by a backward shift in supply of land:

Slope of land supply schedule determined by elasticity of land supply:
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?
Supply of Agricultural Land
Land Rents
Agricultural Land
0
New supply curve due to urbanization
Original land supply curve

### Slide 23
Equation E_PLANDg         # determines the endogenous price of land in crop production #    (all,g,REG_GEO)    p_QLANDg(g) = 
         ELANDg(g) * p_PLANDg(g)          -  p_QURBLANDg(g)          -  p_QENVLANDg(g);
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?
Supply of Agricultural Land
Land Rents
Agricultural Land
0
New supply curve due to urbanization
Original land supply curve

### Slide 24
Empirical evidence: 
Area response to Rents (       )
Few long  run studies; Lubowski is most credible – based on land cover change at NRI data points over two decades

Figure shows simulated response to yields over very long run; 20 year cropland response to crop land rents is about 0.15; (larger elasticity wrt commodity price) 

In our theoretical framework:
As time horizon lengthens, area response increases

### Slide 25
Outline of the Talk
Analytical framework: characterizing LR supply and demand for land
Using the framework to predict impacts of a population shock on commodity prices and land use
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?

### Slide 26
What will be the impact of population growth on global commodity prices and land use?
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?
Extracted from Leslie Roberts, “9 Billion?”, Science vol. 333, 29 July, 2011.

### Slide 27
Implications for Equilibrium in the Market for Global Crops
P
Q
0
P**
Q*
Q**
Supply Curve
P*

### Slide 28
Equilibrium change in land use as a function of the population shock to demand in the theoretical model


Land use depends on relative, not absolute, size of intensive and extensive margins: large intensive response will not limit land use change if extensive margin is also large
Larger demand- and intensive-supply elasticities serve to diminish demands on biophysical system
In the special case where the intensive supply and demand elasticities are zero, long run land use change grows at the population growth rate (assuming no other shocks to the system)
If demand and yields are responsive to price, this approach will exaggerate predicted change in land use
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?
Impact of population growth on agricultural land use

### Slide 29
Now two sets of shocks:
demand growth, includes food, fiber, fuel
exogenous yield growth, alters derived demand for land
Same three margins of economic response:
demand response
intensive margin of supply response
extensive margin of supply response
Together, these determine the resulting land use and price change:



Note that, if yield growth is rapid enough, prices will fall and land use is smaller; this is what happened over latter half of the 20th century
Adding exogenous shocks to yields and agricultural land supply

## Fetched resources (external URLs)

### Book Chapter: Overview of Global Land Use, Food Security and the Environment (link)
*URL:* https://link.springer.com/chapter/10.1007/978-3-319-22662-0_1

# Overview of Global Land Use, Food Security and the Environment | Springer Nature Link

Overview of Global Land Use, Food Security and the Environment | Springer Nature Link
Skip to main content
Advertisement
Overview of Global Land Use, Food Security and the Environment
Chapter
pp 1–12
Cite this chapter
Save chapter
View saved research
Global Change and the Challenges of Sustainably Feeding a Growing Planet
Abstract
Feeding the world’s population while ensuring the environmental sustainability is one of the world’s ‘grand challenges’. As we look ahead to the middle of this century, will the world’s agricultural resource base be up to the task of meeting the diverse demands being placed on it by growing population, rising incomes, growing biofuel production and rising demand for land-based environmental services? In this chapter we lay out a framework for thinking about the long run sustainability of the world’s food and environmental systems. This model brings together factors from the demand side (population, income, biofuels) as well as the supply side (technological progress, climate change, competing land uses) in order to predict the equilibrium use of land in agriculture over the long run. Absent economic responses, this boils down to a food race between demand growth and improving yields. By bringing the responsiveness of demand and supply to scarcity into the picture, we find that the resource requirements due to growing demands are muted. This framework also gives us a vehicle for determining how much of the adjustment to potential scarcity will come through reduced consumption and how much from increased supplies. The former has important consequences for nutrition, while the latter can have serious environmental impacts. This basic framework, which is fully developed in Appendix B, forms the basis for the economic analysis throughout this book.
This chapter draws heavily on Hertel’s Presidential Address to the Agricultural and Applied Economics Association (Hertel,
2011
).
This is a preview of subscription content,
log in via an institution
to check access.
Access this chapter
Log in via an institution
Subscribe and save
Springer+
from $39.99 /Month
Starting from 10 chapters or articles per month
Access and download chapters and articles from more than 300k books and 2,500 journals
Cancel anytime
View plans
Buy Now
Chapter
USD 29.95
Price excludes VAT (USA)
Available as PDF
Read on any device
Instant download
Own it forever
Buy Chapter
eBook
USD 39.99
Price excludes VAT (USA)
Available as EPUB and PDF
Read on any device
Instant download
Own it forever
Buy eBook
Softcover Book
USD 54.99
Price excludes VAT (USA)
Compact, lightweight edition
Free shipping worldwide -
view details
Buy Softcover Book
Hardcover Book
USD 54.99
Price excludes VAT (USA)
Durable hardcover edition
Free shipping worldwide -
view details
Buy Hardcover Book
Tax calculation will be finalised at checkout
Purchases are for personal use only
Institutional subscriptions
Similar content being viewed by others
Global Food Systems—The Challenges and Trends in the Anthropocene Epoch
Chapter
© 2026
Climate Change Resilient Crops to Combat Food and Nutrition Insecurity in Marginal Lands
Chapter
© 2024
Loss of Agro-Biodiversity and Productivity Due to Climate Change in Continent Asia: A Review
Chapter
© 2020
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Biophysical Economics
Energy Supply and Demand
Food Security
Resource and Environmental Economics
Sustainable Growth
Sustainability
References
Ahmed, S. A., Diffenbaugh, N. S., & Hertel, T. W. (2009). Climate volatility deepens poverty vulnerability in developing countries.
Environmental Research Letters, 4
(3), 034004.
http://doi.org/10.1088/1748-9326/4/3/034004
.
Article
Google Scholar
Alexandratos, N. (Ed.). (1995).
World agriculture: Towards 2010
. Rome, Italy: Food and Agriculture Organization of the United Nations and Wiley. Retrieved from
http://www.fao.org/docrep/V4200E/V4200E00.htm
.
Google Scholar
Alexandratos, N., & Bruinsma, J. (2012).
World agriculture towards 2030/2050: The 2012 revision
(Working Paper No. 12-03). Rome, Itally: Food and Agriculture Organisation of the United Nations.
Google Scholar
Alston, J. M., Pardey, P. G., & Ruttan, V. W. (2008).
Research lags revisited: Concepts and evidence from U.S. Agriculture
(Staff Paper No. 50091). University of Minnesota, Department of Applied Economics. Retrieved from
http://ideas.repec.org/p/ags/umaesp/50091.html
.
Baldos, U. L., & Hertel, T. (2014). Bursting the bubble: A long run perspective on crop commodity prices. Retrieved from
http://www.gtap.agecon.purdue.edu/resources/res_display.asp?RecordID=4574
.
Balmford, A., Green, R. E., & Scharlemann, J. P. W. (2005). Sparing land for nature: Exploring the potential impact of changes in agricultural yield on the area needed for crop production.
Global Change Biology, 11
(10), 1594–1605.
http://doi.org/10.1111/j.1365-2486.2005.001035.x
.
Article
Google Scholar
Barona, E., Ramankutty, N., Hyman, G., & Coomes, O. T. (2010). The role of pasture and soybean in deforestation of the Brazilian Amazon.
Environmental Research Letters, 5
(2), 024002.
http://doi.org/10.1088/1748-9326/5/2/024002
.
Article
Google Scholar
Baumert, K. A., Herzog, T., & Pershing, J. (2005).
Navigating the numbers: Greenhouse gas data and international climate policy
(p. 122). Washington, DC: World Resources Institute. Retrieved from
http://www.wri.org/publication/navigating-the-numbers
.
Google Scholar
Bruinsma, J. (2009). The resource outlook to 2050. By how much do land, water use and crop yields need to increase by 2050? In
FAO Expert meeting on How to Feed the World in 2050
. Rome: Food and Agriculture Organisation of the UN.
Google Scholar
Buringh, P. (1985). The land resource for agriculture.
Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences, 310
(1144), 151–159.
Article
CAS
Google Scholar
Cassman, K. G., Grassini, P., & van Wart, J. (2010). Crop yield potential, yield trends, and global food security in a changing climate. In D. Hillel & C. Rosenzweig (Eds.),
Handbook of climate change and agroecosystems: Impacts, adaptation, and mitigation
(Vol. 1, pp. 37–51). Hackensack, NJ: World Scientific.
Chapter
Google Scholar
Deininger, K. W., & Byerlee, D. (2010).
Rising global interest in farmland: Can it yield sustainable and equitable benefits?
Washington, DC: World Bank.
Google Scholar
Energy Information Agency. (2010).
Annual energy outlook 2010
(Annual Energy Outlook No. DOE/EIA-0383(2010)). Washington, DC: US Department of Energy.
Google Scholar
Foley, J. A., DeFries, R., Asner, G. P., Barford, C., Bonan, G., Carpenter, S. R., … Snyder, P. K. (2005). Global consequences of land use.
Science, 309
(5734), 570–574.
http://doi.org/10.1126/science.1111772
.
Google Scholar
Food and Agriculture Organization of the UN Media Centre. (2013, April 12). Feeding nine billion in 2050. Retrieved May 23, 2013, from
http://www.fao.org/news/story/en/item/174172/icode/
.
Fuglie, K. O. (2012). Productivity growth and technology capital in the global agricultural economy. In K. O. Fuglie, S. L. Wang, & V. E. Ball (Eds.),
Productivity growth in agriculture: An international perspective
(pp. 335–368). Cambridge, MA: CAB.
Chapter
Google Scholar
Gibbs, H. K., Ruesch, A. S., Achard, F., Clayton, M. K., Holmgren, P., Ramankutty, N., & Foley, J. A. (2010). Tropical forests were the primary sources of new agricultural land in the 1980s and 1990s.
Proceedings of the National Academy of Sciences of the United States of America, 107
(38), 16732–16737.
http://doi.org/10.1073/pnas.0910275107
.
Google Scholar
Golub, A. A., Henderson, B. B., Hertel, T. W., Gerber, P. J., Rose, S. K., & Sohngen, B. (2013). Global climate policy impacts on livestock, land use, livelihoods, and food security.
Proceedings of the National Academy of Sciences of the United States of America, 110
(52), 20894–20899.
http://doi.org/10.1073/pnas.1108772109
.
Article
CAS
Google Scholar
Golub, A., Hertel, T. W., Lee, H.-L., Rose, S., & Sohngen, B. (2009). The opportunity cost of land use and the global potential for greenhouse gas mitigation in agriculture and forestry.
Resource and Energy Economics, 31
(4), 299–319.
http://doi.org/10.1016/j.reseneeco.2009.04.007
.
Article
Google Scholar
Green, R. E., Cornell, S. J., Scharlemann, J. P. W., & Balmford, A. (2005). Farming and the fate of wild nature.
Science, 307
(5709), 550–555.
http://doi.org/10.1126/science.1106049
.
Article
CAS
Google Scholar
Hayami, Y., & Ruttan, V. W. (1985).
Agricultural development: An international perspective
. Baltimore, MD: Johns Hopkins University Press.
Google Scholar
Hertel, T. W. (2011). The global supply and demand for agricultural land in 2050: A perfect storm in the making?
American Journal of Agricultural Economics, 93
(2), 259–275.
http://doi.org/10.1093/ajae/aaq189
.
Google Scholar
Keeney, R., & Hertel, T. W. (2008).
Yield response to prices: Implications for policy modeling
(Working Paper No. 08-13). Purdue University.
Google Scholar
Lambin, E. F. (2012). Global land availability: Malthus versus Ricardo.
Global Food Security, 1
(2), 83–87.
http://doi.org/10.1016/j.gfs.2012.11.002
.
Article
Google Scholar
Lepers, E., Lambin, E. F., Janetos, A. C., DeFries, R. S., Achard, F., Ramankutty, N., & Scholes, R. J. (2005). A synthesis of information on rapid land-cover change for the period 1981–2000.
BioScience, 55
(2), 115–124.
http://doi.org/10.1641/0006-3568(2005)055[0115:ASOIOR]2.0.CO;2
.
Google Scholar
Lubowski, R. (2002).
Determinants of land use transitions in the United States: Econometrics analysis of changes among the major land-use categories
. Cambridge, MA: Harvard University.
Google Scholar
Malthus, T. R. (1888).
An essay on the principle of population
(9th ed.). London, UK: Ballantyne Press.
Google Scholar
McKinsey & Co. (2009).
Charting our water future: Economic frameworks to inform decision-making
. 2030 Water Resources Group: McKinsey & Co.
Google Scholar
Muhammad, A., Seale, J. L., Jr., Meade, B., & Regmi, A. (2011).
International evidence on food consumption patterns: An update using 2005 International Comparison Program Data
(Technical Bulletin No. TB-1929) (p. 59). Washington, DC: Economic Research Service, US Department of Agriculture. Retrieved from
http://www.ers.usda.gov/Publications/TB1929/
.
OECD/FAO. (2013).
OECD-FAO agricultural outlook 2013-2022
(p. 326). OECD/FAO. Retrieved from
http://dx.doi.org/10.1787/agr_outlook-2013-en
.
Paarlberg, R. L. (2008).
Starved for science: How biotechnology is being kept out of Africa
. Cambridge, MA: Harvard University Press.
Book
Google Scholar
Ramankutty, N. (2010). Agriculture and forests: Recent trends, future prospects. In T. Graedel & E. van der Voet (Eds.),
Linkages of sustainability
(Vol. 4, pp. 11–31). Cambridge, MA: MIT Press.
Google Scholar
Ramankutty, N., Foley, J. A., & Olejniczak, N. J. (2002). People on the land: Changes in global population and croplands during the 20th century.
AMBIO: A Journal of the Human Environment, 31
(3), 251–257.
Article
Google Scholar
Ramankutty, N., Graumlich, L., Achard, F., Alves, D., Chhabra, A., DeFries, R. S., … Turner, B. L. (2006). Global land-cover change: Recent progress, remaining challenges. In
Land use and land cover change
(pp. 9–39). The Netherlands: Springer. Retrieved from
http://dx.doi.org/10.1007/3-540-32202-7_2
.
Reilly, J., Paltsev, S., Felzer, B., Wang, X., Kicklighter, D., Melillo, J., … Wang, C. (2007). Global economic effects of changes in crops, pasture, and forests due to changing climate, carbon dioxide, and ozone.
Energy Policy, 35
(11), 5370–5383.
Google Scholar
Steinbuks, J., & Hertel, T. W. (2014).
Confronting the food-energy-environment trilemma: Global land use in the long run
(No. WPS6928) (pp. 1–87). The World Bank. Retrieved from
http://documents.worldbank.org/curated/en/2014/06/19696268/confronting-food-energy-environment-trilemma-global-land-use-long-run
.
Vermeulen, S. J., Campbell, B. M., & Ingram, J. S. I. (2012). Climate change and food systems.
Annual Review of Environment and Resources, 37
(1), 195–222.
http://doi.org/10.1146/annurev-environ-020411-130608
.
Article
Google Scholar
Vitousek, P. M., Naylor, R., Crews, T., David, M. B., Drinkwater, L. E., Holland, E., … Zhang, F. S. (2009). Nutrient imbalances in agricultural development.
Science, 324
(5934), 1519–1520.
http://doi.org/10.1126/science.1170261
.
Google Scholar
World Bank. (2008).
Agriculture for development
(pp. 1–386).
Google Scholar
World Bank. (2013, April 15). Food crisis. Retrieved May 23, 2013, from
http://www.worldbank.org/foodcrisis/bankinitiatives.htm
.
Download references
Author information
Authors and Affiliations
Department of Agricultural Economics, Purdue University, West Lafayette, IN, USA
Thomas W. Hertel & Uris Lantz C. Baldos
Authors
Thomas W. Hertel
View author publications
Search author on:
PubMed
Google Scholar
Uris Lantz C. Baldos
View author publications
Search author on:
PubMed
Google Scholar
Rights and permissions
Reprints and permissions
Copyright information
© 2016 Springer International Publishing Switzerland
About this chapter
Cite this chapter
Hertel, T.W., Baldos, U.L.C. (2016).  Overview of Global Land Use, Food Security and the Environment.

                     In:  Global Change and the Challenges of Sustainably Feeding a Growing Planet. Springer, Cham. https://doi.org/10.1007/978-3-319-22662-0_1
Download citation
.RIS
.ENW
.BIB
DOI
:
https://doi.org/10.1007/978-3-319-22662-0_1
Publisher Name
:
Springer, Cham
Print ISBN
:
978-3-319-22661-3
Online ISBN
:
978-3-319-22662-0
eBook Packages
:
Earth and Environmental Science
Earth and Environmental Science (R0)
Share this chapter
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy shareable link to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Keywords
Agricultural land use change
Intensive margin of supply
Extensive margin of supply
Drivers of global cropland expansion
Economic analysis of land use change
Publish with us
Policies and ethics
Access this chapter
Log in via an institution
Subscribe and save
Springer+
from $39.99 /Month
Starting from 10 chapters or articles per month
Access and download chapters and articles from more than 300k books and 2,500 journals
Cancel anytime
View plans
Buy Now
Chapter
USD 29.95
Price excludes VAT (USA)
Available as PDF
Read on any device
Instant download
Own it forever
Buy Chapter
eBook
USD 39.99
Price excludes VAT (USA)
Available as EPUB and PDF
Read on any device
Instant download
Own it forever
Buy eBook
Softcover Book
USD 54.99
Price excludes VAT (USA)
Compact, lightweight edition
Free shipping worldwide -
view details
Buy Softcover Book
Hardcover Book
USD 54.99
Price excludes VAT (USA)
Durable hardcover edition
Free shipping worldwide -
view details
Buy Hardcover Book
Tax calculation will be finalised at checkout
Purchases are for personal use only
Institutional subscriptions

### GEMPACK software (link)
*URL:* https://www.copsmodels.com/gplapsoft.htm

# Installing GEMPACK on your laptop prior to a training course

Installing GEMPACK on your laptop prior to a training course
Installing GEMPACK on your laptop prior to a training course
GEMPACK-oriented training courses often require that you bring and use your own laptop computer. Most Windows laptops will be adequate (for
   specific requirements see
here
). To do the course exercises, you'll need to install GEMPACK on your laptop. Usually,
   this is rather easy. However, we ask that you install the software
prior to the course
, for two reasons:
Any software problems will surface during the first course sessions -- when the instructors are busiest. Installing beforehand allows problems
   to be identified and addressed before the course starts.
To install the software, you will need "Administrator" access rights. If your laptop belongs to, or was configured by, your organization's IT
   section, you may only have limited or "Standard User" access rights. In that case an Administrator password may be needed to install GEMPACK. This
   could mean that someone from your organization's IT section has to be present during the install. In such a case, installation during the course
   might be impossible. Moreover, particular corporate IT policies occasionally cause problems with GEMPACK. You would need to work with your IT
   section to resolve such problems.
What if my laptop already has GEMPACK on it?
The course requires that you have GEMPACK Release 11.0 or later. To see which version you have, use the menu command
Help...GEMPACK
   licence
from TABmate or ViewHAR. If you have Release 10 or earlier, you must install Release 11. The instruction document mentioned below
   explains how you can rename your existing GEMPACK folder so that you can later go back to the old version, if necessary.
Downloading and Installing the Executable-Image Version of GEMPACK
First, download, print out, and
read
quickinst.pdf
. It contains simplified install instructions
   especially designed for training course use.
Next, download the Trial Edition of the
Limited Executable-Image Version of GEMPACK
from
this page
. It
   mentions a longer install document, GPInstall.pdf, but you should follow the shorter QuickInst instructions. Section 3 of the QuickInst
   instructions explains how to check that your installation is working properly by running a model simulation:
it is important that you complete
   this section
.
The Trial Edition includes all the main GEMPACK programs and can carry out a full range of modelling tasks. There is a model size limitation --
   but this will not cause problems during the course. The Trial Edition comes with a temporary licence lasting 6 months from the download date --
   long enough to complete the course. Often course participants will receive a
longer-lasting licence during the course
.
Other course software
For some courses, you may also need to pre-install other software, such as, for example, the RunDynam program for running dynamic simulations, or
   the RunGTAP program which solves the GTAP model. You will receive specific instructions if you need to install other programs. In any case, you
   should install GEMPACK
first
: the other programs may require that you already have GEMPACK installed.
Participants in the
Practical GE
course held in Melbourne and elsewhere are required to download the
MINIMAL free training software
, and to complete the exercises supplied with it.
Other course files
At the beginning of the course you will be supplied with various other files that are needed for the course exercises.
Course CD
During most courses participants are given a course CD (or USB key) containing: software required for the course; files needed for course
   exercises; and various supplementary material. Such CDs are mainly intended for use
after
the course. You should install the necessary
   software
before
the course.
Upgrading the temporary licence
The trial edition of the
Limited Executable-Image Version of GEMPACK
comes with a temporary licence lasting 6 months from the
   download date -- long enough to complete the training course. Usually course participants will be entitled to a better licence. Specific details
   will vary according to the course. For example:
Often course participants will receive (either beforehand by email, or on arrival at the course) a course-specific licence lasting 12 months
   from the start of the course.
See also
Laptop requirements
Executable-Image Version of GEMPACK
Training course page

---
title: "HANDS-ON LAB assignment"
unit_id: 34
course_id: 1
level: "Developer"
slug: hands-on-lab-assignment
is_course: 0
---

# HANDS-ON LAB assignment

**Description:** Step-by-step guidance on hands-on labs and analysis.

## Extracted resources (local files)

### Replicate and discuss GEC paper
*Source file:* `GEC Lab Assignment - African Green Revolution.doc`  ·  *type:* file

Hands-on Lab:
Food and Environmental Security in a Globalizing Economy

Prepared by Thomas Hertel and Uris Baldos 

For use in the SIMPLE-G Short Course

Purdue University

September 17, 2019

 SHAPE  \* MERGEFORMAT 

Up to this point in the course, we have tacitly assumed that there are no barriers to international trade. In fact, we have imposed the ‘law of one price’, which means that anyone, anywhere in the world can access the world markets, selling or buying at this unique world price. Even the most ardent international trade economist doesn’t believe this to be true for any given merchandise commodity. However, for purposes of long run analysis of commodity markets, this ‘bathtub’ model of global trade is often used as a benchmark. Suppliers ‘dump’ their output into the global marketplace and consumers draw their requirements from this bathtub without regard to the source of the commodity. If there is a shortfall in supply, for example due to bad weather in one part of the country, price will rise to equilibrate demand and supply in a new equilibrium in this frictionless marketplace. 

In practice there is a great deal of friction in agricultural commodity markets. The price of rice, for example, many vary widely across countries and even within countries. These differences can arise due to policy interventions (e.g., tariffs, consumer subsidies) or due to infrastructure and differing access to markets. The price will tend to be lower in regions where a surplus of rice is produced and higher in urban areas where transport and logistics result in higher costs. In short, we live in a world of segmented markets. In this assignment, you will use the segmented markets version of the model along with the integrated markets version which you have been using in the earlier lab assignments. The core reference for this assignment is the following paper, is also discussed in the lecture on globalization:

Hertel, T.W. and U.L.C. Baldos. (2016) “Attaining Food and Environmental Security in an Era of Globalization”, Global Environmental Change, 41:195-205.

This paper turns things around, and starts with the segmented markets structure, which is a better representation of historical agricultural trade. It then introduces an integrated world market structure as a counterfactual market environment – perhaps indicative of a future in which world agriculture is far more globalized due to the emergence of global supply chains connecting producers around the world with consumers.

 SHAPE  \* MERGEFORMAT 

The basic idea in the segmented markets model is that not all consumers have access to goods in the global markets and not all producers have the opportunity to sell into the world market. If we make some assumptions about the distribution of consumers and producers across space/market access, and aggregate to the market level, then the relationship between relative domestic and international prices and national market share of the domestically produced good (and by implication, that of the international good) is well-described via a constant elasticity of substitution function, such as used elsewhere in the SIMPLE model. When market access is very good for most of the population, then the implied elasticity of substitution is large, and there can be very little deviation of local and international prices. When market access is very heterogeneous, with many households having little or no access to world markets, then the implied elasticity of substitution is small. The following parameters must be defined to accommodate this theory:

Coefficient (parameter)       (all,r,REG)                                                ESUBr(r)      # substitution elasticity between local and global crops #;       Read ESUBr   from file LANDPARM header "ESUB";  Coefficient (parameter)       (all,r,REG)                                                ETRANSr(r)      # transformation elasticity between local and global crops #;       Read ETRANSr   from file LANDPARM header "ETRA";

And they appear on the consumption equations as follows (separate equations for each consumption category):

Equation E_QDCROPr      # derived demand for local crops for direct consumption #     (all,r,REG)      p_QDCROPr(r,"Crops","local") =           p_QCONS("Crops",r) - ESUBr(r) * [p_PCROP_loc(r) - p_P("Crops",r)] ;     Equation E_QCONS_CRP_GLB     # derived demand for global crops for direct consumption #     (all,r,REG)      p_QDCROPr(r,"Crops","global") =           p_QCONS("Crops",r) - ESUBr(r) * [p_PCROPW - p_P("Crops",r)] ;       and on the production side:

Equation E_QSCROP_LOC      # supply of crops in the local market #     (all,r,REG)         p_QSCROPr(r,"local") = p_QCROP(r)                  + ETRANSr(r) * [p_PCROP_loc(r) - p_PCROP(r)] ;     Equation E_QSCROP_GLB     # supply of crops in the global market #     (all,r,REG)           p_QSCROPr(r,"global") = p_QCROP(r)                   + ETRANSr(r) * [p_PCROPW - p_PCROP(r)] ;   

As you see we have new variables:
local prices (PCROP_loc(r)), 
world price (PCROPW), 
supply to local market (QSCROPr(r,"local")), 
supply to global market (QSCROPr(r,"global")), 
demand from local market (QDCROPr(r,"Crops","local")), and 
demand from global market (QDCROPr(r,"Crops","global")). 

In this framework, an additional key factor is the current degree of international market access. When this is small, the impact of a world price change on the domestic market will be smaller than when it is large. The following figure (taken from the GEC paper) reports the share of regional crop supply and demand which is met from global markets. You can see that this is particularly small for Sub-Saharan Africa, and large for the EU. All else constant, this means that the EU is much more closely integrated into world markets than is the SSA region. So a change in world price is more likely to be felt in the EU. In the case of Japan/Korea, producers are relatively insulated from world markets, while consumers are more exposed to world price changes, as can be seen from the subsequent table, reporting transmission elasticities from the international to domestic markets in each region.
Figure 1. Share of international market in regional crop supply (gross export sales/total sales) and in regional crop demand (gross import purchases/total crop purchases)


Table 1.Price Transmission Elasticity
Region
Eastern Europe
0.287
North Africa
0.356
Sub Saharan Africa
0.189
South America
0.336
Australia+New Zealand
0.516
European Union
0.635
South Asia
0.184
Central America + Caribbean
0.498
South Africa
0.465
South East Asia
0.491
Canada+United States
0.494
China
0.165
Middle East
0.413
Japan+Korea
0.636
Central Asia
0.338





In this lab, you will explore the implications of market segmentation for impacts of an ‘African Green Revolution’ arising from accelerated investments in agricultural R&D in Sub Saharan Africa. In the terminology of SIMPLE, this is a ‘shock’ to crop productivity in the SSA region. The timing, and impact of these investments is discussed in more detail in the following PNAS paper:  

Hertel, T., W., N. Ramankutty and U.L.C. Baldos, (2014) “Global market integration increases likelihood that a future African Green Revolution could increase crop land use and CO2 emissions”, Proceedings of the National Academy of Sciences 111(38): 13799–13804, doi: 10.1073/pnas.1403543111.

However, unlike that paper, the policy simulations will be performed on the updated, 2050 economies resulting from two alternative baselines: one resulting from projections to 2050 using the segmented markets model and one resulting from the integrated markets model. This follows the experimental design employed in the GEC paper referenced above and simplifies discussion and analysis in a lab setting. The counterfactual experiments will be undertaken using a 2050 baseline economy, as established via projections of either the segmented or the integrated economy, so the two simulations start in different places. However, the percentage changes remain relevant points of comparison across the two models.

A more sophisticated approach would involve projecting each model (both segmented and integrated market models) forward to 2050, first under the baseline assumption and then under the green revolution scenario, and differencing the results as done in the Hertel, Ramankutty & Baldos (2014) PNAS paper. This requires more data manipulations but can be readily undertaken on your own.

We will begin the lab by revisiting the baseline projects to 2050 undertaken in the GEC paper, then shift to the two alternative 2050 data bases to analyze the impacts of the African Green Revolution.
 

 SHAPE  \* MERGEFORMAT 

Start by running the two baseline experiments which simulate the evolution of the global economy over the period: 2006-2050. You will need to operate out of two different sub-directories – one corresponding to the Segmented Markets version of the model and one for the Integrated Markets version. In each case, you will need to start by loading the correct data base, namely LANDDATA-2006-SEG.HAR or LANDDATA-2006-INT.HAR. (The parameters and sets are invariant to the time period considered.) Then you will need to load the projections closure (Projections.cls), and the baseline shocks (Baseline 2006-2050.shf). Don’t forget to save your output file under a meaningful name. We suggest: baseline 2006-2050-SEG.sl4 and baseline 2006-2050-INT.sl4, respectively. Before solving the model, please choose an appropriate solution method. To obtain comparability with the GEC paper, we suggest: Gragg 2-4-6 with 2 subintervals and automatic accuracy for BOTH data and solution at 4 figures with 95% accuracy.

Once you have run the model, an easy way to view the results is side-by-side in VIEWHAR. To do so, first open baseline 2006-2050-SEG.sl4 in VIEWHAR and then go to file/open and open 2006-2050-INT.sl4 from the integrated markets output subdirectory. Fill in the following tables and then address the associated discussion questions. 


Table 1. Global and regional impacts of the 2006-2050 baseline under two market structures

Baseline Scenario
Global Impacts (in %)

Crop Price
Nonfarm Undernutrition
Cropland
Terrestrial Carbon Emissions

Segmented
Integrated
Segmented
Integrated
Segmented
Integrated
Segmented
Integrated





















Regional Impacts: Sub Saharan Africa (in %)

Crop Price
Nonfarm Undernutrition
Cropland
Terrestrial Carbon Emissions

Segmented
Integrated
Segmented
Integrated
Segmented
Integrated
Segmented
Integrated

SSA



















China


















Discussion questions: Draw on these results, as well as what you have learned thus far in the course, in order to address the following questions. 

Why do you think the global price changes are nearly the same in the two projections experiments?
Please explain the differences in the regional crop price outcomes. (Hint: you might want to refer back to the exogenous projections of regional growth in productivity – AOCROP, and the regional growth in demand – POP and INC_PC.)
Use your answer to #2 to explain the difference in undernutrition outcomes in SSA under segmented and integrated markets.
Why is the change in cropland in the SSA region so different under the two scenarios.
(Extra credit: While the regional percentage changes in terrestrial carbon emissions scale with cropland area change, the global emissions do not. Why is this?)


 SHAPE  \* MERGEFORMAT 


Now run the two Green Revolution experiments starting from the 2050 baseline established using projections of the segmented and integrated markets models, respectively. This will involve changing your base data, your closure and your shocks as follows (do this both for the INT and SEG models):

LANDDATA-2050-INT.har	: the updated data base for 2050
50_GR_SSA.cls		: this is the closure file for the GR shock
50_GR_SSA.shk	: this shocks agricultural productivity in SSA and South Africa in 2050 based on advances observed during a comparable period of the Asian Green Revolution

Be sure to save your output file under an appropriate name, such as 50_GR_SSA_INT. Fill in the results in table 2. 
Table 2. Global and regional impacts of an African Green Revolution in 2050

Policy Scenario
Global Impacts (in %)

Crop Price
Nonfarm Undernutrition
Cropland
Terrestrial Carbon Emissions

Segmented
Integrated
Segmented
Integrated
Segmented
Integrated
Segmented
Integrated
African Green Revolution



















Regional Impacts: Sub Saharan Africa (in %)

Crop Price
Nonfarm Undernutrition
Cropland
Terrestrial Carbon Emissions

Segmented
Integrated
Segmented
Integrated
Segmented
Integrated
Segmented
Integrated
African Green Revolution


























Discussion questions: Draw on these results, as well as what you have learned throughout the course, in order to address the following questions. 

Discuss the impacts of the African Green Revolution on global crop price as well as the price in the SSA region. 
Discuss the impacts of the African Green Revolution on undernutrition and terrestrial carbon emissions under segmented markets. 
Why do the results under integrated markets differ so radically? 









 Introduction


A. Overview of the segmented markets model structure and TAB file

C. Running the baseline experiments 

D. Impact of an African Green Revolution

### Understanding the SIMPLE-G-US-CS at the level of individual grid cells
*Source file:* `Hands-On Lab with CS model-final.docx`  ·  *type:* file

Hands-on Lab:
Understanding the SIMPLE-G-US-CS at the level of individual grid cells
Prepared by Thomas Hertel and Jing Liu 
For use in the SIMPLE-G Short Course
Purdue University
September 17, 2019
Key References:
Core Model:
Baldos, Uris Lantz C., Iman Haqiqi, Thomas W. Hertel, Mark Horridge, and Jing Liu. 2019. “SIMPLE-G: A Multiscale Framework for Integration of Economic and Biophysical Determinants of Sustainability.” In Preparation for Environmental Modelling & Software. 
Application: 
Liu, J., Hertel, T.W., Bowling, L., Jame, S., Kucharik, C. and Ramankutty, N., 2018. Evaluating Alternative Options for Managing Nitrogen Losses from Corn Production. Purdue Policy Research Institute (PPRI) Policy Briefs, 4(1), p.9. (This will be more fully developed for journal submission.)
The purpose of this lab is to introduce you to the gridded version of the SIMPLE model, SIMPLE-G, but to do it in a way that delivers a deeper understanding of the results that is offered by simply viewing maps of the model outputs. This is, of course, the challenge with gridded modeling: How do you develop a rigorous analysis when tens of thousands of grid cells are in play? The approach we will use here takes advantage of the ‘hinge’ separating our global model, SIMPLE, from the gridded US component. By 
fixing the national crop price we can turn off the part of SIMPLE that we rely on for generating national and international equilibria in crops. Commodity demand will also be ignored in this analysis, as we will be predetermining any price changes exogenously. Furthermore, given our focus on nitrogen use, we will also fix the national price of nitrogen to allow us to control the price paid by farmers via a leaching tax.
Throughout the course of this lab we will alternate between a ‘mini’ version of SIMPLE-G-CS and the full scale version. The mini model is obtained by excerpting the block of code relating to grid cell activities from the full SIMPLE-G model. Since the mini model eliminates any interaction across grid cells (which only happens through market mechanisms in SIMPLE-G), we are free to pick any subset of the grid cells. In this case, we have selected ten grid cells drawn from across the Corn Belt. By examining how these heterogeneous grid cells respond to an exogenous crop price increase, or a nitrogen leaching tax, we can enrich our understanding of what drives the heterogenous outcomes when we solve the model with tens of thousands of grid cells on the GeoHub. Of course, since the mini model we are not modeling all the grid cells in the US in this lab, we cannot speak to potential changes in market conditions and prices. The other great advantage of the mini model is that it is easy to modify and experiment on. This may make is useful in some of the project extensions undertaken later in the week.
The ‘corn-soy’ version of SIMPLE-G zooms in on the United States (US) and aggregates corn and soy production (CS) to avoid having to model the supply and demand side interactions between these crops. The fact that these commodity prices move in tandem is an economic justification for this aggregation. By allowing for grid cell/irrigation differentiation of production technologies, we also capture the biophysical differences arising from continuous and rotation corn-soy farming. The drawback is that we don’t allow for changing crop rotation. This is a major limitation of this model, although there are many others! That is why it is SIMPLE!
As you will learn in the lecture on the ‘nested’ crop production functions in SIMPLE-G, there are more than two inputs identified in the gridded model. However, for purposes of this lab we will focus on the ‘top nest’ of the SIMPLE-G-US-CS ‘production tree’ shown below. This means, we will focus on what happens to nitrogen fertilizer use, on the one hand, and ‘augmented land’ on the other. Augmented land includes not only the crop land, but also, in the case of irrigated agriculture, any additional irrigation infrastructure – as well as the associated irrigation water input. It also includes all other, non-nitrogen ‘non-land’ inputs. So, when we talk about the intensive margin of supply in this lab, we will be referring to increased use of nitrogen fertilizer per unit of augmented land and when we refer the extensive margin of supply, we will be referring to increased use of the augmented land input. In keeping with the analytical model (see Box 1 at the end of this document), we will assume that the market price of fertilizer is unchanging, while the augmented land input is inelastically supplied. (I.e., greater demand for this input bids up its price.) Thus, it is the augmented land input that constrains crop supply in this mini model.
Figure 1. The SIMPLE-G Production Tree
Key equations from the mini model are as follows: 
!Demand for nitrogen fertilizer input !
E_QNITROgl    (all,g,GRID)(all,l,LTYPE)           
p_QNITROgl(g,l) + p_AFNITROg(g,l) 
     = p_QCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l) 
     - ECROPgl(g,l)* [p_PNITROgl(g,l) - p_AFNITROg(g,l)
                       -  p_PCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l)];
!Demand for augmented land input !
p_QAUGLANDgl(g,l) 
     = p_QCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l)
     - ECROPgl(g,l)* [p_PAUGLANDgl(g,l) - p_PCROPgl(g,l) - p_AOCROPr(GRID2REG(g),l)] ;

These two equations are the computer implementation of input demand equation (3) in the analytical model in Box 1 (appended at the bottom of this document). The terms in this code beginning with A (e.g., AOCROP) have been added to allow for technological change.
There are three inputs in the augmented land composite (see the code below), and each has its own supply conditions (recall equation 4 in the analytical model in Box 1). Therefore, we must compute the combined supply response for the composite augmented land input as an independent exercise. We have done so numerically using a local perturbation to crop price, and this result is given for the ten grid cells in Table 1 below. For purposes of this lab, we can think in terms of this as the supply elasticity for the (composite augmented) land input. This puts us back in the context of the analytical model, wherein land is inelastically supplied and, with the market price of nitrogen fixed, there is just one variable, nonland input (labeled N).
! Supply of land by grid-cell
    ----------------------------------------------------------------------!
Equation E_PLANDgl     (all,g,GRID)(all,l,LTYPE)    
p_QLANDgl(g,l) 
    = ELANDg(g)      *  p_PLANDg(g) + s_QLANDg(g) 
    - ETRAN_LANDg(g) * [p_PLANDgl(g,l) - p_PLANDg(g)];
! Water supply by grid-cell  
    ----------------------------------------------------------------------  !
Equation E_PWATERgl (all,g,GRID)(all,l,LTYPE)                                      
    p_QWATERgl(g,l)  = EWATERr(GRID2REG(g)) * p_PWATERgl(g,l); 

! Supply of other inputs, by grid-cell & land type
    ----------------------------------------------------------------------  !
E_PNLANDgl    (all,g,GRID)(all,l,LTYPE)      
p_QNLANDgl(g,l) = ENLANDr(GRID2REG(g)) * p_PNLANDgl(g,l);
Finally, there is the zero profits equation, which, while normally expressed in terms of prices (equation 2 in the analytical model, Box 1), can also be expressed in quantities as shown here, provided the farms are minimizing costs in making their production decisions:
!Alternative form of zero profit condition
    ----------------------------------------------------------------------!
E_QCROPgl     (all,g,GRID)(all,l,LTYPE) 
P_QCROPgl(g,l)   
     = SHR_NITROgl(g,l) * p_QNITROgl(g,l) 
     + SHR_NLANDgl(g,l) * p_QNLANDgl(g,l) 
     + SHR_LANDgl(g,l)  * p_QLANDgl(g,l) 
     + SHR_WATERgl(g,l) * p_QWATERgl(g,l) 
     + p_AOCROPr(GRID2REG(g),l);
We start by shocking the US corn/soy price by +10%. This should be viewed as a permanent price increase, not a seasonal blip or a one-year change. This could be due to a permanent improvement in market conditions or perhaps a permanent hike in government support, equivalent to a ten percent rise in expected revenue per unit of output. The parameter settings in this model are designed to reflect the full adjustment of producers to this higher price. 
Let’s start by running the full SIMPLE-G-US-CS model on the GeoHub. Since the US crop price is endogenous in this model’s normal closure, we need to swap price with the quantity of biofuels demanded in the US. Then we can shock price, asking the question: how much would biofuels demand have to increase to boost price in the US by 10%? Once we get this experiment running on the GeoHub, we will return to the mini-model.
Load the simple-mini.cls closure file and then shock PCROP by 10%, solving the model using Gragg 2-4-6 with automatic accuracy. Open AnalyseGE and search for key parameters so that you can paste them into the missing values in the IN row of Table 2 below. Next fill in the key outcome variables: p_PAUGLANDgl(g,l), p_QAUhGLANDgl(g,l), p_QNITROgl(g,l), p_QCROPgl(g,l), first for the irrigated cropping practices and then for the rainfed ones. 
Now use this information to provide a detailed analysis of the impacts of the crop price rise: The following mapping will be useful as you seek to bring to bear the analytical model insights developed in the lecture in your analysis of these results:
p_QCROPgl(g,l) =  Crop output, by grid and land type
p_QAUGLANDgl(g,l) =  Derived demand for augmented land, by grid and land type
p_QNITROgl(g,l) =  Derived demand for N, by grid and land type
p_PCROPr(GRID2REG(g)) =  Regional crop price
p_PAUGLANDgl(g,l) =  Price of augmented land, by grid and land type
p_PNITROgl(g,l) =  Price of N, by grid and land type
ECROPgl(g,l) =  Elasticity of substitution btw N and augmented land, by grid and land type
ELANDg(g) =  Supply elasticity of augmented land, by grid-cell
SHRAUGLANDgl(g,l) =  Cost share of augmented land in total cost 
Recall from the analytical model lecture the way in which a crop price change is transmitted to farmland returns when non-land input prices are unchanging:
Treating augmented land as the ‘land’ input in this expression, discuss the variation in p_PAUGLANDgl(g,l) across grid cells. (Important note: the analytical solutions are only linear approximations and will not hold exactly when you plug in the results from the computational model. But these approximations are generally good enough to allow an explanation of the results and capture the key differences across grid cells.)
Your discussion here – feel free to focus on a few extreme grid cell outcomes: 
Now consider the change in output of a given practice in a grid cell. Here is the decomposition of supply response into the intensive and extensive margins:
Identify the grid cells in table 2 with the largest and the smallest supply response and use this equation and the parameter values reported in that table in order to explain why these two grid cells show different supply responses. 
Hint: To make your life easier, you may want to leverage AnalyseGE and the following decomposition expression provided at the bottom of the model code:
Equation E_p_QCROP_A (all,g,GRID)(all,l,LTYPE)     
p_QCROP_A(g,l)
    =  {[(1/SHR_ALANDgl(g,l))-1] * ECROPgl(g,l)} * p_PCROPgl(g,l) 
      + {[(1/SHR_ALANDgl(g,l)) * EALANDgl(g,l)]} * p_PCROPgl(g,l)
      - {[(1/SHR_ALANDgl(g,l)) - 1] * ECROPgl(g,l)} * p_PNITROgl_t(g,l)
      - {[(1/SHR_ALANDgl(g,l)) - 1] * EALANDgl(g,l)} * p_PNITROgl_t(g,l) ;
The left-hand side of this equation offers an approximation to the output change based on the solution of the linear model. By evaluating the components of this equation, you can decompose the change in crop output into the intensive and extensive margins – both with respect to changes in crop price as well as the price of nitrogen.
Your discussion here:
Now return to your GeoHub solution for this problem.
What do you think will be the main difference between the results for your ten grid cells coming from the mini-model and those obtained from the full model? Why?
What happens to the prices of nitrogen fertilizer and other non-land inputs in this simulation? How does this affect output?
Now let us consider the impact of a nitrate leaching tax on gridded output and input usage when crop price is fixed, as might be the case if this tax is only applied locally. 
Let’s start by running the full SIMPLE-G-US-CS model on the GeoHub once again. This time we are applying a $100/ton leaching tax. Please start this simulation running and then return to the mini-model.
Load the simple-mini.cls closure file and then shock NTAX by $100/ton leaching, solving the model using Gragg 2-4-6 with three sub-intervals. Paste into the IN row of table 3 the results for the following outcome variables: p_PNITRO_t, p_PAUGLANDgl(g,l), p_QAUGLANDgl(g,l), p_QNITROgl(g,l), p_QCROPgl(g,l), first for the irrigated cropping practices and then for the rainfed ones.
From the analytical model, we have the following relationship:
Where is the tax share of the farm price of nitrogen. This will be equal to the leaching tax multiplied by the leaching intensity (tons leached/tons applied). Discuss the impact of leaching intensity (LEACHINTgl(g,l)) on the change in fertilizer price (p_PNITROgl_t(g,l)) facing farmers in the different grid cells, and across irrigated and rainfed practices:
Next discuss the impact on returns to augmented land (p_PAUGLANDgl(g,l)):
What about the change in fertilizer usage? In the simplified case of fixed crop prices, the change in fertilizer use becomes:
So fertilizer use will drop more, the larger is the fertilizer cost share (i.e., the smaller is land’s cost share), the greater the substitution possibilities of N for L and the larger the acreage response. Discuss the results for the grid cells with the largest and smallest changes in fertilizer use. 
Hint: There is a decomposition expression at the bottom of the mini-model code that can assist you in this analysis. As with the output decomposition above, this uses a linear approximation to the solution as follows: 
Equation E_p_QNITROgl_A (all,g,GRID)(all,l,LTYPE)     
p_QNITROgl_A(g,l)
    =  {(1/SHR_ALANDgl(g,l)) * [ECROPgl(g,l) + EALANDgl(g,l)]} * 
        [p_PCROPgl(g,l) - p_PNITROgl_t(g,l)]  
      + [EALANDgl(g,l) * p_PNITROgl_t(g,l)];
Now use the output decomposition given previously to discuss the impact on output by practice and grid cell of the fertilizer price increase. How much of the output change is due to de-intensification and how much is due to a reduction in area?
Your discussion here:
An alternative decomposition of the output change (again from the analytical results lecture) is as follows:
Use this to decompose the output change into that attributable to the change in augmented land and that attributable to the change in nitrogen input. 
Hint: since this equation appears directly in the model – albeit with the component parts of augmented land broken out – you can use AnalyseGE to evaluate the individual contributions of each input to the total output change. Here is the relevant equation from the mini-model code:
E_QCROPgl     (all,g,GRID)(all,l,LTYPE) 
P_QCROPgl(g,l)   
     = SHR_NITROgl(g,l) * p_QNITROgl(g,l) 
     + SHR_NLANDgl(g,l) * p_QNLANDgl(g,l) 
     + SHR_LANDgl(g,l)  * p_QLANDgl(g,l) 
     + SHR_WATERgl(g,l) * p_QWATERgl(g,l) 
     + p_AOCROPr(GRID2REG(g),l); 
Now return to your GeoHub solution for this problem.
What do you think will be the main difference between the results for your ten grid cells coming from the mini-model and those obtained from the full model? Why?
What happens to the price of crop output in the face of this fertilizer tax? How does this affect output? How does it affect N use?
The notion of taxing fertilizer purchases is not very popular with the agricultural community in the United States. The more common approach involves conservation measures such as wetland restoration. In this case, on suitable lands (typically former wetlands that have been drained) a fraction of the land in the lowest part of the field is restored to wetland status. This restoration is costly, and the government typically participates through cost-sharing. Here, we assume that the government covers the full cost of wetland restoration, so that the main cost to the farmer is the loss in land area. We assume that this, too, is compensated, so the main economic impact of this conservation practice is to make land more scarce on the farm, while leaving overall revenue unchanged. This is accomplished via a backward shift in the land supply curve and a compensating revenue stream, computed based on land rents. The reduction in leaching rate accomplished via these wetlands varies by location and it computed based on biophysical variables. In this application, we assume that one percent of the land is set aside and farmers are compensated for the cost share of land times one percent of total revenue. 
First examine the overall impact on output using the input-based decomposition:
E_QCROPgl     (all,g,GRID)(all,l,LTYPE) 
P_QCROPgl(g,l)   
     = SHR_NITROgl(g,l) * p_QNITROgl(g,l) 
     + SHR_NLANDgl(g,l) * p_QNLANDgl(g,l) 
     + SHR_LANDgl(g,l)  * p_QLANDgl(g,l) 
     + SHR_WATERgl(g,l) * p_QWATERgl(g,l) 
     + p_AOCROPr(GRID2REG(g),l);
What is the relative contribution of each input to the overall change in output? Why do cropping activities experience an increase in output?
Next consider the impact on land use, by examining the land supply equation:
What do you conclude about the overall reduction in land use? Why is it not one percent?
What happens to overall fertilizer use? 
 Box 1: Analytical model of gridded impacts of environmental constraints
Table 1. Supply Elasticity for Augmented Land | Table 1. Supply Elasticity for Augmented Land | Table 1. Supply Elasticity for Augmented Land
Grid cell | Irrigated | Rainfed
KS | 0.80 | 0.77
SD | 1.26 | 1.13
NE | 0.77 | 0.75
MN | 1.03 | 1.05
IA | 0.84 | 0.77
MO | 0.95 | 0.95
WI | 1.12 | 1.16
IL | 0.96 | 0.96
IN | 1.07 | 1.11
OH | 0.87 | 0.79
Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise | Table 2A. Irrigated production parameters and results from crop price rise
 | Parameters | Parameters |   |  | Results PCROP 10% | Results PCROP 10% |   |  
Grid cell | land supply | land cost share | subst elast | subst elast | PAUGLAND | QAUGLAND | QNITRO | QCROP
KS | 0.80 | 0.90 | 0.262 |  | 11.56 | 9.06 | 12.23 | 9.46
SD | 1.26 | 0.87 | 0.25 |  | 11.14 | 14.09 | 17.14 | 14.38
NE | 0.77 | 0.85 | 0.184 |  | 12.63 | 9.47 | 11.90 | 9.95
MN | 1.03 | 0.89 | 0.295 |  | 11.37 | 11.72 | 15.32 | 12.13
IA | 0.84 | 0.84 | 0.218 |  | 12.84 | 10.49 | 13.45 | 11.11
MO | 0.95 | 0.88 | 0.262 |  | 11.64 | 10.95 | 14.20 | 11.39
WI | 1.12 | 0.87 | 0.274 |  | 11.38 | 12.85 | 16.23 | 13.23
IL | 0.96 | 0.87 | 0.233 |  | 11.60 | 11.01 | 13.89 | 11.39
IN |  |  |  |  |  |  |  | 
OH | 0.87 | 0.83 | 0.207 |   | 12.69 | 10.82 | 13.60 | 11.37
 |  |  |  |  |  |  |  | 
Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise | Table 2B. Rainfed  production parameters and results from crop price rise
 | Parameters | Parameters |   |  | Results PCROP 10% | Results PCROP 10% |   |  
Grid cell | land supply | land cost share | subst elast | subst elast | PAUGLAND | QAUGLAND | QNITRO | QCROP
KS | 0.77 | 0.76 | 0.136 |  | 13.17 | 9.84 | 11.70 | 10.27
SD | 1.13 | 0.68 | 0.125 |  | 14.79 | 16.84 | 18.86 | 17.46
NE | 0.75 | 0.74 | 0.122 |  | 13.55 | 9.71 | 11.42 | 10.13
MN | 1.05 | 0.84 | 0.245 |  | 11.96 | 12.55 | 15.71 | 13.04
IA | 0.77 | 0.78 | 0.18 |  | 12.92 | 9.63 | 12.06 | 10.15
MO | 0.95 | 0.82 | 0.203 |  | 12.21 | 11.46 | 14.11 | 11.92
WI | 1.16 | 0.85 | 0.263 |  | 11.75 | 13.73 | 17.10 | 14.20
IL | 0.96 | 0.82 | 0.192 |  | 12.27 | 11.71 | 14.22 | 12.15
IN |  |  |  |  |  |  |  | 
OH | 0.79 | 0.80 | 0.182 |   | 12.57 | 9.64 | 12.03 | 10.11
Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax | Table 3A. Irrigated production parameters and results from leaching tax |  |  | 
 | Parameters | Parameters |   |  |  | Results NTAX100 | Results NTAX100 |   |   |  
Grid cell | land supply | land cost share | subst elast | leaching int | leaching int | PNITRO_t | PAUGLAND | QAUGLAND | QNITRO | QCROP
KS | 0.80 | 0.90 | 0.262 | 0.11 |  |  |  |  |  | 
SD | 1.26 | 0.87 | 0.25 | 0.1 |  |  |  |  |  | 
NE | 0.77 | 0.85 | 0.184 | 0.23 |  |  |  |  |  | 
MN | 1.03 | 0.89 | 0.295 | 0.16 |  |  |  |  |  | 
IA | 0.84 | 0.84 | 0.218 | 0.24 |  |  |  |  |  | 
MO | 0.95 | 0.88 | 0.262 | 0.16 |  |  |  |  |  | 
WI | 1.12 | 0.87 | 0.274 | 0.3 |  |  |  |  |  | 
IL | 0.96 | 0.87 | 0.233 | 0.22 |  |  |  |  |  | 
IN | 1.07 | 0.87 | 0.239 | 0.26 |  |  |  |  |  | 
OH | 0.87 | 0.83 | 0.207 | 0.26 |   |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | 
Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax | Table 3B. Rainfed  production parameters and results from leaching tax |  |  | 
 | Parameters | Parameters |   |   |  | Results NTAX100 | Results NTAX100 |   |   |  
Grid cell | land supply | land cost share | subst elast | leaching int | leaching int | PNITRO_t | PAUGLAND | QAUGLAND | QNITRO | QCROP
1 | 0.77 | 0.76 | 0.136 | 0.31 |  |  |  |  |  | 
2 | 1.13 | 0.68 | 0.125 | 0.41 |  |  |  |  |  | 
3 | 0.75 | 0.74 | 0.122 | 0.5 |  |  |  |  |  | 
4 | 1.05 | 0.84 | 0.245 | 0.35 |  |  |  |  |  | 
5 | 0.77 | 0.78 | 0.18 | 0.42 |  |  |  |  |  | 
6 | 0.95 | 0.82 | 0.203 | 0.36 |  |  |  |  |  | 
7 | 1.16 | 0.85 | 0.263 | 0.34 |  |  |  |  |  | 
8 | 0.96 | 0.82 | 0.192 | 0.33 |  |  |  |  |  | 
9 | 1.11 | 0.83 | 0.217 | 0.35 |  |  |  |  |  | 
10 | 0.79 | 0.80 | 0.182 | 0.38 |   |  |  |  |  | 

					: US crop price from SIMPLE	
				: agricultural entry/exit; zero profits
	             : demand for agricultural input j	
	                          : supply of input j to agriculture 
		: farmer’s cost of inputs		
                                                      : US output
                                                      : US input use
Where:
	: % change in regional (or gridded) crop output 
	: % change in regional (or gridded) demand for agricultural input  j
	: % change in the grid cell price of agricultural output
	: % change in the farmers’ price of agricultural input j in grid cell k
	: % change in the specific tax on agricultural input j in grid cell k
	: tax share of input cost in grid cell k
	: non-negative elasticity of substitution between land and non-land inputs
	: non-negative elasticity of factor supply for input j in grid cell k 
	: non-negative cost share of input j in grid cell k

### Learning about Water in SIMPLE-G-US at the level of individual grid cells
*Source file:* `Hands-On Lab with mini Water model-final.docx`  ·  *type:* file

Hands-on Lab:
Learning about Water in SIMPLE-G-US at the level of individual grid cells
Iman Haqiqi
SIMPLE-G Short Course 
Purdue University, West Lafayette, IN
September 16-20, 2019
Key References:
Core Model:
Baldos, Uris Lantz C., Iman Haqiqi, Thomas W. Hertel, Mark Horridge, and Jing Liu. 2019. “SIMPLE-G: A Multiscale Framework for Integration of Economic and Biophysical Determinants of Sustainability.” In Preparation for Environmental Modelling & Software. 
Application: 
Haqiqi, Iman, Laura Bowling, Sadia Jame, Thomas Hertel, Uris Baldos, and Jing Liu. 2018. “Global Drivers of Land and Water Sustainability Stresses at Mid-Century.” Purdue Policy Research Institute, Policy Brief 4 (1). https://docs.lib.purdue.edu/gpripb/ .
 (This will be more fully developed for journal submission.)
Introduction
This set of exercises will introduce the water module of the gridded SIMPLE model, SIMPLE-G. SIMPLE is a Simplified International Model of agricultural Prices, Land use and the Environment. It is a partial equilibrium economic model which connects human system decisions to land and water in the environmental systems. Here, you will mainly focus on the local (gridded) drivers of agricultural water supply and demand. This is an example of how you may be able to link changes in environmental systems to the human system. 
To understand how SIMPLE-G makes the connection between changes in agriculture and environment, you will focus on the production at each grid cell. You will do so by fixing the national crop price – in effect turning off the part of the SIMPLE that we rely on for generating national and international equilibria in crops. Crop demand will also be irrelevant for this analysis, as we will be predetermining any price changes exogenously. In other words, the trade and the consumption side of the model is off. The model code that we will be working with here is an excerpt from the full SIMPLE-G model – focusing solely on what happens at the grid cell level.
Since we eliminate any interaction across grid cells (which only happens through market mechanisms in SIMPLE-G), we are free to pick just a subset of the grid cells – in this case 10. By examining how these heterogeneous grid cells respond to 1) an exogenous shock to water supply, and 2) an exogeneous shock to rainfed crop productivity, 3) an exogeneous shock to irrigated crop productivity. The results can be generalized to learn about the heterogenous outcomes when we solve the full model with tens of thousands of grid cells. Of course, since we are not modeling all the grid cells in the US, we cannot speak to potential changes in market conditions and prices. These non-gridded prices will be treated as exogenous variables in the closure.
Requirements
Exercise files: SIMPLE-G-US-mini.zip
Software: RunGEM from GEMPACK, available at: https://www.copsmodels.com/gprgem.htm; 
Any spreadsheet program, e.g. Google Sheets
Note: by installing GEMPACK you will also have access to: 
Overview of the production structure of SIMPLE-G Water
Production structure in SIMPLE-G-US is illustrated in figure 1. This is called a ‘nested’ crop production system. There are five main inputs identified in this model: nitrogen, land, water, irrigation equipment, and other inputs. The model determined equilibrium changes in price and quantity of each input. For purposes of this lab, we will focus on the ‘water nest’ (QWATERgl). This means, we will focus on what happens to water withdrawal (QW-WDRLgl) and irrigation equipment (QW-EQPTgl). However, the nested production technology provides the possibility of substitution between one input and aggregated other inputs. For example, there is a substitution between nitrogen and aggregated other inputs (QAUGLAND). Here is a list of what is included in each nest:
QWATERgl ~ QWWDRLgl + QWEQPTgl
QLANDWTRgl ~ QLANDgl + QWATERgl
QAUGLANDgl ~ QLANDWTRgl + QNLANDgl
Figure 1. production structure in SIMPLE-G-US
There is a substitution between water withdrawal and irrigation equipment. The “irrigation equipment” includes not only the capital, but also, any additional irrigation infrastructure which can potentially be used to reduce water withdrawal. On the other hand, the “water withdrawal” includes water and other irrigation inputs which depend on the volume of water applied (like additional labor for irrigation, additional energy for irrigation, and so on). Note that we distinguish between the water nest and aggregate water withdrawals. When we talk about the irrigation expansion, we will be referring to increases in irrigation area; when we talk about irrigation intensity, we refer to volume of water applied per unit of crop produced; when we talk about the irrigation efficiency, we refer to a costless exogeneous change in the irrigation water use (e.g. change in management, timing, and productivity). 
A quick look at key equations
Change in water withdrawal depends on the change in irrigation area, change in the scale of production, and substitutions between the inputs. We introduce the “AgWater-Identity” as:
This identity shows that total water withdrawal in each grid cell depends on the irrigated area, crop yields, and water per crop. This identity gives rise to the following decomposition in the TABLO code:
! decomposing water use!
   WATERgl(g,l) = QLANDgl(g,l) * YIELDgl(g,l) * WATperCROPgl(g,l);

This identity decomposes the change in water withdrawal into three main components which we can track in the TABLO with the AnalyseGE. 
!change in water per crop!
p_WATperCROPgl_A(g,l) =  
     - ECROPgl(g,l)    * [p_PAUGLANDgl(g,l) - p_PCROPgl(g,l)    ] !subs with Nitro
     - EAUGLANDgl(g,l) * [p_PLANDWTRgl(g,l) - p_PAUGLANDgl(g,l) ] !subs with Other
     - EIRRIGgl(g,l)   * [p_PWATERgl(g,l)   - p_PLANDWTRgl(g,l) ] !subs with Land
     - ESUB_WKgl(g,l)  * [p_PWWDRLgl(g,l)   - p_PWATERgl(g,l)   ] !subs with EQPT;

!change in yield!
p_YIELDgl_A(g,l) =  
     + ECROPgl(g,l)    * [p_PAUGLANDgl(g,l) - p_PCROPgl(g,l)    ] !subs with Nitro
     + EAUGLANDgl(g,l) * [p_PLANDWTRgl(g,l) - p_PAUGLANDgl(g,l) ] !subs with Other
     + EIRRIGgl(g,l)   * [p_PLANDgl(g,l)    - p_PLANDWTRgl(g,l) ] !subs with water

Note that prices of other inputs are determined in the market and depend on their underlying supply elasticity. In the experiments with the mini model, price of nitrogen and other inputs are given. However, land is in limited supply in the grid cell and so the use of irrigated land depends on competition with rainfed production in that grid cell as well. 
!supply of total cropland!
E_QLANDg     (all,g,GRID)   
p_QLANDg(g) = ELANDg(g) *  p_PLANDg(g) ;

!allocation of cropland to irrigated and rainfed!
E_PLANDgl     (all,g,GRID)(all,l,LTYPE)    
p_QLANDgl(g,l) 
    = p_QLANDg(g) + s_QLANDgl(g,l)
    - ETRAN_LANDg(g) * [p_PLANDgl(g,l) - p_PLANDg(g)];

!Average land rents!
E_PLANDg      (all,g,GRID)                           
p_PLANDg(g) = 
    sum(l,LTYPE, SHR_VLANDgl(g,l) * p_PLANDgl(g,l)) ; 


Finally, there is the zero profits equation, which, while normally expressed in terms of prices (equation 2 in the analytical model), is can also be expressed in quantities as shown here, provided the farms are minimizing costs in making their production decisions:
!Alternative form of zero profit condition!
E_QCROPgl     (all,g,GRID)(all,l,LTYPE) 
P_QCROPgl(g,l)   
     = SHR_NITROgl(g,l) * p_QNITROgl(g,l) 
     + SHR_NLANDgl(g,l) * p_QNLANDgl(g,l) 
     + SHR_LANDgl(g,l)  * p_QLANDgl(g,l) 
     + SHR_WATERgl(g,l) * p_QWATERgl(g,l) ;
Step-by-step guide to use RunGEM 
To run an experiment, you should follow these steps:
Make sure you have RunGEM installed and working.
Unzip the experiment file.
Open the simple-g-us.tab file in TABmate. On the top toolbar, click on “TABLOCode”. (Make sure GEMSIM is selected on the top right).
Open RunGEM.
In the “Model/Data” tab, select the simple-g-us.gss file as in the model directory.
Select the data files accordingly from the “Data” folder.
In the “closure” tab, select the file from the “Closure” folder.
In the “Shocks” tab, select the desired shock file from “Shocks” folder.
In the “Output files”, name your solution.
In the “Solve” tab, choose “Gragg-2-4-6” and choose a description.
Click on solve. And go to the “Results”.
Exercise 1: a look at data and parameters
Got to the Data folder.
Open the GRIDPARM.HAR file. 
Find and write down the description of the followings:
Fill in the blank.
Table 1. values of major parameters 
How different is ECROPgl for CA-grid with other grid cells? What are the implications of it?
How different is EIRRIGgl for CA-grid with other grid cells? What are the implications of it?
How about ETRAGIGg and ELAND for CA-grid?
Exercise 2: water scarcity
We start by looking at the impacts of a local water scarcity scenario. You may need to obtain the value of the shocks by looking at historical changes or from environmental and hydroclimatic simulations. In this experiment we shock the water supply by uniform -10% for all grid cells. This should be viewed as a permanent decrease, not a seasonal blip or a one-year change. The parameter settings in this model are designed to reflect the full adjustment of producers to this shock. Load the watScarcity.shf shock file (shock s_QWATERg by -10%), solving the model using Gragg 2-4-6. [Open the RunGEM. Load the model, data, closure, and shock (watScarcity.shf). Give a name to the experiment and solve the experiment. 
Fill in the blank. 
Table 2: post simulation values for value shares and quantity ratios (irrigated)
Table 3: post simulation values for value shares and quantity ratios (rainfed)
Which grid cell/practice has the highest average yields? 
Which one has the highest N per crop output?
Which one has the highest water cost share?
Fill in the blank.
Table 4: Impacts of 10% reduction in water availability (irrigated crops)
Table 5: Impacts of 10% reduction in water availability (rainfed crops)
Decompose the changes in the water use.
Discuss the results. Why are some grid cells much more responsive to this shock than others? 
Exercise 3: global warming (3-A)
For the global warming scenario, we assume the yield of rainfed production will decline due to the heat stress, but that this will be largely mitigated for rainfed production. We do this by shocking p_AOCROgl(g,”rainfed”) by -10%. Again, this should be viewed as a permanent increase, not a one-year change. Load the warming_rfd.shf shock file and solve the model using Gragg 2-4-6. Note that this shock is a total factor productivity shock – i.e., farmers applying the same mix of inputs under the new climate obtain ten percent less production than under the old climate. Of course, we expect some adjustment in input mix as relative prices change.
Fill the blank.
Table 6: Impacts of 10% reduction in rainfed productivity on irrigated agriculture
Table 7: Impacts of 10% reduction in rainfed productivity on rainfed agriculture
What happens to total cropland supply?
Discuss the results. Why some grid cells are very responsive to this shock? 
Exercise 4: global warming (3-B)
For our second global warming scenario, we assume that both the yields of rainfed and irrigated production will decline due to the heat stress. We also assume the water requirement by crops are higher for irrigated practices. We do this by shocking AOCROgl(g,”rainfed”) by -10%, AOCROgl(g,”irrigated”) by -5%, and AFWATERgl = -10%. Again, this should be viewed as a permanent increase, not a one-year change. Load the warming_all.shf shock file and solve the model using Gragg 2-4-6. 
Fill table 8 and 9.
Table 8: Impacts of global warming on irrigated agriculture
Table 9: Impacts of global warming on rainfed agriculture
Decompose the changes in the water use.
Discuss the results. Why some grid cells more responsive than others to this shock? 
ECROPgl | 
EIRRIGgl | 
ETRANIGg | 
ELAND | 
 | ECROPgl | ECROPgl | EIRRIGgl | EIRRIGgl | ETRANIGg | ELAND
 | Irrigated | Rainfed | Irrigated | Rainfed |  | 
TX | 0.20 | 0.03 | 0.09 | 0.09 | -2.51 | 0.042
ID | 0.21 | 0.20 | 0.27 | 0.27 | -0.01 | 0.041
CA |  |  |  |  |  | 
AR | 0.23 | 0.22 | 0.34 | 0.34 | -1.26 | 0.032
IL | 0.25 | 0.23 | 0.31 | 0.31 | -1.88 | 0.037
MO | 0.23 | 0.22 | 0.31 | 0.31 | -1.88 | 0.017
ND | 0.27 | 0.25 | 0.47 | 0.47 | -0.01 | 0.036
WA | 0.20 | 0.20 | 0.45 | 0.45 | -0.01 | 0.002
NE | 0.23 | 0.20 | 0.17 | 0.17 | -0.63 | 0.046
MI | 0.25 | 0.22 | 0.31 | 0.31 | -1.88 | 0.031
grid cell | SHR_LAND | SHR_NITRO | SHR_WATER | YIELDgl | WATper
CROPgl | NITper
CROPgl
TX | 0.18 | 0.15 | 0.14 | 2.1 | 26.2 | 0.0031
ID | 0.10 | 0.06 | 0.20 | 7.7 | 40.6 | 0.0011
CA |  |  |  |  |  | 
AR | 0.21 | 0.18 | 0.16 | 2.7 | 32.8 | 0.0037
IL | 0.16 | 0.09 | 0.11 | 5.1 | 18.4 | 0.0018
MO | 0.09 | 0.07 | 0.11 | 6.5 | 18.7 | 0.0014
ND | 0.06 | 0.03 | 0.10 | 12.4 | 16.6 | 0.0006
WA | 0.25 | 0.05 | 0.09 | 1.0 | 16.8 | 0.0010
NE | 0.08 | 0.03 | 0.12 | 10.3 | 23.9 | 0.0007
MI | 0.10 | 0.05 | 0.10 | 7.7 | 16.6 | 0.0010
grid cell | SHR_LAND | SHR_NITRO | SHR_WATER | YIELDgl | WATper
CROPgl | NITper
CROPgl
TX | 0.12 | 0.25 | 0.00 | 1.0 | 0.0 | 0.0066
ID | 0.11 | 0.21 | 0.00 | 2.1 | 0.0 | 0.0042
CA |  |  |  |  |  | 
AR | 0.12 | 0.16 | 0.00 | 3.1 | 0.0 | 0.0032
IL | 0.10 | 0.07 | 0.00 | 6.9 | 0.0 | 0.0013
MO | 0.10 | 0.09 | 0.00 | 5.2 | 0.0 | 0.0017
ND | 0.10 | 0.13 | 0.00 | 3.0 | 0.0 | 0.0026
WA | 0.03 | 0.01 | 0.00 | 8.0 | 0.0 | 0.0001
NE | 0.10 | 0.07 | 0.00 | 5.1 | 0.0 | 0.0013
MI | 0.06 | 0.06 | 0.00 | 6.2 | 0.0 | 0.0012
grid cell | p_QCROPgl | p_QLANDgl | p_QNITROgl | p_QWWDRLgl | p_PLANDgl | p_PWATERgl
TX | -1.101 | -0.886 | -1.101 | -3.498 | -8.092 | 10.952
ID | -2.133 | -0.36 | -2.133 | -5.322 | -8.85 | 8.445
CA |  |  |  |  |  | 
AR | -2.004 | -0.92 | -2.004 | -5.306 | -3.874 | 8.594
IL | -1.572 | -1.726 | -1.572 | -5.234 | -1.08 | 7.268
MO | -1.516 | -1.921 | -1.516 | -5.336 | -1.109 | 7.153
ND | -0.963 | -0.017 | -0.963 | -5.257 | -2.182 | 7.034
WA | -0.665 | -0.007 | -0.665 | -4.953 | -1.406 | 8.289
NE | -1.284 | -0.72 | -1.284 | -4.509 | -9.071 | 9.556
MI | -1.17 | -1.194 | -1.17 | -5.085 | -2.077 | 7.277
grid cell | p_QCROPgl | p_QLANDgl | p_QNITROgl | p_PLANDgl
TX | 2.125 | 5.256 | 2.125 | -5.86
ID | -0.109 | -0.3 | -0.109 | 0.384
CA |  |  |  | 
AR | 0.599 | 1.589 | 0.599 | -1.941
IL | 0.025 | 0.083 | 0.025 | -0.116
MO | 0.013 | 0.044 | 0.013 | -0.061
ND | -0.001 | -0.004 | -0.001 | 0.005
WA | 0 | 0.002 | 0 | -0.004
NE | 0.818 | 2.827 | 0.818 | -3.871
MI | 0.131 | 0.683 | 0.131 | -1.092
grid cell | p_QCROPgl | p_QLANDgl | p_QNITROgl | p_QWWDRLgl | p_PLANDgl | p_PWATERgl
TX | 0.953 | 1.572 | 0.953 | 1.069 | -8.092 | 10.952
ID | -0.021 | -0.062 | -0.021 | -0.018 | -8.85 | 8.445
CA |  |  |  |  |  | 
AR | 2.538 | 4.658 | 2.538 | 1.736 | -3.874 | 8.594
IL | 6.637 | 15.741 | 6.637 | 5.168 | -1.08 | 7.268
MO | 3.826 | 13.809 | 3.826 | 3.328 | -1.109 | 7.153
ND | -0.163 | -0.902 | -0.163 | -0.097 | -2.182 | 7.034
WA | 0.047 | 0.084 | 0.047 | 0.027 | -1.406 | 8.289
NE | 0.205 | 0.661 | 0.205 | 0.257 | -9.071 | 9.556
MI | 2.68 | 8.859 | 2.68 | 2.37 | -2.077 | 7.277
grid cell | p_QCROPgl | p_QLANDgl | p_QNITROgl | p_PLANDgl
TX | -26.346 | -18.967 | -18.421 | -5.86
ID | -20.603 | -0.293 | -13.621 | 0.384
CA |  |  |  | 
AR | -22.984 | -11.44 | -16.387 | -1.941
IL | -19.797 | -2.014 | -13.019 | -0.116
MO | -19.799 | -0.911 | -12.93 | -0.061
ND | -20.298 | -1.119 | -13.744 | 0.005
WA | -20.791 | -0.14 | -13.825 | -0.004
NE | -21.62 | -9.496 | -14.727 | -3.871
MI | -21.561 | -6.955 | -14.843 | -1.092
grid cell | p_QCROPgl | p_QLANDgl | p_QNITROgl | p_QWWDRLgl | p_PLANDgl | p_PWATERgl
TX | -8.984 | -0.748 | -5.171 | -4.744 | -24.538 | 8.603
ID | -11.08 | -1.066 | -7.403 | -8.46 | -22.474 | 2.364
CA |  |  |  |  |  | 
AR | -8.88 | 1.51 | -5.209 | -7.216 | -18.854 | 4.851
IL | -7.228 | 5.801 | -3.589 | -5.646 | -23.569 | 6.515
MO | -9.438 | 3.957 | -5.789 | -7.237 | -26.113 | 3.687
ND | -11.131 | -1.058 | -7.74 | -9.288 | -15.729 | -0.163
WA | -8.435 | 0.026 | -4.599 | -7.632 | -12.236 | 3.295
NE | -10.633 | -1.31 | -7.033 | -7.351 | -25.757 | 4.134
MI | -9.355 | 2.895 | -5.8 | -7.17 | -23.594 | 3.54
grid cell | p_QCROPgl | p_QLANDgl | p_QNITROgl | p_PLANDgl
TX | -21.667 | -5.663 | -13.238 | -26.052
ID | -20.825 | -1.129 | -13.862 | -30.014
CA |  |  |  | 
AR | -21.159 | -5.595 | -14.407 | -23.408
IL | -19.681 | -1.504 | -12.893 | -26.421
MO | -19.746 | -0.674 | -12.873 | -27.882
ND | -20.307 | -1.158 | -13.754 | -28.354
WA | -20.789 | -0.117 | -13.823 | -30.15
NE | -19.805 | -1.767 | -12.752 | -26.3
MI | -21.022 | -3.355 | -14.257 | -26.097

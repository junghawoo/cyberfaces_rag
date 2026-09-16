---
title: "Lectures"
unit_id: 33
course_id: 1
level: "Expert"
slug: lectures
is_course: 0
---

# Lectures

**Description:** Instructor presentations.

## Extracted resources (local files)

### Hertel: Analytics of the Gridded Model.pdf
*Source file:* `Analytics of the Gridded Model.pdf`  ·  *type:* file

ANALYTICAL FOUNDATIONS OF SIMPLE-G
Thomas Hertel
SIMPLE-G Short Course
Purdue University
September 16, 2019

• SIMPLE-G WAS INSPIRED BY CLIMATE SCIENCE:
- GCMs solved globally and provide boundary conditions (e.g., sea surface 
temperature) used as inputs to high resolution RCMs
- SIMPLE (non-gridded version) is like the GCM – (very) coarse resolution, 
producing global price changes which can be fed into the gridded model
- Due to its simpler structure, the gridded model will be nested within the 
global model and solved simultaneously
- It is nonetheless useful to think of this as a two step process wherein global 
prices and national prices are determined at one level and gridded 
responses at the fine-scale
• FOR EXPOSITORY PURPOSES, THIS LECTURE:
- Assumes that the global (and national) crop price is given
- Focuses exclusively on what happens at the grid cell level
- How do we understand/explain heterogeneous grid cell responses?
- Focus on percentage changes in gridded variables
- Analytical results based on simplified model facilitate understanding of 
underlying mechanisms and relationships
- Provide notational mapping to GEMPACK model at the end
Background and Motivation

Analytical Model

What drives land returns?
1( *
)
F
F
Lk
Lk
Nk
Nk
p
p
p


−
=
−
When nonland input prices (e.g., fertilizer) are unchanging, then land rents 
are a magnified reflection of output prices:
1 *
F
Lk
Lk
p
p
−
=
Combining equations (1) – (3) we obtain:

Impact on of price rise on grid cell output
(when nonland prices are unchanging)
1
1
[(
1)
] *
k
Lk
k
Lk
Lk
qo
p



−
−
=
−
+
Gridded output changes will be larger:
-
the smaller is the economic importance of land 
-
the greater the scope for intensification 
-
and the greater the crop land supply response
0
Lk

→
0
k

1
0
Lk
Lk

−

Intensive margin of supply
Extensive margin of supply

Tax on excess nitrogen use
F
Nk
N
Nk
Nk
P
P
T
=
+ 
(1
)
F
Nk
Nk
N
Nk Nk
p
p
t


=
−
+
Farmer’s fertilizer cost depends on price and tax per pound leached N and
is the leaching rate (N applied/N leached)
Percentage change in price depends on weighted combination of market price change
and tax rate change. Weight on tax is tax’s share in farmer’s overall cost per pound, i.e.
𝛺𝑁𝑘
/
F
Nk
Nk
Nk
Nk
T
P

= 

Impact of N tax on Land Returns
1( *
((1
)
))
F
Lk
Lk
Nk
Nk
N
Nk Nk
p
p
p
t




−
=
−
−
+
The change in gridded land rents depends on the severity of the tax in that grid cell
as well as the market price adjustment in nitrogen fertilizer.

Impact of tax on Land Rents
1( *
((1
)
))
F
Lk
Lk
Nk
Nk
N
Nk Nk
p
p
p
t




−
=
−
−
+
Gridded land rents are dependent on the severity of the tax in that grid cell.
When the fertilizer price is determined outside the grid cell (e.g., nationally), then:
1( *
)
F
Lk
Lk
Nk
Nk Nk
p
p
t


−
=
−
Gridded land rents are dependent on the severity of the tax in that grid cell, i.e., impact
is larger when N is a large share of total costs and N leaching rate is substantial.

Impact on grid cell output
(excess N taxed, N price fixed)
For taxed grid cells, there are two competing effects – the direct impact of the N tax 
on profitability and de-intensification in the grid cell, and the indirect impact of the 
cumulative tax impact on national output and hence on output price and ultimately on the 
intensive and extensive margins of supply. For grid cells no leaching, output will rise.
1
1
1
[(
1)
] * (
1)(
)
k
Lk
k
L
Lk
Lk
k
Lk
Nk Nk
qo
p
t







−
−
−
=
−
+
−
−
+
Indirect impact – higher output price
Raises output
Direct impact – higher fertilizer price
Lowers output

Impact on grid cell crop output
(excess N taxed, crop output price fixed)
When the crop price is fixed, then the size of the output reduction hinges on the potential
for substituting away from N (intensive margin) and the acreage reduction (extensive margin)
in that grid cell. The extent to which this deintensification and cropland reduction occurs also
depends on the cost share of N. As this gets larger, the cost share of labor gets smaller
and its inverse gets larger so that the first term on the RHS gets larger in absolute value.
1
(
1)(
)
0
F
k
Lk
k
Lk
Nk
qo
p



−
= −
−
+

Intensive 
margin
Extensive 
margin (area response)

Impact on grid cell fertilizer use
(excess N taxed, crop output price fixed)
When the crop price is fixed, then fertilizer use will drop more, the larger is the fertilizer cost
share (i.e., the smaller is land’s cost share), the greater the substitution possibilities of N for L
and the larger the acreage response.
1
1
[
(
1)
]
0
F
F
N
L
L
L
N
q
p



−
−
= −
+
−

De-intensification 
Area reduction due to lower 
profitability

Another decomposition of gridded 
output change
If we assume cost minimizing behavior, such that land and nonland inputs are paid the value
of their marginal product in crop production, and assuming that entry/exit leads to zero pure 
economic profits, then we can fully attribute output changes in each grid cell to changes in 
input use, with each input weighted by its economic importance in production (cost share). A 
given input’s contribution to the output change will be larger, then larger is:
-
Its cost share: 
-
Input growth, which depends on the technical potential for input substitution:  
-
As well as the relative price change                       which, in turn, depends on factor supply
conditions – does increased usage drive up price?
0
jk


0
k

k
Lk
Lk
Nk
Nk
qo
q
q


=
+
𝑝∗−𝑝𝑁𝑘

Impact on national output and price
Where      is the share of grid cell k in national output
k
k
k
qo
qo

=
𝛼𝑘
1
*
D
p
qo

−
=
Where      is the price elasticity of demand facing US producers. If this is low, the price
increase will be large.
𝜀𝐷

Mapping to SIMPLE-G notation & example
p_QCROPgl(g,l) =  
p_QAUGLANDgl(g,l) = 
p_QNITROgl(g,l) =
p_PCROPr(GRID2REG(g)) =
p_PAUGLANDgl(g,l) = 
p_PNITROgl(g,l) = 
ECROPgl(g,l) = 
ELANDg(g) = 
SHRAUGLANDgl(g,l) =    
𝑞𝑜𝑘
𝑞𝐿𝑘
𝑞𝑁𝑘
𝑝∗
𝜃𝐿𝑘
𝜈𝐿𝑘
𝜎𝑘
𝑝𝑁𝑘
𝐹
𝑝𝐿𝑘
𝐹
1
1
[(
1)
] *
k
Lk
k
Lk
Lk
qo
p



−
−
=
−
+
Equation E_p_QCROP_A (all,g,GRID)(all,l,LTYPE)     
p_QCROP_A(g,l)
=  {[(1/SHR_ALANDgl(g,l))-1] * ECROPgl(g,l)} * p_PCROPgl(g,l) 
+ {[(1/SHR_ALANDgl(g,l)) * EALANDgl(g,l)]} * p_PCROPgl(g,l)

### Haqiqi: Condensation_2019-09-15
*Source file:* `Condensation_2019-09-15.pdf`  ·  *type:* file

Condensation For SIMPLE-G
Iman Haqiqi
SIMPLE-G Short Course
Purdue University, West Lafayette
September 16-20, 2019

Large models and computation speed
• Speed of solution is a challenging issue for large models with millions 
of grid cells.
• For a large model with complex interconnections between the 
unknown variables, the issue is more critical (e.g. market response to 
farmers decision and farmers response to market equilibrium)
• People may design different algorithms to reduce the solution time 
• There are also techniques for better use of computational resources 
(CPU, GPU, and memory)
• We use a method called condensation…

What is condensation
• Reducing the model size before solving the linearized system of 
equations
• It involves
• Omit
• Substitute
• Backsolve

How effective is condensation?
• For the SIMPLE-G presented at National Press Club, with 4 million 
unknowns for ~75,000 grid cells.
• 45 minutes without condensation
• 2 minutes with condensation
• For a simplified model, with 6 million unknown and 1,000,000 grid 
cells
• 10 minutes without condensation
• 0.5 minute with condensation
*On a laptop with 8th gen core i7 and 32G memory

How GEMPACK/TABLO works
• You introduce variables and equations
• In either levels or percentage changes (e.g. PCROP, p_PCROP)
• Stage 1: Check
• TABLO checks your input file and reporting any error it finds
• It automatically linearizes all the level equations 
• Stage 2: Condensation
• TABLO substitute variables in the order you specify
• Stage 3: Code generation

How we do it: substitution
• If we re-write the system: C.z = 0
• We try to reduce the size (number of rows and/or columns) of C 
matrix.
1. substitute out variables
• Those that are to be endogenous
2. omit variables: 
• Those that are to be exogenous and not shocked in a group of simulations

Example
Suppose you want to substitute out (linear) variable x (all components of it) using 
the (linearized) equation.
x(i) = A(i)*y(i) + z(i)
TABLO will replace every occurrence of a component of x in the other (linearized) 
EQUATIONs For example, the equation:
B(i)*(x(i) + y(i)) = 0
Becomes:
B(i)*([A(i)*y(i)+z(i)] + y(i)) = 0

Omit, Backsolve or Substitution? 
• Omit:
• If all components of a (linear) variable x(i) are to be exogenous and not shocked, all 
values (changes or percentage changes) in the linearized equations will be zero.
• Substitute:
• If you are not interested in reporting the value of the variable
• Backsolve:
• You want to see the value of the variable which was substituted out
• If you plan to use AnalyseGE
• It is a post simulation process and takes some resources to report. 
• It is best to mark for backsolving only variables you think you will need to examine or 
report.

Condensation info file
====================================================
Final status of Equations (in decreasing size order)
====================================================
Equation name   |   Size     | Status of equation
----------------------|------------|--------------------
E_QCONS              |         64 |In condensed system
...
E_QNITROgl
|[    151332]|Used for BACKSOLVING
E_QLANDgl
|[    151332]|Used for BACKSOLVING
...
E_PNITROgl
|[         0]|ELIMINATED from system
...

Limitations
• Some condensations are not possible.
• The number of equations in the equation block must equal the number of 
components of the variable
• It should be possible to get an expression for EVERY component of the 
variable
• You should look ahead to substitution when preparing the code
• Order of substitution matters for some models
• Variables with complex interconnections can cause problems in condensation.
• First, substitute the variables with minimum interconnections

Thanks!

### Baldos: Economic Framework Recap 09-04-2019
*Source file:* `Economic Framework Recap 09-04-2019.pdf`  ·  *type:* file

RECAP ON THEORETICAL FRAMEWORK IN
SIMPLE MODEL
Presentation by Uris Baldos
Purdue University

THEORETICAL FRAMEWORK
• CONSIDER AGRICULTURE AS A SINGLE SECTOR
– produces all food, fiber and fuel from agriculture
– use land and non-land inputs (price of non-land is fixed)
– Farmers minimize costs, entry/exit results in zero economic 
profits
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making? 
See Technical Appendix to: The Global Supply and Demand for Agricultural Land in 2050: 
A Perfect Storm in the Making? AAEA Presidential Address Thomas W. Hertel, Purdue 
University (https://www.gtap.agecon.purdue.edu/resources/download/5115.pdf)

THEORETICAL FRAMEWORK
• CONSIDER AGRICULTURE AS A SINGLE SECTOR
– produces all food, fiber and fuel from agriculture
– use land and non-land inputs (price of non-land is fixed)
– Farmers minimize costs, entry/exit results in zero economic 
profits
•
DRIVERS OF LONG RUN CHANGE IN FOOD PRICES AND
AGRICULTURAL LAND CAN BE SUMMARIZED TO 3 KEY DRIVERS: 
– Demand growth (includes food, fiber, fuel): 
– Derived demand for land (i.e. “trend” yield growth): 
– Shifts in supply of agricultural land
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making? 
See Technical Appendix to: The Global Supply and Demand for Agricultural Land in 2050: 
A Perfect Storm in the Making? AAEA Presidential Address Thomas W. Hertel, Purdue 
University (https://www.gtap.agecon.purdue.edu/resources/download/5115.pdf)

Global 
Food, Fiber & 
Fuel 
Production
Farm
land 
Non Land 
Inputs
Investments in 
Ag. R&D
Population, 
income & 
energy prices
Productivity 
Trends
Demand 
Growth
Climate: 
Temp, Precip
and CO2
Competing 
land uses
THEORETICAL FRAMEWORK (CONT)
Ecosystem 
Services

THEORETICAL FRAMEWORK (CONT)
•
LONG RUN CHANGE IN FOOD PRICES AND AGRICULTURAL LAND
IS GOVERNED BY 3 KEY ECONOMIC RESPONSES: 
– Demand response (price elasticity of food demand): 
– Extensive margin of land use (land supply elasticity): 
– Intensive margin of land use (elasticity of substitution 
between land and non-land inputs)
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making? 
See Technical Appendix to: The Global Supply and Demand for Agricultural Land in 2050: 
A Perfect Storm in the Making? AAEA Presidential Address Thomas W. Hertel, Purdue 
University (https://www.gtap.agecon.purdue.edu/resources/download/5115.pdf)

Global 
Food, Fiber & 
Fuel 
Production
Farm
land 
Non Land 
Inputs
Investments in 
Ag. R&D
Population, 
income & 
energy prices
Productivity 
Trends
Demand 
Growth
Climate: 
Temp, Precip
and CO2
Competing 
land uses
THEORETICAL FRAMEWORK (CONT)
Ecosystem 
Services

THEORETICAL FRAMEWORK (CONT)
•
FOOD PRICE CHANGES CAN BE EXPRESSED AS A FUNCTION OF 3 
DRIVERS AND 3 ECONOMIC RESPONSES:
•
LAND USE CHANGES CAN BE EXPRESSED AS A FUNCTION OF 3 
DRIVERS AND 3 ECONOMIC RESPONSES: 
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making? 
*
,
,
,
[(
) / (1
/
/
)]
D
S
D
S I
S E
D
S E
L
A
L
L
A
A
A
A
q




=
+ −
+
+
*
,
,
(
) / (
)
D
S
D
S I
S E
D
A
A
L
L
A
A
A
p



= + −
+
+
See Technical Appendix to: The Global Supply and Demand for Agricultural Land in 2050: 
A Perfect Storm in the Making? AAEA Presidential Address Thomas W. Hertel, Purdue 
University (https://www.gtap.agecon.purdue.edu/resources/download/5115.pdf)

THEORETICAL FRAMEWORK (CONT)
• LAND USE DEPENDS ON RELATIVE, NOT ABSOLUTE, SIZE OF
INTENSIVE AND EXTENSIVE MARGINS
• LARGER DEMAND- AND INTENSIVE-SUPPLY ELASTICITIES SERVE
TO DIMINISH DEMANDS ON BIOPHYSICAL SYSTEM
• WHAT IF IGNORE ECONOMIC RESPONSES (A PURELY
BIOPHYSICAL ANALYSIS)?
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making? 
*
,
,
,
[(
) / (1
/
/
)]
D
S
D
S I
S E
D
S E
L
A
L
L
A
A
A
A
q




=
+ −
+
+

THEORETICAL FRAMEWORK IN SIMPLE
CROP DEMAND
•
CROP DEMAND FOR FOOD, FIBER AND FUEL FROM AGRICULTURE IS
DEFINED BY TWO KEY COMPONENTS:
– Exogenous % shocks (e.g., population, biofuels): 
– Endogenous (price-sensitive) component: 
•
•
KEY EQUATIONS IN SIMPLE
– Per Capita Commodity Demand 
p_QPC(i,y) =   EOP(i,y) * p_P(i,y)  + EINC(i,y) * p_INC_PC(y)
– Regional Commodity Demand 
p_QCONS(i,y) = p_QPC(i,y) + p_POP(y)
– Crop demand and supply balance 
sum(g, REG_GEO, QCROPg(g)) = sum(y,REG_INC, QCRPFEED(y) 
+ QCRPFOOD(y) + QCONS("Crops",y)) + QCRPBIOF
D
A

A
D
A p

−
D
A
A
D
A
D
A
p
q

+
−
= 

THEORETICAL FRAMEWORK IN SIMPLE
CROP DEMAND
Price of
Crop
Per Capita Quantity of 
Crop
0
P*
Q*
• Given price level P*, 
consumers purchase Q* 
quantity of food
• E_QPC #  Per Capita 
Commodity Demand  #
• p_QPC(i,y) =   EOP(i,y) * 
p_P(i,y) + EINC(i,y) * 
p_INC_PC(y)

THEORETICAL FRAMEWORK IN SIMPLE
CROP DEMAND GIVEN ENDOGENOUS PRICES
• Market price falls to  P**
• Consumers purchase more food: Q*
• In lower case (% chng) notation: 
0
P*
Q*
P
Q
P**
Q**
−𝜂𝐴
𝐷reflects slope:
sensitivity of demand to price; steeper demand is less 
responsive to price, smaller 𝜂𝐴
𝐷
D
D
A
A
A
q
p

= −
p_QPC(i,y) =   EOP(i,y) * p_P(i,y) + 
EINC(i,y) * p_INC_PC(y)

ECONOMETRIC EVIDENCE ON LONG RUN FOOD
DEMAND RESPONSE TO PRICE
•
Consumers take time to adjust; 
how much would demand adjust 
to permanently higher prices?
•
International cross-section studies 
use ICP data – designed to 
compare  cost of living across 
countries
•
Demand elasticities (abs value at 
constant income, from Mohammed 
et al., 2011):
– Range: 0.86 to 0.30 for sample of 144 
countries in 2005
– Low income avg = 0.74; high income avg
= 0.43
– Global avg in 2005 = 0.53 
– This is just ONE of the three margins of 
economic response
3
4
5
6
7
8
9
10
-0.80
-0.60
-0.40
-0.20
ln of per capita income
price elasticity of food demand
Mohammed et al (2011)
As per capita 
income rises, 
food becomes 
price inelastic
In SIMPLE, EOP becomes smaller as 
incomes increase

THEORETICAL FRAMEWORK IN SIMPLE
CROP DEMAND GIVEN POP GROWTH + FIXED PRICES
P
Q
0
P*
Q*
• If price were unchanged, 
then new consumption 
quantity is Q**
• If population increases, 
overall demand for food 
increases for each price 
level (i.e. demand curve 
shifts). Captured by 
• In our (% chng) notation:
Q**
D
A

D
A

D
D
A
A
q
= 
p_QCONS(i,y) = 
p_QPC(i,y) + p_POP(y)

Greater ELAND (land supply elasticity) implies more cropland 
available, slower rate of increase in land rents – key 
determinant of the extensive margin response
THEORETICAL FRAMEWORK IN SIMPLE
EXTENSIVE MARGIN OF CROP SUPPLY

THEORETICAL FRAMEWORK IN SIMPLE
EXTENSIVE MARGIN OF CROP SUPPLY
if ELAND is high
if ELAND is low
Q
Q*
QD*
QD
PLAND
QLAND
P
P*
Q
Q*
QS
QD*
QD
QS
P
P*
PLAND
QLAND
Cropland expansion due to increased crop demand

THEORETICAL FRAMEWORK IN SIMPLE
EXTENSIVE MARGIN OF CROP SUPPLY
if ELAND is high
if ELAND is low
Q
Q*
QD*
QD
PLAND
QLAND
P
P*
Q
Q*
QS
QD*
QD
QS
P
P*
PLAND
QLAND
Cropland expansion due to increased crop demand
*
,
,
,
/ (1
/
/
)
D
S I
S E
D
S E
L
A
A
A
A
A
q




= 
+
+
Equation E_PLANDg
(all,g,REG_GEO)
p_QLANDg(g) = ELANDg(g) * p_PLANDg(g);

THEORETICAL FRAMEWORK IN SIMPLE
INTENSIVE MARGIN OF CROP SUPPLY
Derived demand for land has two key components
•
Expansion effect (i.e. as output increases, demand for land 
increases)
•
Substitution effect (i.e. if land rents rise faster than per unit 
cost of production, demand for land decreases)

THEORETICAL FRAMEWORK IN SIMPLE
INTENSIVE MARGIN OF CROP SUPPLY
Isoquant (curved line) – tells us the combination of inputs that can produce an 
amount of output
Isocost (straight line) – tells us the combination of inputs that can produce a level 
of total cost

THEORETICAL FRAMEWORK IN SIMPLE
INTENSIVE MARGIN OF CROP SUPPLY
Regions tend to move towards away from extensive production (i.e. use of more 
land vs. non-land inputs) to intensive crop production (i.e. use more non-land therefore 
higher yields). This is the endogenous source of yield growth in the model

THEORETICAL FRAMEWORK IN SIMPLE
INTENSIVE MARGIN OF CROP SUPPLY
Expansion effect
Substitution effect
Total Change

THEORETICAL FRAMEWORK IN SIMPLE
INTENSIVE MARGIN OF CROP SUPPLY
Without intensive margin, crop production follows fixed 
combination/proportion of land and non-land inputs
No substitution effect: yields are constant since input use will 
proportionally rise with output

### Liu: Introduce gridded model theory and gridded indexing
*Source file:* `Introduce gridded model theory and gridded indexing.pdf`  ·  *type:* file

INTRODUCE GRIDDED MINI-MODEL:
THEORY AND GRIDDED INDEXING
Presentation by Jing Liu
SIMPLE-G Short Course
Purdue University, West Lafayette
September 16-20, 2019

Demand
Response
Per Capita
Demand
Population
P

Food 
Consumption
Income 
per capita
INC

Biofuels
Food Security
Food Prices
DEMAND
Crop 
Demand
Domestic Market
Global Market
SIMPLE-G: Simplified International Model of 
agricultural Prices, Land use and the Environment

Nitrogen
Land-Water 
Nitrogen
Land-Water 
Input Substitution
Input Prices
Input Supply Response
LAND

NLAND

Temp, Precip
& CO2
Investments in 
Ag. R&D
SUPPLY
Productivity 
Shocks
Crop 
Supply
CROP

Non-Land
Inputs
LW

WATER

Grid_1
Grid_k
……
SIMPLE-G: Simplified International Model of 
agricultural Prices, Land use and the Environment
𝜀𝑁𝑖𝑡𝑟𝑜

Nitrogen
Land-Water 
Nitrogen
Land-Water 
Input Substitution
Input Prices
Input Supply Response
LAND

NLAND

Temp, Precip
& CO2
Investments in 
Ag. R&D
SUPPLY
Productivity 
Shocks
Crop 
Supply
Demand
Response
Per Capita
Demand
Population
P

Food 
Consumption
Income 
per capita
INC

Biofuels
Food Security
Food Prices
DEMAND
Crop 
Demand
CROP

Non-Land
Inputs
Domestic Market
Global Market
LW

WATER

Grid_1
Grid_k
……
SIMPLE-G: Simplified International Model of 
agricultural Prices, Land use and the Environment
𝜀𝑁𝑖𝑡𝑟𝑜

Zoom into one single grid-cell k
Augmented land

SIMPLE-G mini
• Pick ten grid-cells from the 
top 10 corn producing 
states in the US:
1 KS
2 SD
3 NE
4 MN
5 IA
6 MO
7 WI
8 IL
9 IN
10 OH

Key parameters vary across grid-cells
Irrigated
Rainfed
Irrigated
Rainfed
Elast. Of land supply
1 KS
0.26
0.14
0.097
0.239
0.13
2 SD
0.25
0.12
0.126
0.322
0.7
3 NE
0.18
0.12
0.153
0.261
0.1
4 MN
0.29
0.25
0.114
0.162
0.52
5 IA
0.22
0.18
0.161
0.224
0.12
6 MO
0.26
0.2
0.119
0.179
0.35
7 WI
0.27
0.26
0.127
0.147
0.75
8 IL
0.23
0.19
0.134
0.183
0.37
9 IN
0.24
0.22
0.134
0.169
0.62
10 OH
0.21
0.18
0.168
0.203
0.14
Elast. Of sub. btw N and aug-land
Cost shr of N
Grid

Farmers minimize expenditure subject to a CES (constant 
elasticity of substitution) technology constraint
,
1
1
N land


= −
(
)
(
)
1/
min
. .
land
land
N
N
crop
crop
land
land
N
N
P
Q
P
Q
s t Q
ao
af
Q
af Q




+



=
+


Elasticity of substitution between N and land
Q_land =f(ao,af, P_crop, Q_crop, P_land; elasticity of substitution)
Q_N      =f(ao,af, P_crop, Q_crop, P_N    ; elasticity of substitution)

crop
crop
land
land
crop
crop
land
land
crop
crop
N
N
crop
crop
N
N
ao
P
af
Q
Q
ao
P
af
ao
P
af
Q
Q
ao
P
af








=









=








• ************************             QCROPgl (Y)                               
*   DERIVED DEMAND *                /      \
************************           /  ECROP \
/----------\
/            \
/              \
QAUGLANDgl (AUG)
QNITROgl (N)                      
!Demand for nitrogen fertilizer input !
E_QNITROgl
(all,g,GRID)(all,l,LTYPE)           
p_QNITROgl(g,l) + p_AFNITROg(g,l) 
= p_QCROPgl(g,l) - p_AOCROPr(GRID2REG(g),l) 
- ECROPgl(g,l)*[p_PNITROgl(g,l) - p_AFNITROg(g,l)
-p_PCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l)];
!Demand for augmented land input !
E_QAUGLANDgl
(all,g,GRID)(all,l,LTYPE) 
p_QAUGLANDgl(g,l) 
= p_QCROPgl(g,l) - p_AOCROPr(GRID2REG(g),l)
- ECROPgl(g,l)*[p_PAUGLANDgl(g,l) 
-p_PCROPgl(g,l) - p_AOCROPr(GRID2REG(g),l)];

• ************************             QCROPgl (Y)                               
*       SUPPLY         *            /      \
************************           /  ECROP \
/----------\
/            \
/              \
QAUGLANDgl (AUG)
QNITROgl (N)                      
!Supply of nitrogen fertilizer, by region !
E_QNITROr (all,r,REG) 
p_QNITROr(r) = ENITROr(r) * p_PNITROr(r);
!Price indices !
E_PAUGLANDgl
(all,g,GRID)(all,l,LTYPE) 
p_PAUGLANDgl(g,l) 
= SHR_OinAUGgl(g,l) * p_PNLANDgl(g,l) 
+ SHR_LinAUGgl(g,l) * p_PLANDgl(g,l) 
+ SHR_WinAUGgl(g,l) * p_PWATERgl(g,l)  ;

• *************************            QCROPgl (Y)                               
* ZERO PROFIT CONDITION *            /      \
*************************           /  ECROP \
/----------\
/            \
/              \
QNITROgl (N) 
QAUGLANDgl (AUG)
!Alternative form of zero profit condition !
E_QCROPgl
(all,g,GRID)(all,l,LTYPE) 
P_QCROPgl(g,l)   
= SHR_NITROgl(g,l) * p_QNITROgl(g,l) 
+ SHR_NLANDgl(g,l) * p_QNLANDgl(g,l) 
+ SHR_LANDgl(g,l)  * p_QLANDgl(g,l) 
+ SHR_WATERgl(g,l) * p_QWATERgl(g,l) 
+ p_AOCROPr(GRID2REG(g),l);

Start with 15 SIMPLE regions

Start with 15 SIMPLE regions
Disaggregate the continental US 
to 5 arcmin scale

N application rate
Unit: kg/ha
Rainfed land
Unit: 1000 ha
Irrigated land
Unit: 1000 ha

Mapping from grids to regions

……
! Declaration of mapping from grid to reg!
Mapping GRID2REG from GRID to REG;
Read GRID2REG from file GRIDSETS header "MAP1";
! Additional fertilizer cost ($/kg of N use) = 
Leaching intensity (kg of leaching / kg of N use) * Leaching 
tax ($/kg of leaching) !
Formula&Equation (LEVELS) E_PNITROgl (all,g,GRID)(all,l,LTYPE)  
PNITROgl(g,l) = PNITROr(GRID2REG(g)) +                     
LEACHINTgl(g,l) * NLTAXr(GRID2REG(g));

### Baldos: Market Segmentation 09-04-2019
*Source file:* `Market Segmentation 09-04-2019 .pptx`  ·  *type:* file

### Slide 1
Market Segmentation 
in SIMPLE model
Presentation by Uris Baldos
Purdue University

### Slide 2
Our world is interconnectedSwarm of airplanes in the sky…

### Slide 3
Our world is interconnectedThrongs of cargo ships at sea…

### Slide 4
Rise of international tradeTotal Value of Merchandise Trade

### Slide 5
In the 21st century the world economy is becoming more integrated
Expect continued growth in international trade
Regional trade agreements - while agriculture follows a slower path, reform eventually scheduled
Improvements in trade facilitation (e.g. streamlined processing, infrastructure for exports and imports)

Integration of developing countries into private sector global food supply chains

### Slide 6
Differentiation of domestic and international markets on both demand and supply sides
Crop Demand
Global Market
Domestic Markets
Crop Supply

### Slide 7
Differentiation of domestic and international markets on both demand and supply sides
Crop Demand
Global Market
Domestic Markets
Crop Supply

### Slide 8
Integrated vs. Segment Markets
Under Segmented markets
Not all producers can export to global market due to trade costs
Import tariffs and export taxes
Transportation and insurance costs
Time for transporting from farm to market
Consumer preferences for crops produced in different regions

With Integrated market, we ignore these =>single global price for crops

### Slide 9
Data / parameter needs for implementing segmented markets in SIMPLE
Taken from outside sources
Shares of domestic and global consumption and purchase shares from GTAP; these play an important role in differentiating the extent of integration

Parameter governing substitution between local and global crops are the same (ESUB=3)

### Slide 10
Extent of market penetration varies greatly by region
Source: Authors calculations, as reported in Hertel and Baldos (2016) based on FAO and GTAP data bases circa 2006. Share of supply sold to international markets and share of demand purchased from international markets

### Slide 11
Extent of market penetration determines world price transmission to local prices
Given a one percent rise in world prices, how much do Domestic prices rise?

### Slide 12
Revisiting (and Re-writing) History: 1961-2006

### Slide 13
Source: Hertel and Baldos (2016) under segmented markets and historical data from FAOSTAT (2014) and World Bank GEM Database (2014)
Revisiting History: 1961-2006SIMPLE Historical Validation

### Slide 14
Source: Hertel and Baldos (2016) under segmented markets and historical data from FAOSTAT (2014) and World Bank GEM Database (2014)
Revisiting History: 1961-2006SIMPLE Historical Validation

### Slide 15
Source: Hertel and Baldos (2016) under segmented markets and historical data from FAOSTAT (2014) and World Bank GEM Database (2014)
Revisiting History: 1961-2006SIMPLE Historical Validation

### Slide 16
Drivers of change include: Population, Per capita income & Ag. Productivity as well as growth in SSA rural labor and irrigation investments in South and Southeast Asia
Revisiting History: 1961-2006SIMPLE Historical Validation – Regional Output
[Speaker notes] Segmented markets critical in capturing broad patterns of output expansion by region

### Slide 17
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets
[Speaker notes] North America experienced faster than average TFP growth, and slower than 
	average population growth. Thus, despite somewhat faster income 
	growth, Therefore, output would have been larger under 
	integrated markets: (more exports).

### Slide 18
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets
[Speaker notes] North America experienced faster than average TFP growth, and slower than 
	average population growth. Thus, despite somewhat faster income 
	growth, Therefore, output would have been larger under 
	integrated markets: (more exports).

### Slide 19
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets
[Speaker notes] North America experienced faster than average TFP growth, and slower than 
	average population growth. Thus, despite somewhat faster income 
	growth, Therefore, output would have been larger under 
	integrated markets: (more exports).

### Slide 20
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets
[Speaker notes] East Asia (dominated by China) experienced faster than average TFP growth – 
	suggests more rapid output/export growth under integrated markets
However, relative rate of income growth was even faster, 
	so imports would have risen faster under integrated markets
Therefore output growth would have been less rapid under integrated markets

### Slide 21
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets

### Slide 22
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets
[Speaker notes] North America experienced faster than average TFP growth, and slower than 
	average population growth. Thus, despite somewhat faster income 
	growth, Therefore, output would have been larger under 
	integrated markets: (more exports).

### Slide 23
Historical Counterfactual: 1961-2006Understanding the impact of integrated markets

### Slide 24
Future Projection: 2006-2050

### Slide 25
Looking forward to 2050: Demand-side drivers are changing
[Speaker notes] Brackets as in MIT talk here again.

### Slide 26
Looking forward to 2050: Demand-side drivers are changing
[Speaker notes] Brackets as in MIT talk here again.

### Slide 27
Regional output pattern under market segmentation: 2006-2050

### Slide 28
Regional output pattern under market segmentation: 2006-2050
SSA now amongst fastest growing regions due to hi pop growth.
In China, output growth is much slower due to flat pop

### Slide 29
Regional output pattern with full market integration: 2006-2050

### Slide 30
Regional output pattern with full market integration: 2006-2050
SSA imports food since domestic market is not competitive (low productivity)
With fully integrated markets, China produces more and sells in the world market

### Slide 31
Impact of policies are different under segmented vs integrated markets: 2050 with vs without policy

### Haqiqi: Parameter Estimation and Validation_2019-09-15
*Source file:* `Parameter Estimation and Validation_2019-09-15.pdf`  ·  *type:* file

PARAMETER ESTIMATION AND
VALIDATION
Iman Haqiqi
SIMPLE-G Short Course
Purdue University, West Lafayette
September 16-20, 2019

VALUE OF WATER
• Approach 1:
• Fixed expenditure share
• Approach 2:
• GTAP Water Data Base v1
• Approach 3:
• Revenue & Expenditure estimation

(1) FIXED EXPENDITURE SHARE
• Benefits:
• Useful where limited information is available 
• It shows higher value for water where irrigated yield is higher 
• Limitations:
• It does not consider the opportunity cost of land (rainfed)

(2) GTAP WATER V1
• Using irrigated-rainfed yield gap
• Based on GTAP-E
• The general form:
PWATER * QWATER = QLANDirr *(Yield_irr – Yield_rfd)
• Benefits:
• Considering the opportunity cost of land
• Calculated for the world at 5 arc min
• Limitations:
• Not corn-equivalent!

(3) THE NEW DATA BASE OF IRRIGATED AGRICULTURE
• Extending GTAP Water
• Considering expenditure differences between rainfed and irrigated
• Considering national data and grid cell specific information
• Statistically estimated parameters
• Cost structure depends on:
• Water per land, energy per water, N per land, chemicals per land, etc.
• Domestic prices of energy, labor, capital (including tax/subsidy/support)
• Limitations:
• To be published!

PARAMETERS: CET RAINFED-IRRIGATED
• For Simple-G-US:
• Statistically estimated the CET transformation elasticity 
• Using USDA county-level information on:
• Irrigated / rainfed area
• Irrigated / rainfed rent
• Clustered by water laws
• (Qland_irr/Qland_rfd) = τ * (Pland_irr/Pland_rfd)

PARAMETERS: WATER SUPPLY ELASTICITY
• Water supply at each grid cell 
• is limited by hydrological constraints 
• We assume a Fréchet type function for water supply
• where,
• 𝜎, 𝛼, 𝜀, 𝜅are shape parameter, asymptote, location of minimum, and scale 
parameter respectively




−




−
−
=
PW
e
QW

+
-
Restricting US groundwater withdrawal:
production will move production
8
237 
(458)
406 
584 
38 
122 
139 
37 
593 
United
States
(East)
United
States
(West)
Europe
Latin
America
China
South
Asia
Rest of
Asia
M. East &
N. Africa
Sub
Saharan
Africa
1000 hectare

PARAMETERS: AGGREGATION TO NATIONAL SUPPLY
Rest of the 
world

EXAMPLE: IMPACTS OF WATER RESTRICTION IN THE
WESTERN US ON QCROP

VALIDATION: CHANGE IN IRRIGATED AREA
PROJECTED BY SIMPLE-G-W (LEFT, IN 1000 HA) 
REPORTED BY USDA (RIGHT).

### Baldos: PB2 GLASS for NPC-08-2018
*Source file:* `PB2 GLASS for NPC-08-2018.pdf`  ·  *type:* file

AGRICULTURAL PRODUCTIVITY GROWTH
FOR LONG RUN SUSTAINABILITY
Presented by Uris Lantz Baldos 
In collaboration with Thomas Hertel

OUTLINE
U.S. FARM OUTPUT AND FARM PRODUCTIVITY
U.S. FARM PRODUCTIVITY AND PUBLIC R&D SPENDING
GAINS FROM R&D SPENDING: FUTURE PROJECTIONS

U.S. FARM OUTPUT AND FARM PRODUCTIVITY: 
SOURCE OF GROWTH
Farm
Productivity 
Growth 
Farm 
Input
Use
Growth
Farm Output Growth

U.S. FARM OUTPUT AND FARM PRODUCTIVITY: 
2015 VS 1965
0
50
100
150
200
250
Farm Productivity
Farm Input Use
Farm Output
2015
1965
USDA-ERS (2017) Agricultural Productivity in the U.S.
https://www.ers.usda.gov/data-products/agricultural-productivity-in-the-us/

U.S. FARM OUTPUT AND FARM PRODUCTIVITY: 
2015 VS 1965
0
50
100
150
200
250
Farm Productivity
Farm Input Use
Farm Output
2015
1965
226
94
220
USDA-ERS (2017) Agricultural Productivity in the U.S.
https://www.ers.usda.gov/data-products/agricultural-productivity-in-the-us/

U.S. FARM OUTPUT AND FARM PRODUCTIVITY: 
SOURCE OF GROWTH
Farm
Productivity 
Growth 
Farm 
Input
Use
Growth
Farm Output Growth
Applied Inputs
•
Labor and Machineries
•
Seeds, Fertilizer and 
Pesticides
•
Energy
Land
Technology
Economic Policies
Growing Conditions

U.S. FARM OUTPUT AND FARM PRODUCTIVITY: 
TECHNOLOGY LIFE CYCLE
Time
Farm Output Benefits
Maturity
Funding & 
Investment
(Public R&D)

U.S. FARM OUTPUT AND FARM PRODUCTIVITY: 
TECHNOLOGY LIFE CYCLE
Time
Farm Output Benefits
Years 11-23 
(45% of Gains)
Years 1-5 
(<1% of Gains)
Years 6-10 
(5% of Gains)
Year 24-42 
(44% of Gains)
1950
1960
1970
1980
1990
2000
Output Gains from 
U.S. Public Agricultural R&D Investments in Year 1950
Baldos, U. L. C., Viens, F. G., Hertel, T. W., & Fuglie, K. O. (2018). 
R&D Spending, Knowledge Capital, and Agricultural Productivity Growth: A Bayesian Approach. AJAE.

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING: GAINS FROM R&D
Drivers excluding Public R&D
USDA-ERS (2017) Agricultural Productivity in the U.S.
https://www.ers.usda.gov/data-products/agricultural-productivity-in-the-us/

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING: GAINS FROM R&D
Drivers excluding Public R&D
Public R&D
50% of output gains over 1950-2010
could be linked to U.S. Public R&D Inv.

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING: GAINS FROM R&D
Drivers excluding Public R&D
Public R&D
After 1980
Public R&D Before 1980
40% of output gains over 2001-2010
could be linked to
U.S. Public R&D Inv. after 1980

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING
Huffman, W. E., & Evenson, R. E. (2006). Science for agriculture: A long-term perspective. 
USDA-ERS. (2015) Agricultural Research Funding in the Public and Private Sectors. 
http://www.ers.usda.gov/data-products/agricultural-productivity-in-the-us.aspx

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING
Huffman, W. E., & Evenson, R. E. (2006). Science for agriculture: A long-term perspective. 
USDA-ERS. (2015) Agricultural Research Funding in the Public and Private Sectors. 
http://www.ers.usda.gov/data-products/agricultural-productivity-in-the-us.aspx

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING
Heisey and Fuglie (2018) "Agricultural Research Investment and Policy Reform in High-Income 
Countries". USDA-ERS Report 249.

U.S. FARM PRODUCTIVITY AND PUBLIC R&D 
SPENDING
Clancy, M., Fuglie, K. & Heisey, P. U.S. Agricultural R&D in an Era of Falling Public Funding. 
Amber Waves (2016).

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Greater TFP Growth - 1.5% yr
Ave. increase in Public RD 
spending of  1.1 B USD / yr over 
2020-2050 
Baseline TFP - 1.2% yr
Historical TFP Growth (1981-10)
Projections from SIMPLE-G using Global Population, Income, US Biofuels as other drivers

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Greater TFP Growth - 1.5% yr
Ave. increase in Public RD 
spending of  1.1 B USD / yr over 
2020-2050 
Baseline TFP - 1.2% yr
Historical TFP Growth (1981-10)
Projections from SIMPLE-G using Global Population, Income, US Biofuels as other drivers

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Projections from SIMPLE-G using Global Population, Income, US Biofuels as other drivers

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Other drivers: Global Population, Income, US Biofuels

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Other drivers: Global Population, Income, US Biofuels

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Other drivers: Global Population, Income, US Biofuels

GAINS FROM R&D SPENDING: 
FUTURE PROJECTIONS
Higher productivity growth 
results in slower water use…
… and cropland 
reduction

SUMMARY
• PAST GAINS IN U.S. AGRICULTURAL OUTPUT GROWTH HAS BEEN DRIVEN BY
PRODUCTIVITY GROWTH => FUELED BY PUBLIC R&D INVESTMENTS IN
AGRICULTURE
• DECLINING U.S. PUBLIC R&D INVESTMENTS IN RECENT YEARS AND
INCREASED AGRICULTURAL R&D INVESTMENTS ABROAD COULD WEAKEN U.S. 
COMPETITIVENESS IN THE FUTURE
• INCREASED INVESTMENTS IN U.S. PUBLIC R&D INVESTMENTS IS NEEDED

### Liu: PB3 GLASS for NPC-08-2018
*Source file:* `PB3 GLASS for NPC-08-2018.pdf`  ·  *type:* file

Presented by Christopher Kucharik1, Laura 
Bowling2 and Jing Liu2
Based on collaboration with Thomas Hertel2, 
Sadia Jame2 and Navin Ramankutty3
1University of Wisconsin-Madison, 2Purdue University, 3University of British Columbia
MANAGING NITRATE LEACHING
IN THE CORN BELT

•
Widespread and intensive agricultural 
production is dependent on nitrogen (N) 
fertilizer to sustain yields
•
In the Corn Belt, large amounts of nitrate 
are lost from soils, mostly attributed to corn 
production
•
Nutrients are transported through the 
Mississippi River Basin to Gulf of Mexico, 
creating ”dead zones” (hypoxia)
•
US EPA Hypoxia Task Force has suggested a 
45% reduction in N load to gulf is needed by 
2035 to reduce the dead zone size to a 
more acceptable level
•
How are we going to get there?
The Sustainability Challenge

US Nitrogen Fertilizer Applications1
1For 2006-2012 time period.  From Booth et al. 2016, Environmental Modelling & Software 85: 80 - 97

Alexander et al. 2008

0
20
40
60
80
100
120
140
160
50
70
90
110
130
150
170
0
50
100
150
200
250
300
NO3-N loss below the root zone (leaching)
Corn yield (bu/ac)
Fertilizer + Manure N (kg/ha)
Agro-IBIS used for Wisconsin continuous corn, no irrigation, sandy soils
Modeling builds our understanding of N and yield responses
Yield response
Nitrogen Loss
Optimum N rate

•
A variety of conservation 
practices have been suggested
•
Model the impacts of these 
interventions using a novel 
sustainability framework 
•
Join biophysical modeling with 
agronomic relationships  (Agro-
IBIS) to economic models of land 
use (SIMPLE-G-US)
How do we manage nitrate leaching to 
improve water quality?
Credit: DuPont Pioneer
Credit: NRCS - USDA

Nitrogen Reduction Strategies
Data compiled from field sites as part of the Iowa Nutrient Reduction 
Strategy, accessed from https://www.iasoybeans.com/

• Controlled Drainage
• Bioreactor
• Two-stage Ditch
• Managed Wetland
• Cover crops
• Nitrogen field trials
ACRE

Controlled Drainage at DPAC

Measured impacts of controlled drainage

Managed Wetlands at ACRE
subsurface 
drainage 
in
streamflow 
out
28% 
reduction in 
nitrate load

Nitrogen Rate & Cover Crops at SEPAC
0
5
10
15
20
25
30
35
40
1985 1986 1987 1988 1989
1990
1991 1992
1993 1994 1995 1996
1997
1998
1999
Nitrate-N Concentraiton in Drainage Water (mg/L)
5 m
10 m
20 m
250 lb N/acre
200 lb N/acre
Corn/soy 
with cover crop
175 lb
N/acre
155 lb
N/acre
Continuous Corn

0
20
40
60
80
100
120
140
160
50
70
90
110
130
150
170
0
50
100
150
200
250
300
NO3-N loss below the root zone (leaching)
Corn yield (bu/ac)
Fertilizer + Manure N (kg/ha)
Yield response
Nitrogen Loss
Current N rate
Reduced N rate
Leaching reduction and yield loss owing to reduced N rate

0.75
0.65
0.50
0.12
-16.65
-11.63
-8.65
-1.47
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
-18.80
-16.80
-14.80
-12.80
-10.80
-8.80
-6.80
-4.80
-2.80
-0.80
1.20
Rate reduction
Split N
Split N + Controlled
drainage
Split N + Wetland
restoration
Leaching charge ($/lb N applied)
Change in crop output (%)
130% of N price
Achieving the Hypoxia Task Force Target solely via reduced 
N rates is costly and results in sharp output reduction

0
20
40
60
80
100
120
140
160
50
70
90
110
130
150
170
0
50
100
150
200
250
300
NO3-N loss below the root zone (leaching)
Corn yield (bu/ac)
Fertilizer + Manure N (kg/ha)
Yield response
Nitrogen Loss
Current N rate
Yield and leaching response altered by managing N use

0.75
0.65
0.50
0.12
-16.65
-11.63
-8.65
-1.47
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
-18.80
-16.80
-14.80
-12.80
-10.80
-8.80
-6.80
-4.80
-2.80
-0.80
1.20
Rate reduction
Split N
Split N + Controlled
drainage
Split N + Wetland
restoration
Leaching charge ($/lb N applied)
Change in crop output (%)
22% of N price
130% of N price
Improving NUE moderates somewhat the cost of achieving 
the targeted reduction

Nitrogen Reduction Strategies
Data compiled from field sites as part of the Iowa Nutrient Reduction 
Strategy, accessed from https://www.iasoybeans.com/

Fraction of land suitable for controlled 
drainage

0.75
0.65
0.50
0.12
-16.65
-11.63
-8.65
-1.47
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
-18.80
-16.80
-14.80
-12.80
-10.80
-8.80
-6.80
-4.80
-2.80
-0.80
1.20
Rate reduction
Split N
Split N + Controlled
drainage
Split N + Wetland
restoration
Leaching charge ($/lb N applied)
Change in crop output (%)
22% of N price
130% of N price
Adding controlled drainage where feasible further 
reduces the leaching charge required

Feasible sites for wetland restoration

0.75
0.65
0.50
0.12
-16.65
-11.63
-8.65
-1.47
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
-18.80
-16.80
-14.80
-12.80
-10.80
-8.80
-6.80
-4.80
-2.80
-0.80
1.20
Rate reduction
Split N
Split N + Controlled
drainage
Split N + Wetland
restoration
Leaching charge ($/lb N applied)
Change in crop output (%)
22% of N price
130% of N price
Wetland restoration appears to be the most effective 
mitigation strategy – very limited impact on output

0.75
0.65
0.50
0.12
-16.65
-11.63
-8.65
-1.47
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
-18.80
-16.80
-14.80
-12.80
-10.80
-8.80
-6.80
-4.80
-2.80
-0.80
1.20
Rate reduction
Split N
Split N + Controlled
drainage
Split N + Wetland
restoration
Leaching charge ($/lb N applied)
Change in crop output (%)
22% of N price
130% of N price
Wetland restoration appears to be the most effective 
mitigation strategy – very limited impact on output
Even in the absence of leaching charge, comprehensive wetland restoration 
paired with improved N efficiency would still deliver a 40% reduction in N 
leaching.

While each of the policy scenarios achieves the 
same 45% aggregate reduction in N leaching, the 
spatial patterns of mitigation are quite different
More effective for Illinois, Indiana, 
and Ohio
More effective for Nebraska, 
Iowa and Minnesota 
Tons N/grid

• The relative importance of in-
field and edge-of-field 
practices varies greatly across 
states.
• In-field reduction is more 
dominant when controlled 
drainage management is 
adopted, as opposed to 
wetland restoration.
In-field reduction
Edge-of-field reduction
Cropland area contraction
Decompose total reduction into:

Limitations
• We explore ‘best case’ scenarios representing full 
implementation of conservation practices
• Only focused on N loss from corn production
• Emission of nitrous oxide not considered 
• Ecosystem loading of N yet to be evaluated

Summary of findings
• 45% N leaching reduction is feasible using different 
approaches—some more painful than others
• In-field N reductions coupled with wetland 
restoration are the most effective strategy
• Local N reduction policies can have consequences 
for national and global markets
26

### Haqiqi: Production Structure_2019-09-15
*Source file:* `Production Structure_2019-09-15.pdf`  ·  *type:* file

PRODUCTION STRUCTURE OF SIMPLE-G:
OPTIMAL MIX OF INPUTS
(land, fertilizer, water, and other inputs)
Iman Haqiqi
SIMPLE-G Short Course
Purdue University, West Lafayette
September 16-20, 2019

Outline 
• What are the inputs of production at each grid cell
• What is a production function
• Nested production functions
• CES: constant elasticity of substitution
• The “tree structure”
• Key concepts
• Mathematical representations

Inputs and outputs?
Ecosystem
Agriculture 
Input Markets
(Labor, Capital, Fertilizer, etc)
Output Markets
(Crops)

Why gridded production is important?
• Change in land, water and fertilizer use depends on production 
function at each location. We need gridded production to find 
• Gridded demand for inputs
• Gridded supply of outputs
• The parameters and the functional form will determine the response 
of each grid cell to ecological or economic shocks. 
• It also shows the possible changes in technology of production.

What is a production function?
• Production function (or production technology) is a mathematical 
equation that shows the technological relation between quantities of 
inputs and quantities of output
• This function combined with given market prices of inputs and 
output(s) will determine the optimum amount of input demand and 
output supply.
• What is the functional form of the production technology?
• We assume a Nested CES (constant elasticity of substitution) function.

Key concepts: elasticity
• Supply elasticity:
• Substitution elasticity:
• Demand elasticities
• Price elasticity of demand:
• Income elasticity of demand:

Key concepts (cont.)
• Constant elasticity of substitution production function 
• Separability; e.g.
• optimal mix of land and water is invariant to price of other inputs
• elasticity of substitution between water/land and other inputs is the same
• Relative prices: 
• Same change in all the prices => no change in the optimal mix of inputs

The simplest form!
• Application: 
• land use changes
• total factor productivity shocks
• land productivity shocks
• Requirements: 
• Gridded substitution elasticity on 
land and non-land
• Gridded land supply elasticity 
QCROP
QLAND
QNLAND
ECROP

Adding nitrogen fertilizer
• + Application: 
• Nitrogen fertilizer productivity 
shocks
• Nitrate/leaching tax/subsidy/cap
• +Requirements: 
• Gridded substitution elasticity of 
nitrogen and other inputs
• Parameter revisions 
QCROP
QNITRO
QNLAND
QLAND

Adding irrigation
• + Application: 
• Irrigation productivity shocks
• irrigation tax/subsidy/cap
• Water scarcity
• +Requirements: 
• Value of irrigation
• Gridded substitution elasticity of 
water and other inputs
• Parameter revisions 
QCROP
QNITRO
QNLAND
QLAND
QWATER

Adding irrigation technology
• + Application: 
• withdrawal productivity shocks
• withdrawal tax/subsidy/cap
• +Requirements: 
• Value of water/ equipment
• Gridded substitution elasticity of 
water and other inputs
• Parameter revisions 
QCROP
QNITRO
QNLAND
QLAND
QWWDRL
QWEQPT

Adding water sources
• + Application: 
• Water availability shock by source
• groundwater tax/subsidy/cap
• +Requirements: 
• Value of water by source
• Gridded substitution elasticity 
between water sources
• Parameter revisions 
QCROP
QNITRO
QNLAND
QLAND
GRDWAT
QWEQPT
SRFWAT

************************
QCROPgl
* TREE STRUCTURE *      
/      \
************************
/        \
/----------\
<--ces
/  ECROPgl
\
/              \
QAUGLANDgl
QNITROgl
/      \
/--------\
<--ces
/EAUGLANDgl\
/            \
/              \
QNLANDgl
QLANDWTRgl
/       \
/         \
/-----------\
<--ces
/  EIRRIGgl
\
/               \
QLANDgl*
QLANDgl
QWATERgl

Top nest composite
demand for NITRO
Equation E_QNITRO
p_QNITRO
= p_QCROP
- ECROP * [p_PNITRO- p_PCROP];
*** Relative price is important
QCROP
QNITRO
QAUGLAND
ECROP

Top nest composite
with g,l index
Equation E_QNITROgl
(all,g,GRID)(all,l,LTYPE) 
p_QNITROgl(g,l)
= p_QCROPgl(g,l)
- ECROPgl(g,l) * [p_PNITROgl(g,l) - p_PCROPgl(g,l)];
QCROPgl
QNITROgl
QAUGLANDgl
ECROPgl

Top nest composite
demand for QAUGLAND
Equation E_QAUGLANDgl
(all,g,GRID)(all,l,LTYPE) 
p_QAUGLANDgl(g,l) 
= p_QCROPgl(g,l) 
- ECROPgl(g,l)* [p_PAUGLANDgl(g,l) - p_PCROPgl(g,l)] ;
QCROPgl
QNITROgl
QAUGLANDgl
ECROPgl

Augmented land nest: 
demand for QNLAND
Equation E_QNLANDgl
(all,g,GRID)(all,l,LTYPE) 
p_QNLANDgl(g,l)  
= p_QAUGLANDgl(g,l)
- EAUGLANDgl(g,l) * [p_PNLANDgl(g,l)   - p_PAUGLANDgl(g,l) ]
;
QAUGLANDgl
QLANDWTRgl
QNLANDgl
ECROPgl

Land-water nest: 
demand for QLAND
Equation E_QLANDgl
(all,g,GRID)(all,l,LTYPE) 
p_QLANDgl(g,l)  
= p_QLANDWTRgl(g,l) 
- EIRRIGgl(g,l) * [p_PLANDgl(g,l) - p_PLANDWTRgl(g,l)];
QLANDWTRgl
QWATERgl
QLANDgl
EIRRIGgl

Land-water nest
with the composite price index
Equation E_QLANDgl
(all,g,GRID)(all,l,LTYPE) 
p_QLANDgl(g,l)  
= p_QLANDWTRgl(g,l) 
- EIRRIGgl(g,l) * [p_PLANDgl(g,l) - p_PLANDWTRgl(g,l)];
Equation E_PLANDWTRgl
(all,g,GRID)(all,l,LTYPE) 
p_PLANDWTRgl(g,l) 
= SHR_LinLWgl(g,l) * p_PLANDgl(g,l) 
+ SHR_WinLWgl(g,l) * p_PWATERgl(g,l)  ;
QLANDWTRgl
QWATERgl
QLANDgl
EIRRIGgl

Technological change variables
• p_AOCROPr(r,l): input-neutral eff. index in Crop prod. by reg & ltype
• p_AFNITROg(g,l): nitrogen eff. index in crop prod. by reg & ltype
• p_AFAUGLANDr(r,l): augmented land eff. index in crop prod. by reg & ltype
• etc.

Technological change variables: 
example
• p_QNITROgl(g,l) + p_AFNITROg(g,l)
= p_QCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l)
- ECROPgl(g,l)* [p_PNITROgl(g,l) - p_AFNITROg(g,l)
-
p_PCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l)];
• When AFNITROg increases it has 3 major impacs:
• reduces demand for NITRO at constant prices
• reduces the effective price of the NITRO and thus encouraging substitution
• lowers the cost of production thus encouraging expansion

How an efficiency shock works
• An increase in nitrogen fertilizer 
productivity
• The farmers need less fertilizer 
to produce the same output
• The price may decline and 
motivates a rebound
PNITRO
QNITRO
Demand2
Supply 
Demand1

Wrap-up
• Production functions are from the nested-CES family
• Key assumptions are:
• separability of inputs
• constant elasticity of substitution within nests
• Can also shock technical change

Thanks!

### Baldos: SIMPLE-G Data 09-04-2019
*Source file:* `SIMPLE-G Data 09-04-2019.pdf`  ·  *type:* file

SIMPLE-G DATA WORKFLOW
Presentation by Uris Baldos
Purdue University

KEY SOURCES OF DATA
• UN FAOSTAT
• EARTHSTAT
• GLOBAL ADMINISTRATIVE DATABASE
• GTAP DATABASE
• MODEL PARAMETERS
• MODEL SHOCKS FOR PROJECTIONS
Hertel, T. W. (2011). The Global Supply and Demand for Land in 2050: A Perfect Storm in the Making?

DATA ON CROP PRODUCTION
•
UN FAOSTAT
Updated Quarterly
Population (country, year)
GDP (country, year)
Arable land + permanent 
croplands (country, year) 
Crop data (175 crops)
- Output (crop, country, 
year) 
- Harvested area (crop, 
country, year)
• http://www.fao.org/faost
at/en/

DATA ON CROP PRODUCTION
• EARTHSTAT                                
Not Updated
Crop data
Output (crop, grid, year 
2000)
Harvested area (crop, grid, 
year 2000//05)
• http://www.earthstat.or
g/harvested-area-yield-
175-crops/

DATA ON COUNTRY BOUNDARIES
•
Global Administrative 
Database Updated Quarterly
Country Boundaries 
https://gadm.org/download
_world.html

DATA ON COST OF PRODUCTION
•
Global Trade Analysis 
Project Database Updated 3-4 
years
Cost shares for crop, livestock 
and processed food 
production
Consumption and sales shares 
for crops by consumers and 
producers in domestic and 
global markets
https://www.gtap.agecon.pur
due.edu/databases/default.as
p

ONLINE WORKFLOW (FUTURE WORK)
•
SIMPLE-G Database 
Creation    
(Gridded, R, GEMPACK)
Data 
Connectors
Data 
Processors
Web Tools
Online 
Course
SIMPLE-G Database
*.har file
0
User Inputs
*.csv file

Enable load / publish model runs
ONLINE WORKFLOW (FUTURE WORK)
Data 
Connectors
Data 
Processors
Web Tools
Online 
Course
0
•
SIMPLE-G Tool

•
Course on Global Sustainability
Link published model runs to course
Data 
Connectors
Data 
Processors
Web Tools
Online 
Course
0
ONLINE WORKFLOW (FUTURE WORK)

MODEL PARAMETERS: 
ELASTICITIES OF SUBSTITUTION
•
Muhammad et al 2011
Initial income and own-price 
elasticities for 100+ countries 
Income elasticities are linked 
to log of per capita income via 
regression. 
Regression estimates are 
adjusted to fit 2001-2006 
calibration simulation
https://www.ers.usda.gov/we
bdocs/publications/47579/76
37_tb1929.pdf?v=0

MODEL PARAMETERS: 
US CROPLAND SUPPLY ELASTICITIES
•
Villoria and Liu 2018
Gridded land supply 
elasticities for the Americas
https://www.sciencedirect.
com/science/article/pii/S02
64837717314023

MODEL PARAMETERS: 
OTHER PARAMETERS
•
CROPLAND SUPPLY ELASTICITIES - OTHER REGIONS
The MIT Emissions Prediction and Policy Analysis (EPPA) Model: Version 4 –
Adjusted land supply values
•
ELASTICITIES OF SUBSITITUTION IN CROP PRODUCTION 
Nitrogen yield response curves for US (Jing will talk about this later)
Imposed values for other regions
•
ELASTICITIES OF SUBSITITUTION IN LIVESTOCK AND 
PROCESSED FOOD PRODUCTION
Calibration experiment 2001-2006
•
NONLAND SUPPLY ELASTICITIES
"GTAP-AGR: A Framework for Assessing the Implications of Multilateral Changes 
in Agricultural Policies “ by Keeney, Roman and Thomas Hertel

MODEL SHOCKS:  POPULATION GROWTH
Population projections remain highly uncertain
World Population Prospects: The 2017 Revision

MODEL SHOCKS:  POPULATION GROWTH
Population growth is fastest in Africa
World Population Prospects: The 2017 Revision

MODEL SHOCKS:  POPULATION GROWTH
ALTERNATIVE PROJECTIONS OF POPULATION BASED ON SSPS
Sources: ISSP Database – IIASA, OECD (2018), van der Mensbrugghe (2014)

MODEL SHOCKS:  POPULATION GROWTH
ALTERNATIVE PROJECTIONS OF POPULATION BASED ON SSPS
Samir KC,  Wolfgang Lutz
The human core of the shared socioeconomic pathways: Population scenarios by age, sex 
and level of education for all countries to 2100

MODEL SHOCKS:  INCOME GROWTH
ALTERNATIVE PROJECTIONS OF POPULATION BASED ON SSPS
Sources: ISSP Database – IIASA, OECD (2018),
van der Mensbrugghe (2014)

MODEL SHOCKS:  CROP TFP GROWTH
HISTORICAL CHANGES IN AGRICULTURAL TFP GROWTH
Sources: Fuglie (2018) R&D Capital, R&D Spillovers, and Productivity 
Growth in World Agriculture. AEPP.  Volume 40, Issue 3

MODEL SHOCKS:  CROP TFP GROWTH
AGRICULTURAL TFP GROWTH FROM R&D SPENDING
Sources: Baldos, Fuglie, Hertel(2019) The Research Cost of Adapting Agriculture to 
Climate Change: A Global Analysis to 2050. Agricultural Economics.  Accepted
Time
R&D Spending Impacts [0,1]
Years 11-23 
(45% of Gains)
Years 1-5 
(<1% of Gains)
Years 6-10 
(5% of Gains)
Year 24-42 
(44% of Gains)
1950
1960
1970
1980
1990
2000

MODEL SHOCKS:  CROP TFP GROWTH
AGRICULTURAL TFP GROWTH FROM R&D SPENDING
Sources: Baldos, Fuglie, Hertel(2019) The Research Cost of Adapting Agriculture to 
Climate Change: A Global Analysis to 2050. Agricultural Economics.  Accepted
0
10
20
30
40
50
60
70
80
C AMER
S AMER
S ASIA
SE ASIA
NE ASIA
W ASIA N AFRICA
SSA
S AFRICA OCEANIA N AMER
ASIA DC W EURO
TRAN
R&D investment TFP growth (% 2006-2050) 
Ag. TFP growth: 2006-2050 0.5 % p.a.
Ag. TFP growth: 2006-2050 1 % p.a.
Ag. TFP growth: 2006-2050 2 % p.a.

• FUTURE CROP YIELDS PRODUCED BY THE AGRICULTURAL
Model Intercomparison and Improvement Project (AgMIP).
• 7 Crop Models.
• 5 Global General Circulation Models.
• 5 Representative Climate Pathways (RCPs).
• CO2 Fertilization and irrigation.
• 12 Crops.
• All the combinations ran from 1971 to 2099.
• + 36,000 0.50 x 0.50 grids with crop yields.
• EASY ACCESS TO DATA FROM AGMIP’S ESTIMATED
HISTORICAL AND FUTURE CHANGES IN YIELDS UNDER
CLIMATE CHANGE SCENARIOS
•
HTTPS://MYGEOHUB.ORG/TOOLS/AGMIP
Gridded 
Crop 
Models
General 
Circulation 
Models
MODEL SHOCKS: 
CLIMATE CHANGE YIELD IMPACTS

Find data
Visualiz
e
Aggregate data (e.g., by 
countries or regions)
AGMIP TOOL
MODEL SHOCKS: 
CLIMATE CHANGE YIELD IMPACTS

### Liu: SIMPLE-G-CS parameters
*Source file:* `SIMPLE-G-CS parameters.pdf`  ·  *type:* file

SIMPLE-G-CS PARAMETERS
EMULATORS AND ELASTICITIES
Jing Liu
SIMPLE-G Short Course
Purdue University, West Lafayette
September 16-20, 2019

Parameters at the grid-cell level
• Cost share
• Nitrogen fertilizer
• Elasticity of substitution between
• nitrogen and augmented land
• water and land
• Price elasticity of input supply
• Cropland 
• Water
• Nitrate leaching response
• Quadratic function of N application rate

How are the parameters estimated?
• Based on biophysical emulators
• Use Agro-IBIS to derive the elasticity of substitution and leaching response 
• Econometrically estimated
• Use fine-resolution biophysical and socio-economic data to estimate cropland 
supply elasticity

Kucharik, 2003, Earth Interactions
THMB
Terrestrial Hydrology Model with Biogeochemistry
Agro-IBIS: 
A Comprehensive Model of 
Land Surface & Ecosystem 
Processes

0
20
40
60
80
100
120
140
160
50
70
90
110
130
150
170
0
50
100
150
200
250
300
NO3-N loss below the root zone (leaching)
Corn yield (bu/ac)
Fertilizer + Manure N (kg/ha)
Agro-IBIS used for Wisconsin continuous corn, no irrigation, sandy soils
Modeling builds our understanding of N and yield responses
Yield response
(Gompertz)
Nitrogen Loss
(Quadratic)

Gompertz production function
(
)
exp(
)
N
f N
a
b
c
=

−

Substitutability between land and fertilizer σLN
Can be computed from the Gompertz yield function fitted to AgroIBIS outputs
σLN varies by grid cell
'( )[ ( )
'( )]
''( ) ( )
LN
f
n
f n
nf
n
nf
n f n

−
=
−

Substitutability between land and water σLW
Can be computed from the quadratic yield function fitted to AgroIBIS outputs
σLw varies by grid cell
'( )[ ( )
'( )]
''( ) ( )
LW
f
w
f w
wf
w
wf
w f w

−
=
−

• Adjusted cost shares of nitrogen 
• Scaled and truncated to 5%～15%
,
,
,
N g
N
shr g
crop g
crop
Q
P
N
Q
P
=


Cropland supply elasticity 
• Larger number indicates more elastic/responsive cropland supply
• Predict land use change when combined with changes in land returns
• 5 arcmin grid level 
%
_
%
_
cropland
area
elasticity
land
returns
=

Elasticities estimated from a spatial 
regression model 
Pr(
)
(
_
;
_
)
cultivation
f market
access land
quality
=
_
Pr
land
response
ma


=

Spatial data
Market access (Verburg et al. 2011) as a proxy for land 
profitability

_
_
cropland
area
land
returns


=

USDA data
Comparing predicted with observed area change can be a 
validation of η and the model.

Observed cropland expansion 2008-2012. (Lark et al., ERL 2015)

!Demand for nitrogen fertilizer input !
E_QNITROgl
(all,g,GRID)(all,l,LTYPE)           
p_QNITROgl(g,l) + p_AFNITROg(g,l) 
= p_QCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l) 
- ECROPgl(g,l)* [p_PNITROgl(g,l) - p_AFNITROg(g,l)
-
p_PCROPgl(g,l)  - p_AOCROPr(GRID2REG(g),l)] ;
Demand for nitrogen at the grid-cell level
A larger elasticity of substitution indicates less responsive change in the demand for nitrogen.

The importance of adopting heterogeneous 
parameters

### Haqiqi: Water Supply and Demand_2019-09-15
*Source file:* `Water Supply and Demand_2019-09-15.pdf`  ·  *type:* file

WATER SUPPLY AND DEMAND
ECONOMICS OF WATER RESOURCES
Iman Haqiqi
SIMPLE-G Short Course
Purdue University, West Lafayette
September 16-20, 2019

GOALS
• WE WILL TALK ABOUT:
– What determines the water demand for irrigation
– How to construct economic supply of water
– Long run equilibrium withdrawal
– How to interpret the “price of water”
– How to shock water supply
– Spatial linkages in water demand

IRRIGATION IN THE US
Irrigation extent varies over time mainly due to conversion 
to/from dryland.

WATER WITHDRAWAL IN THE US
Total water use has been stable in the US in past 3 decades.

•
************************             QCROPgl (Y)            
* PRODUCTION STRUCTURE *            /      \
************************           /        \
/----------\
/            \
/              \
QAUGLANDgl (AUG)
QNITROgl (N)   
/      \
/--------\
/          \
/            \
/              \
QNLANDgl (O)    QLANDWTRgl (WL) 
/     \
/       \
/---------\
/           \
/             \
QLANDgl (L)    QWATERgl (W)
\
/
/     \
\
/
/-------\
\
/
/         \
\
/
/           \
QWWDRLgl
QWEQPTgl

THEORETICAL: OPTIMIZATION
•
FARMERS MINIMIZE THE PRODUCTION COST CONSIDERING THEIR
PRODUCTION FUNCTION:
𝑚𝑖𝑛𝑖𝑚𝑖𝑧𝑒𝑃𝑁𝑖. 𝑁𝑖+ 𝑃𝐿𝑖. 𝐿𝑖+ 𝑃𝑊𝑖. 𝑊𝑖+ 𝑃𝑶𝑖. 𝑶𝑖
𝑠𝑡𝑌𝑖= 𝑓𝑖(𝑁, 𝐿, 𝑊, 𝑶)
– (Y) is the corn equivalent of all the crops produced in the grid cell. 
Production inputs are nitrogen fertilizer (N), land (L), water (W), and 
aggregate other inputs (O)
– where PNi, PLi, PWi, and POi are input prices at each grid cell i. 
– Given the output prices, equilibrium levels of Ni, Li, Wi, and Oi can be 
obtained

THEORETICAL: DEMAND FOR WATER
• AT EACH NEST THERE IS A SUBSTITUTION PARAMETER:
– It shows the possibility of changing input mix when relative 
price of inputs change
• 𝑄𝑊𝐴𝑇𝑖= 𝛽𝑖,𝑤𝑄𝐶𝑅𝑂𝑃𝑖
𝑃𝐶𝑅𝑂𝑃𝑖
𝑃𝐴𝑈𝐺𝑖
𝜎𝑖,𝑦
𝑃𝐴𝑈𝐺𝑖
𝑃𝑊𝐿𝑖
𝜎𝑖,𝑎𝑢𝑔
𝑃𝑊𝐿𝑖
𝑃𝑊𝑖
𝜎𝑖,𝑤
• WATER DEMAND DEPENDS ON:
– Extent of irrigated production
– Relative prices of inputs 
– Substitution possibilities

THEORETICAL: WATER SUPPLY
• WATER SUPPLY AT EACH GRID CELL
– is limited by hydrological constraints 
– We assume a Fréchet type function for water supply
•
WHERE,
– 𝜎, 𝛼, 𝜀, 𝜅are shape parameter, asymptote, location of 
minimum, and scale parameter respectively




−




−
−
=
PW
e
QW

THEORETICAL: WATER SUPPLY EXAMPLE
• When close to the 
asymptote, it requires big 
increase in price to 
motivate more supply
• When close to zero, small 
increase in price will lead to 
large increase in supply.
• Note: In many cases there 
is no “market price”.  The 
supply shows the change in 
cost of extraction and 
transfer.

EQUILIBRIUM: WATER AND DIAMOND!

SIMULATING POLICIES AND SHOCKS
• NEW EQUILIBRIUM DEPENDS ON:
– supply and demand responses to
• Output prices (given for grid cells)
• Change in relative input prices
– Price of N, O are given (national)
– Price of water and land are local
• Irrigation extent (local competitive practices)

WATER SCARCITY SHOCK (1A, 1B)
price
Quantity
Demand
Supply 1
Supply 2
price
Quantity
Demand
Supply 1
Supply 2

WATER SCARCITY SHOCK (1C, 1D)
price
Quantity
Demand
Supply 1
Supply 2
price
Quantity
Demand
Supply 1
Supply 2

RAINFED YIELD SHOCK (2A, 2B)
price
Quantity
Demand1
Supply 
Demand2
price
Quantity
Demand1
Supply 
Demand2

WATER SCARCITY SHOCK (3A, 3B) 
WITH IMPACT ON RAINFED
price
Quantity
D1
S1
S2
D2
price
Quantity
D1
S1
S2
D2

CODE: VARIABLES
p_QWEQPTgl(g,l) # irrig eqpt by g&l
#;
p_PWEQPTgl(g,l) # price of irrig eqpt by g&l
#;
p_QWWDRLgl(g,l) # water use by g&l
#;
p_PWWDRLgl(g,l) # price of water use by g&l
#;
p_PWATERgl(g,l)   # price of water+eqpt by g&l
#;
p_QWATERgl(g,l)   # quantity of water+eqpt by g&l #;

SUPPLY EQUATIONS
!supply of water!
E_PWWDRLgl
(all,g,GRID)(all,l,LTYPE)                       
p_QWWDRLgl(g,l)  
= EWWDRLgl(g,l) * p_PWWDRLgl(g,l) +s_QWATERg(g);
!supply of irrigation equipment etc!
E_PWEQPTgl
(all,g,GRID)(all,l,LTYPE)                       
p_QWEQPTgl(g,l)  
= EWATKLr(GRID2REG(g)) * p_PWEQPTgl(g,l) +s_QWEQPTg(g);

SUPPLY EQUATIONS: SLACK VARIABLES
!supply of water!
E_PWWDRLgl
(all,g,GRID)(all,l,LTYPE)                       
p_QWWDRLgl(g,l)  
= EWWDRLgl(g,l) * p_PWWDRLgl(g,l) +s_QWATERg(g);
!supply of irrigation equipment etc!
E_PWEQPTgl
(all,g,GRID)(all,l,LTYPE)                       
p_QWEQPTgl(g,l)  
= EWATKLr(GRID2REG(g)) * p_PWEQPTgl(g,l) +s_QWEQPTg(g);

DEMAND EQUATIONS
!Demand for water input!
E_QWWDRLgl
(all,g,GRID)(all,l,LTYPE) 
p_QWWDRLgl(g,l) 
= p_QWATERgl(g,l)
- ESUB_WKgl(g,l) * [p_PWWDRLgl(g,l) - p_PWATERgl(g,l) ] ;
!Demand for irrigation equipments!
E_QWEQPTgl
(all,g,GRID)(all,l,LTYPE) 
p_QWEQPTgl(g,l) 
= p_QWATERgl(g,l)
- ESUB_WKgl(g,l) * [p_PWEQPTgl(g,l) - p_PWATERgl(g,l) ] ;

IRRIGATION PRICE AND QUANTITY INDEX
!Quantity index for water+eqpt!
E_QWATERgl
(all,g,GRID)(all,l,LTYPE) 
p_QWATERgl(g,l) 
= ISIRRI(l)    *(p_QLANDWTRgl(g,l)
- EIRRIGgl(g,l)*[p_PWATERgl(g,l)-p_PLANDWTRgl(g,l)]);
!price index for irrigation wat+eqpt!
E_PWATERgl
(all,g,GRID)(all,l,LTYPE) 
p_PWATERgl(g,l) 
= SHR_WWinWgl(g,l) * p_PWWDRLgl(g,l) 
+ SHR_WKinWgl(g,l) * p_PWEQPTgl(g,l) ;

WATER WITHDRAWAL IN THE US
Total water use has been stable in the US in past 3 decades.

AGWATER-IDENTITY
• THIS IDENTITY SHOWS THAT TOTAL WATER WITHDRAWAL IN
EACH GRID CELL DEPENDS ON
– the irrigated area, 
– crop yields, and 
– water per crop. 
/
g
g
g
g
g
g
yield
drop
crop
C
W
W
L
L
C



=










IN TABLO
! DECOMPOSING WATER USE!
WATERGL(G,L) = QLANDGL(G,L) * YIELDGL(G,L) * WATPERCROPGL(G,L);
!CHANGE IN WATER PER CROP!
P_WAT2CROPGL_A(G,L) =  
- ECROPGL(G,L)   *[P_PAUGLANDGL(G,L)-P_PCROPGL(G,L)   ] !SUBS WITH NITRO
- EAUGLANDGL(G,L)*[P_PLANDWTRGL(G,L)-P_PAUGLANDGL(G,L)] !SUBS WITH OTHER
- EIRRIGGL(G,L)  *[P_PWATERGL(G,L)  -P_PLANDWTRGL(G,L)] !SUBS WITH LAND
- ESUB_WKGL(G,L) *[P_PWWDRLGL(G,L)  -P_PWATERGL(G,L)  ] !SUBS WITH EQPT
.

DATA AND PARAMETERS

A NEW DATABASE OF GRIDDED IRRIGATED
AGRICULTURE
•
USDA
– Cropland Data Layer (CDL) at 30-meter resolution
– NASS: Value of Crop Sold and  by county
– NASS: Total Market Value of Agricultural Products Sold by county 
– NASS: Cropland Cash Rents by county 
– ERS: Production Expenses by county
– FRIS: Farm and Ranch Irrigation Survey by state 
•
USGS:
– Moderate Resolution Imaging Spectroradiometer (MODIS) 
Irrigated Agriculture Dataset for the United States (MIrAD-US) at 
250-meter resolution
•
GLOBAL CROP WATER MODEL (GCWM)
25

CROPLAND AREA: MIRAD VERSUS CDL

GROUNDWATER WITHDRAWAL TO
RECHARGE RATIO

VALUE OF IRRIGATION

Thanks!

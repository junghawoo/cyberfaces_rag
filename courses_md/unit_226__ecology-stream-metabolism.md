---
title: "Ecology: Stream Metabolism"
unit_id: 226
course_id: 0
level: "Expert"
slug: ecology-stream-metabolism
is_course: 0
---

# Ecology: Stream Metabolism

## Fetched resources (external URLs)

### JN_Stream Metabolism (notebook)
*URL:* https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Stream%20Metabolism.ipynb

* Downloading data from streamPulse
* different ways to calculate gas exchange
* run the model with old school k estimates
* run the model with bayesian estimation
* plot the results

```python
library(dataRetrieval)
library(stringr)
library(parallel)
library(lubridate)
library(streamMetabolizer)
library(zoo)
library(lubridate)
library(chron)
library(dplyr)
library(doBy)
library(oce)
```

# Stream Metabolism
Ecosystem metabolism is a critical concept and measurement that allows researchers to model the productivity, respiration, and carbon cycling of an ecosystem.

We are going to model ecosystem metabolism in streams (or rivers) using the R package _streamMetabolizer_ developed by USGS. Current ecosystem metabolism methods in aquatic ecosystems using dissolved oxygen time series to infer rates of primary production and _aerobic_ respiration.


<div>
<img src="images/streammetabolism.png" width="500"/>
</div>

This method works by comparing the rate of oxygen increase during the day, when both photosynthesis and respiration are occurring, versus the night, where only respiration is active. We use the equation below to assess how oxygen changes vary with light while taking into account gas exchange between the water and the air across the water surface.

$$ \Delta m_{O_i,d} = \left( \frac{GPP_d}{Z_{i,d}} \times \frac{PPFD_{i,d}}{PPFD_d} + \frac{ER_d}{Z_{i,d}} + f_{i,d}(K600_d)(O_{sat,i,d}-m_{O_i,d}) \right) \times \Delta t $$

Here is mO<sub>i,d</sub> is modeled DO concentration for timestep i on day _d_, Osat<sub>i,d</sub> is DO saturation for timestep _i_ on day _d_. Δt is the length of each time step (60 minutes in our example), GPP<sub>d</sub> and ER<sub>d</sub> are average GPP and ER (both in g-O<sub>2</sub> m<sup>-2</sup> d<sup>-1</sup>) on day _d_. _z<sub>i,d</sub> is average cross-sectional depth of each upstream. _K600<sub>d</sub> is estimated standardized gas exchange rate (d<sup>-1</sup>) scaled to the Schmidt number 600 on day _d_. _PFFD<sub>i,d</sub> is photosynthetic photon flux density at timestep _i_ on day _d_. <span style="text-decoration:overline">PPFD<sub>d</sub></span> represents the sum of solar insolation for day _d_.

## Getting data prepared
There are a lot of data elements to put together so we're going to start by getting a few custom functions defined. The functions below provide some basic conversions (e.g., _radi_, and _bpcalc_). In addition the function _lightest_ models the light insolation at a given point at a given time using only time and location and a model of insolation based on the position of the sun and the passage of light through the atmosphere. This model does not take into account shading at a given site nor will any weather conditions be accounted for. That being said, it is very difficlt to comprehensively measure light _in situ_ and this modeling approach has been demonstrated to add minimal error to models.

```python
# convert degrees to radians
radi<-function(degrees){(degrees*pi/180)}

# function to estimate light
lightest<- function (time, lat, longobs, longstd, year ) {
  jday<-as.numeric(trunc(time)-as.numeric(as.Date(year)))
  E<- 9.87*sin(radi((720*(jday-81))/365)) - 7.53*cos(radi((360*(jday-81))/365)) - 1.5*sin(radi((360*(jday-81))/365))
  LST<-as.numeric (time-trunc(time))
  ST<-LST+(3.989/1440)*(longstd-longobs)+E/1440
  solardel<- 23.439*sin(radi(360*((283+jday)/365)))
  hourangle<-(0.5-ST)*360
  theta<- acos( sin(radi(solardel)) * sin(radi(lat)) + cos(radi(solardel)) * cos(radi(lat)) * cos(radi(hourangle)) )
  suncos<-ifelse(cos(theta)<0, 0, cos(theta))
  GI<- suncos*2326
  GI	
}


####function returns mm of Hg
bpcalc<- function(bpst, alt) {
  bpst*25.4*exp((-9.80665*0.0289644*alt)/(8.31447*(273.15+15)))
}









```

Below is a custom function that downloads USGS data similarly to how we accomplished this in a previous module. This function has been written to format USGS data to be quickly added to a model.

```python
get_usgs_q_data<-function(usgs_id, site_name){
  rm(list=c("site_q_data","site_q_data_old"))
  #	site_q_data_old<-read.csv(file=paste(site_name, "_usgs_q_data.csv",sep=""),header=TRUE)
  usgs_id<-as.character(usgs_id)
  usgs_q_url<-constructNWISURL(paste(usgs_id),c("00060","00065"),statCd="00011","","","iv")
  site_q_data <- importWaterML1(usgs_q_url)
  if(nrow(site_q_data)>0){
    names(site_q_data)<-c("agency_cd","site_no","dateTime","X_00060_00011","X_00060_00011_cd","X_00065_00011","X_00065_00011_cd","tz_cd")
    #	site_q_data_comb<-rbind.data.frame(site_q_data_old,site_q_data)
    site_q_data_comb<-site_q_data
    site_q_data_comb2<-site_q_data_comb[!duplicated(site_q_data_comb$dateTime),]
    #	site_q_data_old<-read.csv(paste(site_name, "_usgs_q_data.csv",sep=""))
    #	names(site_q_data_old)<-names(site_q_data)
    #	site_q_data_comb<-rbind(site_q_data, site_q_data_old)
    #	site_q_data_nodup<-site_q_data_comb[!duplicated(site_q_data_comb$dateTime),]
    site_q_data_comb2$dt<-gsub("T", " ",site_q_data_comb2$dateTime,fixed=TRUE)
    site_q_data_comb2$dt<-gsub(":00.000", " ",site_q_data_comb2$dt)
    site_q_data_comb2$dt<-gsub("-04:00", "-0400",site_q_data_comb2$dt)
    site_q_data_comb2$dt<-gsub("-05:00", "-0500",site_q_data_comb2$dt)
    site_q_data_comb2$dtp <- strptime(site_q_data_comb2$dt, format="%Y-%m-%d %H:%M %z",tz="EST")
    site_q_data_comb2$Site<-rep(paste(site_name),nrow(site_q_data_comb2))
    return(site_q_data_comb2)
    #write.csv(site_q_data_comb2, file=paste(site_name, "_usgs_q_data.csv",sep=""),row.names=FALSE)
  }
}


```

We are going to be modeling ecosystem metabolism in the Farmington River at the USGS gage site in Unionville Connecticut ([01184000](https://waterdata.usgs.gov/monitoring-location/01188090/#parameterCode=00065&period=P7D&showMedian=false)).

Now that we've defined this function, we're going to use it to download data from the USGS site at Unionville

```python
thom_q<-get_usgs_q_data("01184000","UNIO")
thom_q$dtp<-as.POSIXct(thom_q$dtp)

```

_output:_
```
Warning message in rm(list = c("site_q_data", "site_q_data_old")):
“object 'site_q_data' not found”
Warning message in rm(list = c("site_q_data", "site_q_data_old")):
“object 'site_q_data_old' not found”
```

Elevation is provided so that we can correct local barometric pressure readings to the appropriate altitude.

```python
lightlat<-41.7555472
lightlong<--72.8870417
site_id<-"01184000"
eleva<-66
site_n<-"UNIO"
```

Now we're going to import the barometric pressure dataset provided, convert and correct for elevation and then merge those data into the discharge dataset we've already downloaded.

```python
bdl_pressure<-readRDS("files/bdl_pressure_2014_2020_15.rds")
names(bdl_pressure)<-c("dtp","mslp_mmhg")
bdl_pressure$atmo_inhg<-bdl_pressure$mslp_mmhg/25.4
bdl_pressure$site_mmhg<-bpcalc(bdl_pressure$atmo_inhg,eleva)

thom_pressure<-merge(thom_q,bdl_pressure,all.x=TRUE,by="dtp")

```

Now we're going to load a dataset containing time series data from a sonde deployed in the Farmington River. Data include temperature, dissolved oxygen, conductance, and pH, though our analysis will focus on the first two variables.

We are going to take the sonde data and merge it into the other datasets.

Next comes a little housekeeping to make sure our variables are correct named and in the correct units.

```python
site_sonde<-read.csv("files/unio.csv",header=TRUE)
site_sonde$dtp<-as.POSIXct(site_sonde$est,format="%m/%d/%y %H:%M",tz="EST")

#We are going to select a subset of our data so that we don't spend all day (literally) running the model! The full dataset is available so you can run as muchb of the model as you want!
site_sonde_selected<-subset(site_sonde,dtp>=as.Date("2017-07-01") & dtp<=as.Date("2017-07-31"))

sonde_q_pressure<-merge(site_sonde_selected,thom_pressure,by="dtp",all.x=TRUE)

sonde_q_pressure$q_cms<-sonde_q_pressure$X_00060_00011*028316847
sonde_q_pressure$SpCond_mS_cm<-sonde_q_pressure$SpCond_uS_cm/1000

#converting conductance to salinity for estimating DO saturation.
sonde_q_pressure$sal<-swSCTp(sonde_q_pressure$SpCond_mS_cm,sonde_q_pressure$Temp_deg_C,pressure=sonde_q_pressure$site_mmhg,conductivityUnit="mS/cm")


sonde_q_pressure$bp_atm_mb<-sonde_q_pressure$site_mmhg*1.33322
sonde_q_pressure$o2sat<-calc_DO_sat(sonde_q_pressure$Temp_deg_C,sonde_q_pressure$bp_atm_mb,sonde_q_pressure$sal,model = "garcia-benson")

sonde_q_pressure$do_per<-((sonde_q_pressure$HDO_mg_l/sonde_q_pressure$o2sat)*100)
#sonde_q_pressure$dtp_lag<-dplyr::lag(sonde_q_pressure$dtp,k=1)
#sonde_q_pressure$timestep<-sonde_q_pressure$dtp-sonde_q_pressure$dtp_lag
```

Now we need to obtain channel geometry information from USGS (e.g., channel width and channel area) so that we can estimate mean river depth so that it can be incorporated into the model.

```python
chan_url<-paste("https://waterdata.usgs.gov/nwis/measurements?site_no=",site_id,"&agency_cd=USGS&format=rdb_expanded",sep="")
chan_data <- importRDB1(chan_url)

chan_data_1<-subset(chan_data,chan_velocity!="")
chan_data_1$chan_area<-as.numeric(as.character(chan_data_1$chan_area))
chan_data_1$chan_width<-as.numeric(as.character(chan_data_1$chan_width))
chan_data_1$chan_width_old<-chan_data_1$chan_width
#chan_data_1$mean_depth<-(chan_data_1$chan_area/chan_data_1$chan_width)-0.2
chan_data_1$mean_depth<-(chan_data_1$chan_area/chan_data_1$chan_width)
#chan_data_1$chan_width<-chan_data_1$chan_area/chan_data_1$mean_depth
gage_mdepth<-lm(log(chan_data_1$mean_depth)~log(chan_data_1$chan_discharge),na.action=na.omit)
gage_vel<-lm(chan_data_1$chan_velocity~chan_data_1$gage_height_va,na.action=na.omit)
gage_width<-lm(chan_data_1$chan_width~chan_data_1$gage_height_va,na.action=na.omit)


sonde_q_pressure$mdepth_f<-exp((log(sonde_q_pressure$X_00060_00011)*gage_mdepth$coefficients[2])+gage_mdepth$coefficients[1])
sonde_q_pressure$width_f<-(sonde_q_pressure$X_00065_00011*gage_width$coefficients[2])+gage_width$coefficients[1]
sonde_q_pressure$vel_fts<-(sonde_q_pressure$X_00065_00011*gage_vel$coefficients[2])+gage_vel$coefficients[1]

sonde_q_pressure$chr0n<-chron(dates = strftime(sonde_q_pressure$dt, format="%Y-%m-%d",tz="EST"), times = strftime(sonde_q_pressure$dt, format="%H:%M:%S",tz="EST"), format=c(dates = "y-m-d", times = "h:m:s"))
sonde_q_pressure$TIME<-strftime(sonde_q_pressure$dt, format="%H:%M:%S",tz="EST")
```

Essentially all real-world datasets have gaps of some sort. To run this model, we need to remove these gaps. The block of code below subsets each day of data and interpolates gaps that are 2 hours or less in length.

```python
p_phel_sonde_1<-subset(sonde_q_pressure,!is.na(X_00065_00011) & !is.na(sonde_q_pressure$vel_fts) & q_cms>0)
p_phel_sonde_o<-p_phel_sonde_1[order(p_phel_sonde_1$dt),]
date_index<-unique(dates(p_phel_sonde_o$chr0n))
date_len<-length(date_index)-1

dates_list<-p_phel_sonde_o
dates_list$date<-as.Date(dates_list$dtp)
date_run<-summaryBy(date~date,dates_list,FUN=c(length))



rm(accum)
for(i in 2:date_len){
  workd00<-subset(p_phel_sonde_o, p_phel_sonde_o$chr0n>=as.numeric(chron(dates=format(as.Date(date_index)[i-1],"%m/%d/%y"), times="22:00:00")) & p_phel_sonde_o$chr0n<=as.numeric(chron(dates=format(as.Date(date_index)[i+1],"%m/%d/%y"), times="06:00:00")))
  workd0<-workd00[!is.na(workd00$Temp_deg_C),]
  #	workd0<-workd0[!is.na(workd0$mdepth_f),]
  #	workd0<-workd0[!is.na(workd0$p_abp_mmhg),]
  #	workd0<-workd0[!is.na(workd0$light),]
  t0<-chron(dates=format(as.Date(date_index)[i-1],"%m/%d/%y"), times="22:00:00")
  t1<-chron(dates=format(as.Date(date_index)[i+1],"%m/%d/%y"), times="06:00:00")
  cindex<-seq(t0,t1+(1/24/60),by=(1/24/4))
  ci<-as.data.frame(cindex)
  workd0$datematch<-as.POSIXct(workd0$chr0n,tz="EST")
  ci$datematch<-as.POSIXct(ci$cindex,tz="EST")
  ci<-zoo(ci)
  if(sum(!is.na(workd0$HDO_mg_l))>23){
    #	workd<-merge(ci,workd0,by.x="cindex",by.y="chr0n",all.x=TRUE, all.y=FALSE)
    workd<-merge(ci,workd0,by="datematch",all.x=TRUE)
    #	workd$TIME<-strftime(workd$cindex+(5/24), tz="EST", format="%H:%M:%S")
    #	workd$dtp3<-as.POSIXct(workd$cindex)
    workd$Temp_deg_C<-na.approx(workd$Temp_deg_C,rule=2)
    workd$mdepth_f<-na.approx(workd$mdepth_f,rule=2)
    workd$vel_fts<-na.approx(workd$vel_fts,rule=2)
    #workd$width_f<-na.approx(workd$width_f,rule=2)
    workd$site_mmhg<-na.approx(workd$site_mmhg,rule=2)
    #	workd$light<-na.approx(workd$light,rule=2)
    workd$HDO_mg_l<-na.approx(workd$HDO_mg_l,rule=2)
    workd$o2sat<-na.approx(workd$o2sat,rule=2)
    workd$stage_ft_fill<-na.approx(workd$X_00065_00011,rule=2)	
    workd$q_cfs_fill<-na.approx(workd$X_00060_00011,rule=2)	
    workd1<-as.data.frame(workd)
    workd1$dtp3<-as.POSIXct(workd1$datematch.ci,tz="EST")	
    workd1$chr0n<-chron(dates = strftime(workd1$dtp3, format="%Y-%m-%d",tz="EST"), times = strftime(workd1$dtp3, format="%H:%M:%S",tz="EST"), format=c(dates = "y-m-d", times = "h:m:s"))
    workd1$light<- lightest(time=workd1$chr0n, lat=lightlat,  longobs=-lightlong, longstd= 75, year="2016-01-01")	
  }
  if(!exists("accum")){accum<-workd1[0,]}
  accum<-bind_rows(accum,workd1)
  print(i)
}

```

_output:_
```
[1] 2
[1] 3
[1] 4
[1] 5
[1] 6
[1] 7
[1] 8
[1] 9
[1] 10
[1] 11
[1] 12
[1] 13
[1] 14
[1] 15
[1] 16
[1] 17
[1] 18
[1] 19
[1] 20
[1] 21
[1] 22
[1] 23
[1] 24
[1] 25
[1] 26
[1] 27
[1] 28
[1] 29
[1] 30
```

This step does some additional formatting, ensuring that all the variables have the right name.

```python
accum$discharge<-as.numeric(as.character(accum$q_cfs_fill))*0.0283168
accum3<-subset(accum,!is.na(dtp3) & !is.na(discharge))
#accum3<-accum2[!is.na(accum2$dtp3),]
attr(accum3$dtp3,"tzone") <- "Etc/GMT+5"
accum3$solar.time <- streamMetabolizer::calc_solar_time(accum3$dtp3, longitude=lightlong)
#accum3$solar.time<-local2Solar(accum3$dtp3,lon=lightlong)

accum3$mdepth_m<-(as.numeric(as.character(accum3$mdepth_f))*0.3048)+1
accum4<-accum3[order(accum3$solar.time),]
accum5<-accum4[!duplicated(accum4$solar.time),]
dat2<-subset(accum5,select=c("solar.time","HDO_mg_l","o2sat","mdepth_m","Temp_deg_C","light"))
names(dat2)<-c("solar.time","DO.obs","DO.sat","depth","temp.water","light")

dat2q<-subset(accum5,select=c("solar.time","HDO_mg_l","o2sat","mdepth_m","Temp_deg_C","light","discharge"))
names(dat2q)<-c("solar.time","DO.obs","DO.sat","depth","temp.water","light","discharge")


dat2q$DO.obs<-as.numeric(as.character(dat2q$DO.obs))
dat2q$DO.sat<-as.numeric(as.character(dat2q$DO.sat))
dat2q$temp.water<-as.numeric(as.character(dat2q$temp.water))

```

The most challenging part of ecosystem metabolism in streams and rivers isn't measuring the biology of the system, it's accounting for the exchange of oxygen between water and air. This must be accounted for to generate an accurate model.

We are going to introduce two approaches for doing this. The first is to manually estimate gas exchange rate (K) using empirical equations that are based on the flow rate of water.

The second, more sophisticated approach, uses Bayesian estimation to pool estimates of K made by the ecosystem metabolism model across days, developing a relationship between discharge and K that is derived from this dataset.

For more inormation on this approach, check out the [streamMetabolizer documentation](https://web.archive.org/web/20210325145225/https://usgs-r.github.io/streamMetabolizer/).

```python
head(thom_q)
```

_result:_
```
agency_cd site_no  dateTime                      X_00060_00011
1 USGS      01184000 1990-10-01T01:15:00.000-04:00 7780         
2 USGS      01184000 1990-10-01T01:30:00.000-04:00 7780         
3 USGS      01184000 1990-10-01T01:45:00.000-04:00 7600         
4 USGS      01184000 1990-10-01T02:00:00.000-04:00 7510         
5 USGS      01184000 1990-10-01T02:15:00.000-04:00 7690         
6 USGS      01184000 1990-10-01T02:30:00.000-04:00 7600         
  X_00060_00011_cd X_00065_00011 X_00065_00011_cd tz_cd dt                    
1 A [91]           NA            NA               EST   1990-10-01 01:15 -0400
2 A [91]           NA            NA               EST   1990-10-01 01:30 -0400
3 A [91]           NA            NA               EST   1990-10-01 01:45 -0400
4 A [91]           NA            NA               EST   1990-10-01 02:00 -0400
5 A [91]           NA            NA               EST   1990-10-01 02:15 -0400
6 A [91]           NA            NA               EST   1990-10-01 02:30 -0400
  dtp                 Site
1 1990-10-01 00:15:00 UNIO
2 1990-10-01 00:30:00 UNIO
3 1990-10-01 00:45:00 UNIO
4 1990-10-01 01:00:00 UNIO
5 1990-10-01 01:15:00 UNIO
6 1990-10-01 01:30:00 UNIO
```

```python
dat2q
?streamMetabolizer::metab


colname	class	units	need
solar.time	POSIXct,POSIXt		required
DO.obs	numeric	mgO2 L^-1	required
DO.sat	numeric	mgO2 L^-1	required
depth	numeric	m	required
temp.water	numeric	degC	required
light	numeric	umol m^-2 s^-1	required
discharge	numeric	m^3 s^-1	optional

```

_result:_
```
solar.time          DO.obs DO.sat   depth    temp.water light    
1...1      2017-07-01 18:09:15 8.79   9.225831 3.842507 18.76      575.06913
2...2      2017-07-01 18:24:15 8.77   9.227209 3.847250 18.75      470.83766
3...3      2017-07-01 18:39:15 8.76   9.228588 3.849126 18.74      367.20023
4...4      2017-07-01 18:54:15 8.74   9.229970 3.850060 18.73      264.60064
5...5      2017-07-01 19:09:15 8.73   9.232055 3.851919 18.72      163.47824
6...6      2017-07-01 19:24:15 8.72   9.234610 3.852845 18.71       64.26604
7...7      2017-07-01 19:39:15 8.71   9.235290 3.856519 18.71        0.00000
8...8      2017-07-01 19:54:15 8.70   9.237870 3.857430 18.70        0.00000
9...9      2017-07-01 20:09:15 8.70   9.240698 3.859245 18.69        0.00000
10...10    2017-07-01 20:24:15 8.69   9.243732 3.860148 18.68        0.00000
11...11    2017-07-01 20:39:15 8.69   9.244896 3.861049 18.68        0.00000
12...12    2017-07-01 20:54:15 8.69   9.247940 3.861049 18.67        0.00000
13...13    2017-07-01 21:09:15 8.68   9.248270 3.864626 18.67        0.00000
14...14    2017-07-01 21:24:15 8.68   9.246165 3.865513 18.68        0.00000
15...15    2017-07-01 21:39:15 8.67   9.247812 3.866399 18.67        0.00000
16...16    2017-07-01 21:54:15 8.68   9.247590 3.866399 18.67        0.00000
17...17    2017-07-01 22:09:15 8.67   9.245065 3.869913 18.68        0.00000
18...18    2017-07-01 22:24:15 8.66   9.244140 3.870786 18.68        0.00000
19...19    2017-07-01 22:39:15 8.66   9.241337 3.869913 18.69        0.00000
20...20    2017-07-01 22:54:15 8.66   9.238537 3.871656 18.70        0.00000
21...21    2017-07-01 23:09:15 8.66   9.238044 3.872523 18.70        0.00000
22...22    2017-07-01 23:24:15 8.66   9.237817 3.873388 18.70        0.00000
23...23    2017-07-01 23:39:15 8.65   9.237592 3.874251 18.70        0.00000
24...24    2017-07-01 23:54:15 8.65   9.239245 3.875968 18.69        0.00000
25...25    2017-07-02 00:09:15 8.65   9.241459 3.875968 18.68        0.00000
26...26    2017-07-02 00:24:15 8.65   9.245941 3.874251 18.66        0.00000
27...27    2017-07-02 00:39:15 8.65   9.250389 3.877677 18.64        0.00000
28...28    2017-07-02 00:54:15 8.65   9.252981 3.878527 18.63        0.00000
29...29    2017-07-02 01:09:15 8.66   9.257589 3.878527 18.61        0.00000
30...30    2017-07-02 01:24:15 8.67   9.262299 3.878527 18.59        0.00000
⋮          ⋮                   ⋮      ⋮        ⋮        ⋮          ⋮        
100...3712 2017-07-30 18:54:15 8.90   9.378691 3.309994 18.24      158.67096
101...3713 2017-07-30 19:09:15 8.89   9.388516 3.313989 18.19       54.15602
102...3714 2017-07-30 19:24:15 8.88   9.398220 3.309994 18.14        0.00000
103...3715 2017-07-30 19:39:15 8.88   9.407848 3.313989 18.09        0.00000
104...3716 2017-07-30 19:54:15 8.88   9.415563 3.309994 18.05        0.00000
105...3717 2017-07-30 20:09:15 8.88   9.421359 3.309994 18.02        0.00000
106...3718 2017-07-30 20:24:15 8.87   9.429659 3.317921 17.98        0.00000
107...3719 2017-07-30 20:39:15 8.87   9.429659 3.317921 17.98        0.00000
108...3720 2017-07-30 20:54:15 8.87   9.429659 3.317921 17.98        0.00000
109...3721 2017-07-30 21:09:15 8.87   9.429659 3.317921 17.98        0.00000
110...3722 2017-07-30 21:24:15 8.87   9.429659 3.317921 17.98        0.00000
111...3723 2017-07-30 21:39:15 8.87   9.429659 3.317921 17.98        0.00000
112...3724 2017-07-30 21:54:15 8.87   9.429659 3.317921 17.98        0.00000
113...3725 2017-07-30 22:09:15 8.87   9.429659 3.317921 17.98        0.00000
114...3726 2017-07-30 22:24:15 8.87   9.429659 3.317921 17.98        0.00000
115...3727 2017-07-30 22:39:15 8.87   9.429659 3.317921 17.98        0.00000
116...3728 2017-07-30 22:54:15 8.87   9.429659 3.317921 17.98        0.00000
117...3729 2017-07-30 23:09:15 8.87   9.429659 3.317921 17.98        0.00000
118...3730 2017-07-30 23:24:15 8.87   9.429659 3.317921 17.98        0.00000
119...3731 2017-07-30 23:39:15 8.87   9.429659 3.317921 17.98        0.00000
120...3732 2017-07-30 23:54:15 8.87   9.429659 3.317921 17.98        0.00000
121...3733 2017-07-31 00:09:15 8.87   9.429659 3.317921 17.98        0.00000
122...3734 2017-07-31 00:24:15 8.87   9.429659 3.317921 17.98        0.00000
123...3735 2017-07-31 00:39:15 8.87   9.429659 3.317921 17.98        0.00000
124...3736 2017-07-31 00:54:15 8.87   9.429659 3.317921 17.98        0.00000
125...3737 2017-07-31 01:09:15 8.87   9.429659 3.317921 17.98        0.00000
126...3738 2017-07-31 01:24:15 8.87   9.429659 3.317921 17.98        0.00000
127...3739 2017-07-31 01:39:15 8.87   9.429659 3.317921 17.98        0.00000
128...3740 2017-07-31 01:54:15 8.87   9.429659 3.317921 17.98        0.00000
129...3741 2017-07-31 02:09:15 8.87   9.429659 3.317921 17.98        0.00000
           discharge
1...1      809.8605 
2...2      824.0189 
3...3      829.6822 
4...4      832.5139 
5...5      838.1773 
6...6      841.0090 
7...7      852.3357 
8...8      855.1674 
9...9      860.8307 
10...10    863.6624 
11...11    866.4941 
12...12    866.4941 
13...13    877.8208 
14...14    880.6525 
15...15    883.4842 
16...16    883.4842 
17...17    894.8109 
18...18    897.6426 
19...19    894.8109 
20...20    900.4742 
21...21    903.3059 
22...22    906.1376 
23...23    908.9693 
24...24    914.6326 
25...25    914.6326 
26...26    908.9693 
27...27    920.2960 
28...28    923.1277 
29...29    923.1277 
30...30    923.1277 
⋮          ⋮        
100...3712 93.72861 
101...3713 95.42762 
102...3714 93.72861 
103...3715 95.42762 
104...3716 93.72861 
105...3717 93.72861 
106...3718 97.12662 
107...3719 97.12662 
108...3720 97.12662 
109...3721 97.12662 
110...3722 97.12662 
111...3723 97.12662 
112...3724 97.12662 
113...3725 97.12662 
114...3726 97.12662 
115...3727 97.12662 
116...3728 97.12662 
117...3729 97.12662 
118...3730 97.12662 
119...3731 97.12662 
120...3732 97.12662 
121...3733 97.12662 
122...3734 97.12662 
123...3735 97.12662 
124...3736 97.12662 
125...3737 97.12662 
126...3738 97.12662 
127...3739 97.12662 
128...3740 97.12662 
129...3741 97.12662
```

_result:_
```
metab            package:streamMetabolizer             R Documentation

_F_i_t _a _m_e_t_a_b_o_l_i_s_m _m_o_d_e_l _t_o _d_a_t_a

_D_e_s_c_r_i_p_t_i_o_n:

     Runs the metabolism model specified by the ‘specs’ argument.
     Returns a fitted model.

_U_s_a_g_e:

     metab(
       specs = specs(mm_name()),
       data = v(mm_data(NULL)),
       data_daily = v(mm_data(NULL)),
       info = NULL
     )
     
_A_r_g_u_m_e_n_t_s:

   specs: a list of model specifications and parameters for a model.
          Although this may be specified manually (it's just a list),
          it is easier and safer to use ‘specs’ to generate the list,
          because the set of required parameters and their defaults
          depends on the model given in the ‘model_name’ argument to
          ‘specs’. The help file for ‘specs’ lists the necessary
          parameters, describes them in detail, and gives default
          values.

    data: data.frame (not a tbl_df) of input data at the temporal
          resolution of raw observations (unit-value). Columns must
          have the same names, units, and format as the default. The
          solar.time column must also have a timezone code ('tzone'
          attribute) of 'UTC'. See the *'Formatting ‘data’'* section
          below for a full description.

data_daily: data.frame containing inputs with a daily timestep. See the
          *'Formatting ‘data_daily’'* section below for a full
          description.

    info: any information, in any format, that you would like to store
          within the metab_model object

_V_a_l_u_e:

     An object inheriting from metab_model and containing the fitted
     model. This object can be inspected with the functions in the
     ‘metab_model_interface’.

_F_o_r_m_a_t_t_i_n_g '_d_a_t_a':

     Unit-value model inputs passed via the ‘data’ argument should be
     formatted as a data.frame with column names and values that depend
     on the model ‘type’, as follows. (If all columns are optional,
     ‘data’ may equal ‘NULL’.)

     ‘mle’ or ‘night’

            *colname*   *class*         *units*         *need*   
            solar.time  POSIXct,POSIXt                  required 
            DO.obs      numeric         mgO2 L^-1       required 
            DO.sat      numeric         mgO2 L^-1       required 
            depth       numeric         m               required 
            temp.water  numeric         degC            required 
            light       numeric         umol m^-2 s^-1  required 
            discharge   numeric         m^3 s^-1        optional 
           
          *Example*:

            ‘solar.time         ’  ‘DO.obs’  ‘DO.sat’  ‘depth’  ‘temp.water’  ‘light’  ‘discharge’ 
            ‘2050-03-14 15:10:00’  ‘10.1  ’  ‘14.2  ’  ‘0.5  ’  ‘21.8      ’  ‘300.9’  ‘9        ’ 
           
     ‘bayes’

            *colname*   *class*         *units*         *need*   
            solar.time  POSIXct,POSIXt                  required 
            DO.obs      numeric         mgO2 L^-1       required 
            DO.sat      numeric         mgO2 L^-1       required 
            depth       numeric         m               required 
            temp.water  numeric         degC            required 
            light       numeric         umol m^-2 s^-1  required 
            discharge   numeric         m^3 s^-1        optional 
           
          *Example*:

            ‘solar.time         ’  ‘DO.obs’  ‘DO.sat’  ‘depth’  ‘temp.water’  ‘light’  ‘discharge’ 
            ‘2050-03-14 15:10:00’  ‘10.1  ’  ‘14.2  ’  ‘0.5  ’  ‘21.8      ’  ‘300.9’  ‘9        ’ 
           
     ‘Kmodel’

            *colname*   *class*         *units*   *need*   
            solar.time  POSIXct,POSIXt            optional 
            discharge   numeric         m^3 s^-1  optional 
            velocity    numeric         m s^-1    optional 
           
          *Example*:

            ‘solar.time         ’  ‘discharge’  ‘velocity’ 
            ‘2050-03-14 15:10:00’  ‘9        ’  ‘2       ’ 
           
     ‘sim’

            *colname*   *class*         *units*         *need*   
            solar.time  POSIXct,POSIXt                  required 
            DO.obs      numeric         mgO2 L^-1       optional 
            DO.sat      numeric         mgO2 L^-1       required 
            depth       numeric         m               required 
            temp.water  numeric         degC            required 
            light       numeric         umol m^-2 s^-1  required 
           
          *Example*:

            ‘solar.time         ’  ‘DO.obs’  ‘DO.sat’  ‘depth’  ‘temp.water’  ‘light’ 
            ‘2050-03-14 15:10:00’  ‘10.1  ’  ‘14.2  ’  ‘0.5  ’  ‘21.8      ’  ‘300.9’ 
           
_F_o_r_m_a_t_t_i_n_g '_d_a_t_a__d_a_i_l_y':

     Daily-value model inputs passed via the ‘data_daily’ argument
     should be formatted as a data.frame with column names and values
     that depend on the model ‘type’, as follows. (If all columns are
     optional, ‘data_daily’ may equal ‘NULL’.)

     ‘night’ ‘NULL’

     ‘mle’

            *colname*        *class*  *units*             *need*   
            date             Date                         optional 
            K600.daily       numeric  d^-1                optional 
            init.GPP.daily   numeric  gO2 d^-1 m^-2       optional 
            init.Pmax        numeric  gO2 d^-1 m^-2       optional 
            init.alpha       numeric  gO2 s d^-1 umol^-1  optional 
            init.ER.daily    numeric  gO2 d^-1 m^-2       optional 
            init.ER20        numeric  gO2 d^-1 m^-2       optional 
            init.K600.daily  numeric  d^-1                optional 
           
          *Example*:

            ‘date      ’  ‘K600.daily’  ‘init.GPP.daily’  ‘init.Pmax’  ‘init.alpha’  ‘init.ER.daily’  ‘init.ER20’  ‘init.K600.daily’ 
            ‘2050-03-14’  ‘10        ’  ‘5             ’  ‘10       ’  ‘1e-04     ’  ‘-10          ’  ‘-10      ’  ‘10             ’ 
           
     ‘bayes’

            *colname*        *class*  *units*   *need*   
            date             Date               optional 
            discharge.daily  numeric  m^3 s^-1  optional 
           
          *Example*:

            ‘date      ’  ‘discharge.daily’ 
            ‘2050-03-14’  ‘9              ’ 
           
     ‘Kmodel’

            *colname*         *class*  *units*   *need*   
            date              Date               required 
            K600.daily        numeric  d^-1      required 
            K600.daily.lower  numeric  d^-1      optional 
            K600.daily.upper  numeric  d^-1      optional 
            discharge.daily   numeric  m^3 s^-1  optional 
            velocity.daily    numeric  m s^-1    optional 
           
          *Example*:

            ‘date      ’  ‘K600.daily’  ‘K600.daily.lower’  ‘K600.daily.upper’  ‘discharge.daily’  ‘velocity.daily’ 
            ‘2050-03-14’  ‘10        ’  ‘4.5             ’  ‘15.6            ’  ‘9              ’  ‘2             ’ 
           
     ‘sim’

            *colname*        *class*  *units*             *need*   
            date             Date                         optional 
            discharge.daily  numeric  m^3 s^-1            optional 
            DO.mod.1         numeric  mgO2 L^-1           optional 
            K600.daily       numeric  d^-1                optional 
            GPP.daily        numeric  gO2 d^-1 m^-2       optional 
            Pmax             numeric  gO2 d^-1 m^-2       optional 
            alpha            numeric  gO2 s d^-1 umol^-1  optional 
            ER.daily         numeric  gO2 d^-1 m^-2       optional 
            ER20             numeric  gO2 d^-1 m^-2       optional 
            err.obs.sigma    numeric  mgO2 L^-1           optional 
            err.obs.phi      numeric                      optional 
            err.proc.sigma   numeric  gO2 d^-1 m^-2       optional 
            err.proc.phi     numeric                      optional 
           
          *Example*:

            ‘date      ’  ‘discharge.daily’  ‘DO.mod.1’  ‘K600.daily’  ‘GPP.daily’  ‘Pmax’  ‘alpha’  ‘ER.daily’  ‘ER20’  ‘err.obs.sigma’  ‘err.obs.phi’  ‘err.proc.sigma’  ‘err.proc.phi’ 
            ‘2050-03-14’  ‘9              ’  ‘7.5     ’  ‘10        ’  ‘5        ’  ‘10  ’  ‘1e-04’  ‘-10     ’  ‘-10 ’  ‘0.01         ’  ‘0          ’  ‘5             ’  ‘0           ’ 
           
_A_u_t_h_o_r(_s):

     Alison Appling

_E_x_a_m_p_l_e_s:

     dat <- data_metab(num_days='3')
     
     # fit a basic MLE model
     mm <- metab(specs(mm_name('mle')), data=dat, info='my info')
     predict_metab(mm)
     get_info(mm)
     get_fitting_time(mm)
     
     # with chaining & customization
     library(dplyr)
     mm <- mm_name('mle', ode_method='euler') %>%
       specs(init.GPP.daily=40) %>%
       metab(data=dat)
     predict_metab(mm)
     ## Not run:
     
     plot_DO_preds(predict_DO(mm))
     plot_DO_preds(predict_DO(mm), y_var='pctsat', style='dygraphs')
     ## End(Not run)
```

```python
brks
```

_result:_
```
[1] 24.1 24.3 24.5 24.7 24.9 25.1 25.3 25.5 25.7 25.9 26.1 26.3 26.5 26.7 26.9
[16] 27.1 27.3 27.5 27.7 27.9 28.1 28.3 28.5 28.7 28.9 29.1
```

```python
#bayes_name <- mm_name(type='bayes', pool_K600='binned',err_obs_iid=TRUE, err_proc_acor=FALSE, err_proc_iid=TRUE, ode_method='trapezoid')
bayes_name<-"b_Kb_oipi_tr_plrckm.stan"
bayes_name

#bayes_specs <- specs(bayes_name)
#bayes_specs

#we are taking the natural log of the discharge record that will then be placed into evenly spaced bins for Bayesian estimation.
thom_q$q_cms<-thom_q$X_00060_00011*028316847
ln.disch <- log(thom_q$q_cms)

# for use in setting specs
brks <- calc_bins(ln.disch, 'width', width=0.2)$bounds


#specs('b_Kb_oipi_tr_plrckm.stan', K600_lnQ_nodes_centers=brks)
specs(bayes_name, K600_lnQ_nodes_centers=brks, burnin_steps=10,saved_steps=20,verbose=TRUE)


#brks<-seq(3.66,7.88,0.2)
# one way to alter specifications: call specs() again
bayes_specs <- specs(bayes_name, K600_lnQ_nodes_centers=brks, burnin_steps=10,saved_steps=20,verbose=TRUE)
#bayes_specs <- specs(bayes_name, K600_lnQ_nodes_centers=brks, burnin_steps=10,saved_steps=10)

#phel_q$DO.obs<-as.numeric(phel_q$DO.obs)
#phel_q$DO.sat<-as.numeric(phel_q$DO.sat)
#phel_q$temp.water<-as.numeric(phel_q$temp.water)




#Finally we are going to use streamMetabolizer to fit the Bayesian model.
bayes_fit <- streamMetabolizer::metab(specs = bayes_specs, data=dat2q)

```

_result:_
```
[1] "b_Kb_oipi_tr_plrckm.stan"
```

_result:_
```
Model specifications:
  model_name               b_Kb_oipi_tr_plrckm.stan                             
  engine                   stan                                                 
  split_dates              FALSE                                                
  keep_mcmcs               TRUE                                                 
  keep_mcmc_data           TRUE                                                 
  day_start                4                                                    
  day_end                  28                                                   
  day_tests                full_day, even_timesteps, complete_data, pos_disch...
  required_timestep        NA                                                   
  K600_lnQ_nodes_centers   24.0999999999, 24.3, 24.5, 24.7, 24.9, 25.1, 25.3,...
  GPP_daily_mu             3.1                                                  
  GPP_daily_lower          -Inf                                                 
  GPP_daily_sigma          6                                                    
  ER_daily_mu              -7.1                                                 
  ER_daily_upper           Inf                                                  
  ER_daily_sigma           7.1                                                  
  K600_lnQ_nodediffs_sdlog 0.5                                                  
  K600_lnQ_nodes_meanlog   2.484906649788, 2.484906649788, 2.484906649788, 2....
  K600_lnQ_nodes_sdlog     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1....
  K600_daily_sigma_sigma   0.24                                                 
  err_obs_iid_sigma_scale  0.03                                                 
  err_proc_iid_sigma_scale 5                                                    
  params_in                GPP_daily_mu, GPP_daily_lower, GPP_daily_sigma, ER...
  params_out               GPP, ER, DO_R2, GPP_daily, ER_daily, K600_daily, K...
  n_chains                 4                                                    
  n_cores                  4                                                    
  burnin_steps             10                                                   
  saved_steps              20                                                   
  thin_steps               1                                                    
  verbose                  TRUE
```

_output:_
```
MCMC (Stan): requesting 4 chains on 4 of 10 available cores

compiling Stan model

sampling Stan model
```

_output:_
```
CHECKING DATA AND PREPROCESSING FOR MODEL 'anon_model' NOW.

COMPILING MODEL 'anon_model' NOW.

STARTING SAMPLER FOR MODEL 'anon_model' NOW.
```

_output:_
```
model fit in 24 sec
```

Now we're going to plot the comparison between these two different methods of estimating GPP and ER in streams an rivers so we can understand how these different methods impact model estimation.

```python
library(rstan)
```

_output:_
```
Loading required package: StanHeaders


rstan version 2.32.5 (Stan version 2.32.2)


For execution on a local, multicore CPU with excess RAM we recommend calling
options(mc.cores = parallel::detectCores()).
To avoid recompilation of unchanged Stan programs, we recommend calling
rstan_options(auto_write = TRUE)
For within-chain threading using `reduce_sum()` or `map_rect()` Stan functions,
change `threads_per_chain` option:
rstan_options(threads_per_chain = 1)
```

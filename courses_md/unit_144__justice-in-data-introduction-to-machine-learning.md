---
title: "Justice in Data: Introduction to Machine Learning"
unit_id: 144
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-machine-learning
is_course: 0
---

# Justice in Data: Introduction to Machine Learning

## Extracted resources (local files)

### Introduction to ML
*Source file:* `Lecture_Friday_1_Final.pdf`  ·  *type:* file

Introduction to 
Machine Learning

Presenters
2
Steven Tanner McCullough
PhD Student Researcher
Jessica Eisma, PhD
Assistant Professor
June Young Park, PhD
Assistant Professor

Lecture Content 1: Introduction to ML
●Objective of bootcamp
●Introduction to Machine Learning
●Before learning ML algorithms

Lecture Content 2: ML Algorithms
●Supervised learning
○Decision Tree
○Nearest Neighbors
●Unsupervised Learning
○k-means clustering
●Reinforcement Learning
○Markov Decision Process

Lecture Content 3: Coding practice for ML 
●We will use building energy data for learning classification 
algorithms (knn & decision tree)

Ask ChatGPT:
Best way to learn ML?

Our bootcamp objectives
●Learning ML is generally by taking a course (or courses).
○Certain algorithms require designated courses to learn 
(check your institution’s courses).
●This lecture will not cover all the algorithms that you need to 
learn. Researchers currently develop and release their 
algorithms in various communities.
○Also, everyone develops advanced algorithms upon the 
basic ones, so it is important to know how these work.

Our bootcamp objectives
●We will introduce some basic ML algorithms to begin your 
journey.
○This lecture is for your gentle introduction to ML. A lot of 
self-studies are required, if you are interested in this!
○Do not expect we will cover every algorithm today. We will 
introduce 1-2 basic ones for your self learning.

What is machine learning?
What ML algorithms do you know?

Machine Learning is …
“Instead of trying to produce a program to 
simulate the adult mind, why not rather try 
to produce one which simulates the 
child’s?”
-Alan Touring (1950)

Machine Learning is …
“Field of study that gives computers the 
ability to learn without being explicitly 
programmed.”
-Arthur Samuel (1959)

Machine Learning is …
“A computer program is said to learn, if its 
performance on a task improves with 
experience.”
-Tom Mitchell (1997)

The DIKW Pyramid

The DIKW Pyramid
Data:
Facts, which, by themselves have no meaning

The DIKW Pyramid
Information:
That which leads to understanding the meaning we assign to facts

The DIKW Pyramid
Knowledge:
An orderly synthesis of information
…

The DIKW Pyramid
Wisdom (Insight)
The appropriate applications of knowledge
…
!

The DIKW Pyramid
From data 
(closer) to 
wisdom

How do we understand data for ML?

Data types and features
• Text
• Date
• Binary
• Ordinal
• Category
• Numeric

From raw data to features
●A feature is any measure derived from data that be used by 
the machine learning algorithm.
1.
Raw features = raw data source
2.
Derived features
■Flags
■Ratios
■Mappings
■Aggregates 
■Others

From raw data to features
• Flags
• Ratios
• Aggregates 
• Others

How to understand this image in computer?

Feature engineering for image data

Other advanced feature engineering 
Image: google AI blog

Building energy data feature engineering
What are the important features to express?
Source: Miller et al., Automated daily pattern filtering of measured building performance data, 
automation in construction, 2015

Building energy data feature engineering

Now each day’s 
energy consumption 
profiles can be 
simply expressed by 
features

What can go wrong?
●A good ML model should provide a good generalization
●No Free Lunch Theorem!
●Inappropriate bias can lead to 
1. Underfitting: model too simplistic (relationships not captured well)
2. Overfitting: model too complex (model becomes very sensitive to 
noise)

Example data

underfitting or overfitting?

underfitting or overfitting?

This would be a good fit model

Example question: Credit scoring

Example question: Credit scoring
(a) Which of these two models will generalize better to the instances not 
contained in the dataset? 
(b)Propose an inductive bias that would enable a machine learning algorithm to 
make the same preference choice as you did in part (a) 
(c) Do you think the model you rejected in part (a) is overfitting or underfitting 
the data?

Answers

Bias – Variance tradeoff in ML
●Bias: error due to assumptions
○High bias  = underfitting
○Model does not capture sufficient 
characteristic of the data
●Variance: error due to sensitivity of 
model
○High variance = overfitting
○Model captures noise in the data

Bias – Variance tradeoff in ML
●Bias: error due to assumptions
○High bias  = underfitting
○Model does not capture sufficient 
characteristic of the data
●Variance: error due to sensitivity of 
model
○High variance = overfitting
○Model captures noise in the data
How can we 
then evaluate 
(and improve) 
the performance 
of a given 
model?

Approach: Split input data
Training: (70%) : Validation (30%)
•
Training: Train
•
Validation: Compare models
•
Test: Estimate accuracy (no model tuning anymore)

Cross validation: Split & Repeat

Cross validation: Split & Repeat
●Statistical method of evaluating generalization performance
●More stable and thorough than using a split into a training 
and a test set.
●Data is instead split repeatedly and multiple models are 
trained
●Most commonly version: k-fold cross-validation, where k is a 
user specified number, usually 5 or 10.

K-fold cross validation

Note: Cross Validation
●Avoid good/bad choice of a single training & testing set
●Provides sensitivity of model to data
●Use data more efficiently
●BUT! Computationally demand
●Cross validation is not model building! The purpose of cross 
validation is only to evaluate how well a given algorithm will 
generalize when trained on a specific dataset.

Evaluation of classification performance
●Confusion matrix for a binary target (called positive & negative 
by convention)
●Four possible outcomes
○TP (True Positive)
○TN (True Negative)
○FP (False Positive)
○FN (False Negative)

Example: confusion matrix
Accuracy 
= ?

Example: confusion matrix
Accuracy 
= 155/166
=0.93

## Fetched resources (external URLs)

### Introduction to Machine Learning Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=rat/aUXGAhwECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Introduction to Machine Learning Recording (link)
*URL:* https://www.youtube.com/watch?v=Z-ZuQ01XGRc

[YouTube transcript Z-ZuQ01XGRc]
um today I'm going to cover the introduction to machine learning okay oh no so the presenter myself my name is Junior Park I'm assistant professor at UT Arlington so my research area is a smart and Sustainable Building which utilize a lot for um machine learning techniques so I'm glad to share my knowledge about machine learning as much as I can with respect to the building energy domain and this contents and these all Friday session is available by two other presenters or instructors who help me to formalize the session with my pH student tenor McCullough and Jessica isma Dr Jessica there's another pie who helped on these contents so very first question where are you now how far from Arlington Texas is anyone going to compete with me where are you now just quick question to all you can say with the voice or you can put it in the chat so let me check chat now El Paso okay from Dallas area it's about like five hour driving Helena Georgia okay anyone else outside of us Peru okay Pakistan okay anyone else try Virginia okay anyone else okay so I think I'm quite far away from Dallas because I'm currently outside of us now but I guess I'm closer to Dallas compared to Pakistan So currently I'm at South Korea now so which is 6850 miles from Arlington and it also has 14 hour time difference So currently here as you can see on my laptop it's 11 pm so be mindful about my condition because usually this is my kind of like time but I try to put myself in Arlington right to teach this lecture I'm I'm very very glad and excited to teach this topic in this very very late night time it'll be more fun so what time over there in Pakistan zaheed just out of curiosity did you use your chat seven okay that's not bad it's have a good schedule to follow this one it's seven no age huh what was that sorry I missed your question no no I just asked what time over there so it's 7 00 p.m so that is a good time to follow this lecture that's all at 10 A.M in Atlanta I guess so all right so the today's lecture will be um will consist of three main parts the very first part lecture content one is Introduction to ml which is right now we're doing it so in this content one we're going to um clarify the objective of this boot camp with respect to the ml machine learning and then I'm going to like explain the introduction to ml and I would like to um summarize or some highlight or explaining the importance before learning ml algorithms so kind of bridging to the actual algorithms to the internet introduction slide and contents 2 which is ml algorithms so after 15 minute break we'll go through the supervised on supervised and reinforcement learning algorithms and no debt these are like kind of pick out the basic and easy to follow algorithms so that your journey is easy to start the ml Journey and the last component is the coding practice for ML which is the after lunch hour so we'll use the building energy data for learning classification algorithm you being KNN and decision tree okay so these are three main contents that I'm going to deliver today and these three contents are divided into the different lectures all right so before dive into the objective I asked chat GPT and I think everyone knows chat GPT right so I asked Che GPT what is the best way to learn ML and the chat GPT is basically answer almost exact that I would like to highlight in this first lecture so they said the very first one is start with the basic and the basic includes whatever you are familiar that are linear algebra crackless statistics and probability and those basic math skills are really really critical to learn machine learning in your journey and number two was take online courses like this course as well including this bootcamp courses but you can see many many other machine learning courses from Coursera edux udemy and these courses generally require your programming language like python or R and these are two popular um programming languages and I think I started with a Matlab but Matlab is not open source it's licensed in education is free but once you go to after graduation you may not have the like free license to on a Matlab so I highly recommend start your journey with the python or R and for this boot camp we're doing the python as our main programming language so the third contents the coding practice will utilize the python as your main language and they said they recommend it recommends books and research papers to follow up to the most recent algorithms and number four is I think very important practice with real world data set and the real world data set here means also you can download the open data set and also the area that are that you are interested in I think most of them are here are geology or Water Resource Management or building energy or hurricane engineering folks so for those are who are interested in arcade engineer or building energy the building energy data will be the good Target what or good data source to work on and really having those real data sets then you have a more fun and you'll be more into it to learn the machine learning algorithms and the fifth one is I also like this um join a community like Reddit or stack Overflow or GitHub those um you are not coding from scratch you're not coding the machine learning arguments from your by by yourself but you will probably almost highly likely use the already built libraries and even just utilizing utilize those already built-in library is quite hard so you might need some help from those Community to for your coding tasks so knowing where to search and how to search those algorithms using those Community is very very important thing so I would say those all fives are important and I extremely like the last kind of sentence so learning machine learning takes time and effort start with the basic be patient keep practicing good luck so that means like just taking this couple hour lecture today won't be enough um you have to like spend your own time about if you are interested in this field this lecture is literally just starting point of your machine Learning Journey okay so having said that our bootcamp objective is learning ml machine learning is generally by taking a course work courses so certain algorithms for example like auto-ship or network or convolution under a network they have their own designated courses to learn so check your institutions course list if you are particularly interested in a certain course and this lecture will not cover all the algorithms that you need to learn researchers even nowadays they currently develop very very actively and release their Arbiters in various communities like Reddit or like GitHub or stack overflow so checking out those state of Arts algorithms is very very important so that's why links to the chat gpt's recommendation join a community because you cannot learn everything something you are interested in you have to put yourself on those community and see what's going on over there and also everyone develops Advanced algorithms upon the basic ones for example you may heard the decision tree a having those decision tree the advanced one is a random Forest so understanding decision tree is important step to learn about the random Forest algorithm further on so just starting with a very simple basic one is sounds like easy but it's very very important step to further you identify what you want to do to know okay so that's kind of our first objective and we'll introduce some basic algorithms to begin your journey so for example k n algorithm K nearest neighborhood classification and decision tree and um it means clustering and the reinforcement learning technique those are very very very I'll I'll go through very basic steps on those things so that my intention is make you guys interesting about interested in in this ml so that you after taking this course you are devoting yourself or spend your own time to learn and study self-study by yourself and really a lot of self-studies are required and if you're if you're interested in this and if you want to learn on this and do not expect we'll cover every algorithm today we'll introduce one or two basic ones just like said for yourself learning okay all right before starting that any question on your objective and today is one today's lecture and concern and feedback so far then or do we have any chat questions no no chat uh questions you mentioned about two I mean three communities that I mean like we can join you said Reddit and stack Overflow and what was the third one third GitHub yeah that's it g-i-t-h-u-b yeah so people put their algorithms and their paper sometimes their own Repository and there are many others but these three are maybe first you can start with okay thanks for your first question all right so let me ask you some questions um and anyone tell me what is machine learning and what machine learning algorithms do you know if somebody put in a chat please speak out tenor or if you can just turn on your microphone and just speak out that it'll be better too I'll let you know if the question comes up yep just try I just want to know because machine learning is everywhere in use yeah I think um a simple um understanding is making your computer to understand um uh um or to learn how human being um do things or behave or kind of something like that nice good try what was your name okay Seth what was your name again Joseph Joseph yes great great thanks anyone else try what algorithms who have heard or you already know right I guess this is a good signal because we're going to cover these so you will learn and then you can answer this after this session and it'll be the good good good learning progress I think all right well that's one person had um mentioned that they so Joel posted in chat um I did some brief research on linear machine learning last semester I'm still a little confused about it though okay okay thanks for your opinion Joel so hopefully this will after taking this short lecture that will clear up otherwise we can chat up chat after this lecture too all right so here's our some um old sayings from very very establish researchers in computer science domain so anime touring in 19 50. instead of trying to produce a program to simulate the adult mind why not rather try to produce one which simulates the child's so see how Charles learn the new things and not just programming everything so just like there's a rabbit we're not I mean we sometimes explain how the rabbit look like there's long ears and short tails but rather than that just I have a three-year-old daughter and she saw so many rabbits from the news from the media or from reality and she realized or learned oh this is a rabbit if that looked like a rabbit then she just naturally understand or like like say that is rabbit nobody or I didn't or my wife didn't tell my daughter hey this is a remedy if there's a long ears and short tail and white bunny or great Bunny these are remedy we never try to do that that's almost impossible to all the things in the world so you just see it then ask it what it is and we repeat it it's a rivet it's a rabbit then they understand that's a rabbit so that's more like a learning procedure so I'll train during set produce one which simulate the child's learning like skills or something like that that's what Joseph's um answered on this so another um my old saying is field of study that gives computers the ability to learn without being explicitly programmed so it's same along with the previous saying or previous sentence and also the Joseph's comments so learn without being explicitly programmed so we're not telling how to do it but just giving the machine giving the computer to learn without those hard-coded on the learning procedure okay and more recently the professor from Carnegie Mellon Tom Mitchell said computer program is set to learn if it's performance on a task improves a good experience so he just pointed out or emphasized the importance of experience itself in a machine learning because really having the enough data and experience the end of data data driven way the machine or algorithm to learn how to classify or regress on their inputs so these are some old sayings about what is machine learning okay and I would like to introduce the ikw pyramid so here di KW as you can see in here it's a data information knowledge and wisdom so it is starting from the data so data is really fact or Rich by themselves there's no meaning so let's say you are like reading a letters and it's a data it's a textured data or it's whatever data currently there is no meaning but just its effect or just some simple truth simple like letters now the information is that which leads to understand the meaning we assign to fact so now you're reading those letters and you have some information to understand these facts that is information and once they are all the information are the synthetically aligned as orderly then we can say it's a knowledge like for example couple paragraphs or a couple Pages make up one book chapter to understand that or one book to the knowledge the last thing is wisdom which is inside the appropriate application of knowledge so you read a book then try to behave based on that book that the knowledge or the information that you learned from the book that's a wisdom that's your essentially insights on those data okay so really ml tasks are from data closer to wisdom so we are having the raw data everywhere and then we process this data to information knowledge and wisdom and we're trying to we're striving to wisdom but that's like very very hard challenging task if you can make a data to information that is a good enough for data to knowledge that's excellent data to wisdom that's it it can be like published in the nature or somewhere else so these are the ml tasks that we are trying to strive in the developing machine learning algorithms okay so any question at this point no question okay so here's my question then Tuesday machine learning is popular so like very very funny story about when I'm doing my PhD everyone say hey if your PhD dissertation has no data driven or machine learning then you will not pass so it's kind of funny joke that 10 years ago or 20 years ago in almost every engineering domain they said if you have to put micro or you have to assimilation in your dissertation but these days you have to put machine learning work data driven approach or data analytics in your paper so why why do you think machine learning or artificial intelligence is so popular these days with respect to this like d i k w pyramid can anyone have any guess or opinion my own understanding is that in this world they need our day of a lot of information data and this data need to be processed and um as a human being we are limited or confined to what we can say in a little while but um with the aid of programming and AI um a lot of information can be processed in a little time right so you're exactly true so I would say the most important Improvement these days is we have a lot of sensor networks and a lot good computing power systems so for example your cell phone keep collecting all the GPS data set or acceleration or your building or your car your house collects the temperature data or whatever data so everywhere we buy smart products and this smart product is they're highlighting that we have the sensor the sensor and we have the storage we are collecting this this amount of data so because of that data collection is so easily available so big enough we can start this ml task Journey so which is because data is the very starting point of ml tasks if we have no data for example like 50 years ago data was very very limited our house has no smart devices or our car has no smart devices our car was just press to Excel and just go that's all but nowadays it has so many sensors and that sensor is literally the data in newspaper we saw the newspaper these are all the letters facts but once the newspapers are digitalized archived in a computer format then now it's the data then we can process into information knowledge and wisdom so like you said Joseph because of we have so many availability about those big data that's the good starting point of or why it sparked the notion of the ml tasks very popular these days AI yeah of course I think the downside is the first one is a privacy issue broke Big Brother everyone like a monitored so the Privacy agreements and these should be protected at the same time from our own domain like for example my domain is a building engineering so when I was doing the research related to text mining in the building maintenance by one of my research paper was talking about people like writing about their complaints oh this building is too cold this building is too hot or I can smell really bad thing in my room so there are so many complaints Text data and then the previously before the AI developed like manually people read it and they assign the people to the HVAC engineer or I mean heating ventilation and air conditioning engineer or right type of engineer and assign those people to work on but these days they are automatically processed by Machine learning algorithms and then they will replace the physical Engineers using default detection algorithm more diagnostic algorithms and so on so they might like kind of stealing or replace the jobs that we conventionally have but at the same time like when the car mobile I mean the car industry was starting all the horse riders or those people are complaining don't steal my job but look because of car industry is booming they we have so many things like designer for car and the car navigation system or or the car related industry which is another like big um like booming or change the Paradigm of the industry in our domain so if you ask me is it only bad thing well I don't know how we will prepare on that so we if we are preparing well on that we'll create another new industry or new job field on that but otherwise like we will lose our like task by AI am I answering your question Joseph well because that was the second question I was supposed to ask but you answered everything and that was pretty good any other question from other students nothing yet tenor on the chat I don't see anything all right all right so let me continue I'll try my best to make you guys interesting and they give some voice on it all right go to next so we keep saying that data is super important and the very very very important starting point of ml tasks so how do we understand data for ML what kind of data can you see here can anyone answer what type of data you can see uh data by age data by age and age is string or numeric numeric right numeric so there are numeric data in age motor value and we have some classification in gender and policy type and Preferred channel some string values on occupation that can be also some classification we also have ID which is ordinary values so we have to see first um those data types we might have Text data dates binary ordinary category and numeric data so these are all the data types and features we can think of so feature is any measure derived from data that be used by the machine learning algorithms so raw features is raw data sources but you can also derive features like flag excuse me try features here means Flags ratios mappings Aggregates and others so let's back to our raw data source for example the for example occupation if you wanted to know like some only by lab tech then just put the flag on for the lab tech and flag down all the other jaw field outside of laptack okay and maybe age is like ratio values or some range of values so age range by less than 20 and over 20 something like that or in between 22 to 30 30 to 40 40 to 50. so if we if the ml algorithm just you utilize the raw data source then it's a raw age but if you are thinking of that too much the categorical of the age by their range is more beneficial on your algorithm then you can make a categories of your age same thing for model values and policy types and reference channels so we are going to almost cover the raw data features which is by the raw data but just converting those features I mean the raw data into feature is super super duper important in the machine learning task and here's the examples so let's say how to understand this image in your brain can anyone say about few words about when you saw this image what what can you think or how to understand this image in your brain not in computer I think generally when we see the color blue in nature like in this example we can tell that it's a sky and some sort of Lake and then yeah based on that we can infer like we can conclude that it's some sort of forest and a mountain range yeah your joy right yes good good you're almost like a computer thinking now any other now can you procedure this image in your brain let me rephrase the question how can you process this image in your brain yeah for me um what I can process for me the river flowing between two High point where you have vegetation the grain section trees and the pointed section which looks like a high mount I mean Rocky Mountains and by the right you have a lot of vegetation um green with the green uh that Express vegetation and towards the shore you have sand look like some kind of uh peach Resort stuff like that nice nice nice thanks for your input so let's see um so I think there are many many different ways to process these image in the computer like what you said Joel and Joseph it's more advanced the way like mimicking the human procedure but what they firstly start is basically they make a greed read like this and then and I just I cannot draw very very thin line so I just made it this way but oops this point think about this point if I have very very very small cell I would say that cell contains the three information RGB red green blue right and then they put 141 so every like color has that three components RGB so this one portion has one body 141 red 35 green and 31 blue just just I made it up and then it depends on how you procedure on it but here's an example algorithm is they make an average of these three numbers and put it here now this image is converted into a matrix or series of numbers in this grid so just converting this image data which human can understand put it into machine readable or Computing like computable format which is a series of numbers and then we can work on it so this is more on feature features that you can define it okay any question on this kind of procedure or how computer understand image data uh how did they come about the 141 142 143 red uh 35 36 green 31 32 blue yeah so it is really defined rules so let me to keep your included no Discord for example if I search Oops why my keyboard is not working color palette color search color sync utility no column finder no not this far what I mean is it like a standard procedure yeah it's a standard procedure I just wanted to show some apps that I'm using so basically it is agreement in the um visual artist or Computing visual artists so every caller has these three components of RGB so let's say like this one and then go to like color more colors red green blue so if I put I don't know I just made it up this example so 141 35 and 31. the color is like this did I answer your question Joseph uh yes yeah so these RGB is really defined by it's you know it's just whatever they they Define I mean the color is mixed with RGB okay and more advanced feature engineering is from RGB image they can see only depth of it or Surface normals or occlusion boundaries or segmentation mask so whatever you are interested in or whatever you want to focus more on then you can select different types of feature engineering you just pick out um whatever you want to so for example maybe segmentation mask is very very beneficial or very very helpful to detect the shape of the unique thing in this image right for example these keys I would say this key or what is this it's ice this is more on cups glass cups this is um I don't know whatever shape the flower shape things okay and if you want to know if you want to develop like tree detector algorithm then you might want to masking up these three portions to make it right that's how like Vision algorithms or Computing computer vision people are coming up with Advanced feature engineering okay and how about building energy data feature engineering so here's the one building energy consumption data so from zero kilowatt to 200 kilowatts and you can see from one day two three four five six days every day repeating so what are the important features to express in this data set in building energy data can anyone try can you repeat that the important yeah so yeah if you see this building energy data or profiles or patterns what is important features you want to pick out from this time series data I would say could it be like the Peaks where the yeah consumption is the highest yeah the Peaks that's good very reasonable and very very nice insights anything else um yeah you have uniform energy usage mm-hmm that's good and maybe the duration of that Peak cons I mean continues right that length will be the important features as well geomatical features so this paper is coming up with these energy consumption profile with only four letters a b a a and this day is ABBA this one is a CBA a c c a again AAA Acca and so on so every day it's not just like 24 points or more than 800 850 hundred I mean more than that points but they're coming up with only four letters because this is important features that this building energy domain research that wanted to know because they might be useful for understand building an edge consumption patterns each day what was the consumption pattern so because Saturday Sunday and Tuesday this was unique Tuesday because it's a January 1st which is holiday so that's why it shows AAA and if you know the Acca then you can understand these days are super important about the energy Supply so now each day energy consumption profile can be simply expressed by features for example these days are CCC cccb which is all day long very very high energy consumption pattern I don't know what day it is but you can check out if these cccb feature going on then that is a kind of problematic days that you need to check out there might be something wrong on your building energy consumption pattern some devices are over cooling or overheating like throughout the day that's a super important problem you have to check it out so converting the raw energy consumption pattern data into those four features will be beneficial for computing algorithms machine learning algorithms to detect what was the wrong day but it was a good day what is the best day and so on okay um I think you've kind of already gone over this a little bit but someone asked from the numbers is it able to find the type of features that you're looking for so the question was the the numbers can be features okay yes that number can be featured but the point here is this paper or this researchers try to make the feature as simple as possible to make a better ml algorithms for the important features to understand the shapes okay so that's about the feature engineering how to convert the data into the features for the beneficial way and before we're going to the each ml algorithm so here are some important notes about DML so a good ml model should provide a good generalization and that is no freelance ethereum it's very important there is no free thing you have to try it and see the results change the parameter run it again and see the results keep doing and doing and doing and trying better to find the good generalization which is a good ml algorithm because we want to avoid these two types of bias one is under fitting and I mean these bias can lead to one is under fitting and one is overfeeding so underfitting is modeled to simple simplistics relationships not captured well overfitting is model is too complex model becomes very sensitive to noise so here's an example um there's a age and income data set and for example age 21 24K and that point the first point h32 48 okay do you think this is underfitting or overfitting what do you think is it underfitting or overfitting under your fitting yeah why under fitting because I feel like the points are a little too far from that line yeah how about this one but they're fitting over fitting as well I think that would follow under overfitting yeah overfitting so it's really capture every data points right yes so go back to the definition here under fitting model to simple relationships not captured well which is this one right two simple line this is just a X plus b y equal a X Plus V but this is too complex to capture the relationship too sensitive to the noise this will be a good fit model good candidate right it is not very complicated but not very simple but captured good generalization model okay this is a good fit model so here's the example question um I think we don't have enough time to cover that but let me just really quickly go over so there is a model one a model two about outcome default repay based on the if and else statement and which of these two models will generalize better to instances not containing the data set propose some buyers that would enable a machine learning Arc to make the same preference Choice as you did in part A do you think the model I mean question number c do you think the model you rejected in part A is overfitting weren't defeating the Theta so there is a very complicated model in which is a model too and somehow simple model in model one so model one is likely generalized beyond the training data set because it's simpler and appears to capture the real pattern in the data and it features between a number of models that perform equally well prefer the simpler model is always better if you coming up with the Tuesday lecture it's all comes law always go to simple if both having a same performance rate and more on that model 2 is overfitting the data it tried to capture everything in a training data set that might results in some problem in the train I mean the testing data set okay so here's a bias and variance trade-off in ml so bias is error due to assumptions so high bias you have so many high bias on your data set then it will be the underfitting and more model does not capture sufficient characteristic of the data on the other hand the variance is error due to sensitivity of model so high variance here means overfeeding model captures noise and the data so we have to balance between these bias and variance trade-off in ml models to to identify a good fit model not too over fit not to underfit now the question is how can we evaluate and how can that we improve the performance of a given model that's the main question how to identify or how to identify the good fit model anyone try any idea okay so let's move on so the answer is we have to split our input data so let's say we have data of this one occupation age loan salary ratio and outcome is default or repay that kind of data set we got 100 rows or 100 data points now we have to split this data set into firstly we have to put the test data set which is hidden data set never seen data set as a side and then let's say from the Thousand let me redraw it here say we have thousand data point let's say thousand and hundred data points and we have to select 100 test set this is a pure data set pure test set that we will never use for our training and validation approach now we have to split this into 700 and 300. okay so we're going to use that 70 70 of the data for training and validation for 30 percent and training is just for training purpose validation is just for the compare models test is see the accuracy no model tuning anymore whatever we coming up with the right model that we're going to use this test set let me be verified and slow on this task if we giving the model complexity more complete complicated more and more than the training error will go down but what kind of problem that we'll have if we going here the generalization error will increase yeah and also the overfitting the the the graph that you saw that before that curve was very very complicated that was perfect perfectly working well on training set right but if you put some never seen kind of wild data set then the model was trained too much on this 700 data points so it may not good as good as your training set results on your testing set was it clear I can repeat that can you please yeah sure so let's say this one this was overfitting do you remember this and this was under fitting right and if we go more complicated model very very complicated model on your training data set which is a 700 data points if you keep learning and learning the model on those 700 then your model is perfectly doing well on this 700 data set right so that means you are training error on your training set is really decreasing the error is decreasing by complicated model but highly likely if you are too much on the 700 training set then if you put your model into your like hidden or never seen this 100 test set that might not work pretty well because this model is too much onto this 700 data set which caused the generalization error on the training set clear all now or still yeah it makes more sense now thank you yep how about others everyone good on this explanation tenor can you put yes or no on a chat and see how many thumbs up yeah it's clear okay so now it's a it passed the here the midnight so let me stop here and give a break and then let me continue from this point okay I have a question for you please go ahead please please I have a question um yes if um presently I'm an environmental engineer environmental engineering PhD uh student um if I want to build a career on the modeling aspect in order to enhance my career what what direction would you advise me to go into like where to study how to get my resources in order to like be a top-notch because whatever I'm doing I want to know it perfectly so you mean the modeling part is um more like a data scientist um yes okay environmental yeah so I think obviously um as a civil or environmental engineers my degree is civil engineering for example and my I choose my career path as academic career as assistant professor but my one of my lab mate who are doing very similar path as mine he is now a data scientist and a startup company I got some offer from the bigger company but he would like to pursue his own company to work on it so whatever whatever I observed from him was um he firstly he tries to build up his coding and his General machine learning skills obviously that's very very very common skill set these days in engineering PhD students but at the same time he tried to publish the paper with a more advanced algorithms even he can pitch his paper out the Cs communities about his ideas but at the same time we're not the coders or we're not the programmers we're not compete with them you have to see your environmental engineering like expertise or that your own like backgrounds how that is fitted to the data science domain that is more important so in his case he wants to like see how machine learning can apply to the demand response which is a building energy Distribution Systems so he tried to like speak out that machine learning like the the machine learning the algorithm itself can be developed by the building energy data it keeps emphasizing that so from the computer science domain it was very interesting because he understand most of machine learning terminologies and the algorithms but at the same time he can bring the building energy data sets to the machine learning domain so my it's a very long answer but my really important advice even my form for my page student you have to have your own backgrounds that you can bring it to other domains that nobody can compete with you [Music] does it answer okay it makes sense yeah so basic skill set you have to have but at the same time you have to have your own storyline from the environmental engineer perspective okay so I got the question from zaheed so I think that's why I decide to repeat this explanation again so let me share my screen all right so Tanner can you see my screen yes yeah yep so let me repeat here the bias error due to assumptions so high bias means undefeating this graph that you all picked out and variance error due to sensitivity of model High variance means overfitting model captured noisy in the data it's too complicated okay so these are one bias that various error so we have to balance between bias and variance errors so how can then evaluate and improve the performance of a given model that's the main question that we have so the main answer is we have to split our input data so let's say you got 110 oh no thousand hundred data set you have to put that 100 data set into the test set let me repeat again here so your input data was thousand hundred data points whatever you randomly pick that 100 tested should be pure never seen should be used at last end okay now you have a thousand you can split into 700 and 300. 700 on training set and 300 in validation sets okay so this blue line training error is keep decreasing by increasing the model complexity this means if you train your model over and over on this 700 then your error is going down because you are very very good at your training set it's overfitting but it has some generalization error once you go to this test set data set so your role is somehow identify when to stop what is the best in terms of good fit model okay so training is only used for train validation is compare model test is estimate accuracy so let's move on so first iteration you have this amount of test set and training set and the second iteration you have this amount of test set training set training set test set training set so in here this is not test but validation set so you keep changing the validation set all the time and keep iterating this procedure split and repeat so statistical method of evaluating generalization performance so you are training on these models and test on here you're training on these data set and test on here and training on thees and test here and training on these and tests here if you make a k equal 10 then you are splitting 10 different like randomly Shuffle the 10 different test data sets and like 10 different training data sets and your role is the first like run you are this amount is fold one was test set and this fault two to five was training set and fold one was training set fold two was stress set and just keep repeating that and this was 80 85 81 90 92 percent so you keep split test and training set randomly five times or ten times and then take an average in that way you will see what was true accuracy or true um more generalized accuracy of your model but let me back to this formal definition the more stable and thorough then using a split into a training and test set data is instead split repeatedly and multiple models are trained most common version is k-fold cross-validation which where K is specific number usually 5 or 10. okay this cross validation for example you repeat you split and repeat split and repeat split and repeat is a good choice of training a test set but provide the sensitivity of the model use data more efficiently but it's really computationally demand because you keep randomly Shuffle and train the model and test them out validate the model okay so it's not a model building but really the cross validation is just to see your how your result is good enough when you go to the final test set all right so this is all about the cross validation I know somehow overwhelming so let's let me have your questions on Cross validation please correct me like the procedure for the test set and the training set is same but we only changing the time span of the data set no it's not time span of data set but let's say whatever you have a thousand for example let's go this example the 700 and 300. so the very first run you put this amount is 300 but the second run you might want this 300 as a validation set right in the Third Run you input this 300s as a validation set and this run is validation set this one as a validation set and the last one is the validation set all different 300 combination on the splitting training and validation set to get the more generalized or more accurate accuracy or error rate of your model does it answer your question your zaheed right yes thank you and I have another question is like the higher biasedness is because of the error in Assumption so is always be an underfitting or can be a overfitting too like our assumptions can be like we are highly assuming something or sometimes can be we are under assuming yeah to on based off my knowledge and that type of your own error is we call it variance because you're too variant on your like data set so it's very sensitive about your data set and that kind of editor that you just mentioned is variance yeah [Music] thanks for correcting me any other question here I think this cross validation process is the most important step is the most important thing you have to learn even before learning the new ml models okay because sometimes people having the balls in an error debt they have a certain data set and they keep training and training and training model in d700 and that is always good because you train on this data set and you test on this data set that's always good computer works really well but the problem is you will have really wild your algorithm will go to Wild unhidden I mean hidden data set or unseen data set and to prevent that kind of error or doing really see the more reliable number on your errors or accuracy rate that's why we split into training and validation and keep split and repeat for the cabled validation like 10-fold that validation cross validation or five volt cross validation Okay so any question on chat Tanner uh none yet there was one question but you had already answered it I believe so okay cross validation everyone get the points or ideas I see I saw the Daniels here Daniel vomits do you think you got the cross variation concept the environments for Holy you guys are getting the concept of cross validation yes I got it okay sounds good this is very important if you're shy now just feel free to contact me about the crossbow Edition that's I really want to deliver I mean I think this is the most important what parts you have to learn in this I mean this Friday session cross validation the concept of cross-vitation basically all right let's move on the last portion before learning the ml algorithms evaluation of classification performance so let's say like how to evaluate your model that's the main question how to evaluate your ml algorithm model or ml models so we call it confusion Matrix for a binary Target called the positive and negative by convention so there are four possible outcomes prediction computers prediction as a positive and negative an actual positive and negative if the prediction was positive an actual label was positive then it's a true positive if it's a negative prediction and it really was a negative then true negative if the prediction was negative but the target was positive then false negative and prediction was positive and Target was negative then false positive okay let's move on so here's whatever ml algorithm and it detects either orange or not Orange so this is a confusion Matrix note that it was a prediction on column but now the prediction is a row but it just switched there's a two positive as 105 true negative as a 50. false positive as 10 false negative as one what is the accuracy can anyone come up with an idea to calculate the accuracy from this confusion Matrix what's the question again yeah so what is the accuracy can you calculate the accuracy using this confusion Matrix we can say uh accuracy true positive all over to that prediction okay percentage accurate okay close but not quite right would you have to include the true negatives as well that's correct so from the computer perspective the true positive and true negative which is this diagonal line okay is doing great job right it detects it wasn't range and it was orange and it was not orange and it was not Orange right so 155 divided by the total is 165 under 166. is your accuracy 99 yeah yes so this is how you can use the confusion Matrix to calculate the accuracy okay any question quite straightforward concept right yes okay so before I conclude the session one really this tabled cross-validation is important so let me do this ah cross validation is there any thumbs down here so let me ask cross-validation yes I know it uh please vote I know this hey tenor do you understand cross-validation from your end um I think I'm learning with you on this but I I understand it some yeah okay please vote on yes about Joel and uh Joseph Oli aksha C1 you got the right number 93 good okay you're increasing the number five kind of I I do feel like it's kind of checking the attendance now either you're just turning on the computer or not but really if you just logging in now and don't know what the heck going on then just put no then I can explain it across relation to you okay because this is super important concept no okay well no Daniel okay yes but it won't let me use emojis oh okay because you are in a guest mode okay nice okay two people a rate let me try again about the cross validation yeah I feel that Daniel all right so there's a two types of Errors one is on the fitting like this figure this function this is overfitting too sensitive about the data input and we need to evaluate and improve the performance of a given model to balance between these bias of various letter so what we can do here is we need to split and repeat this concept let's say we got 1100 data points that's input now you have two training set of now first you have to put 100 data points enough final test set final test set this is a final test set and this final test set means you put 100 you assign this hundred final test set you never touched that that's for final final accuracy estimate accuracy okay and you have to divide your thousand data point into 300 here for the validation set and 700 data points in your training set now if you learn the model out of this 700 keep all the time then obviously the training error will decrease because you have a certain book and professor said that all the exam will be on this book then if you study pretty well then you'll get 100 points so your error will go down and your model your brain is very complicated about that thing but let's say the professors decide to give a question from outside of the textbook which is this hundred and you might have some errors right all the it's outside of the problem bank for example bank that Professor provides you to avoid that kind of situation you have to have this 300 data sets split it and keep training 700 and 300 all the time so like here first you have a these amount training set and test set note that this is not final test set but this is a validation test set keep changing it changing it changing it and 80 85 81 90 92 percent and take the average in that way and see how it improved or not and see the world was the best in this way you can evaluate you can avoid basically this kind of error but you are testing your wild data set with the keep split and repeat with the stratified the training and validation splitting mode okay so that's the cross validation the main idea of a cross-validation it's super important in any machine learning algorithm development because it will like avoid or balance between variance and bias all right I think I did enough on the cross evaluation if you have any further question on the CrossFit feel free to let me know all right before we move on to ml algorithms anyone have any question on the first part [Music] foreign [Music] I think your microphone condition was not good so um yeah I can hear me now okay uh just a little question this is related their business uh similar to a sensitive analysis um no this is more on the cross validation how to train and validate your model I think sensitive analysis is really depending on what you want to do but uh I think this is no more sensitive analysis now falls into this category was it yeah okay thank you thanks Juan

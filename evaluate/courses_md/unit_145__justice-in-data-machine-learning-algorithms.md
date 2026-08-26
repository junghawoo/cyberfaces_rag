---
title: "Justice in Data: Machine Learning Algorithms"
unit_id: 145
course_id: 10
level: "Foundation"
slug: justice-in-data-machine-learning-algorithms
is_course: 0
---

# Justice in Data: Machine Learning Algorithms

## Extracted resources (local files)

### ML algorithms
*Source file:* `Lecture_Friday_2_Final.pdf`  ·  *type:* file

Machine Learning
Algorithms

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

Supervised, Unsupervised
and Reinforcement Learning

Classification of ML
●Supervised Learning
○Learn mapping from input to output
■Classification
■Regression
●Unsupervised Learning
○Learn patterns in the input
■Clustering
●Reinforcement Learning
○Learn to act from rewards in the absence of examples
■Decision making process

Supervised Learning 
●Modeling the relationship between measured features of data 
ad some label associated with the data; once this model is 
determined, it can be used to apply labels to new, unknown 
data.

Supervised Learning
We will cover knn and decision tree!

KNN (k nearest neighbor)

Main idea for KNN
●In dataset of example {x,y}
○Given input xi, 
○Find k examples that are nearest to xi
○Use these k examples for classification
○Classification: Use majority class of the k neighbors
●Question: what are ‘good’ values for k?

Example: KNN classification for earthquake

Example: KNN classification

KNN underfitting & overfitting issue?
High or low k for what problems?

KNN underfitting & overfitting
●Overfitting
○Low k 
○Perfectly classifies all existing data points
○BUT some data points can be outliers or noisy
○Decision boundary can become very complex

KNN underfitting & overfitting
●Overfitting
○Low k
○Perfectly classifies all existing data points
○BUT some data points can be outliers or noisy
○Decision boundary can become very complex
●Underfitting
○High k
○Everything will be classified as the most frequent class in the whole 
dataset

KNN underfitting & overfitting
●Overfitting
○Low k (k=1)
○Perfectly classifies all existing data points
○BUT some data points can be outliers or noisy
○Decision boundary can become very complex
●Underfitting
○High k
○Everything will be classified as the most frequent class in the whole 
dataset
●How to avoid such problems?
○Cross validation with varying k, and choose k with lowest cross 
validation error

Curse of dimensionality
●kNN works well in low dimensional space with plenty of data
●For high dimensions (>15), even the nearest neighbor is very 
far and not informative
N 
dimensional 
space

Understanding adaptive thermal comfort by KNN
Xiong, Lei, and Ye Yao. "Study on an adaptive thermal comfort model with K-nearest-neighbors (KNN) 
algorithm." Building and Environment 202 (2021): 108026.

Understanding adaptive thermal comfort by KNN

Decision Trees

Main idea for decision tree
●Figure out which features are the most informative ones to 
ask questions about by considering the effects of the different 
answers to the questions, in terms of
1.
How the domain is split up after the answer is received,
2. And the likelihood of each of the answers.

Main idea for decision tree
●A decision tree consists of 1) a root node, 2) interior nodes, and 
3) leaf nodes
●Each of the non-leaf nodes in the tree specifies a test to be 
carried out on one of the query’s descriptive features.
●Each of the leaf nodes specifies a predicted classification for 
the query.

Example: Decision tree
Which question would you ask first?
1. Is it a man? Or 
2. Does the person wear glasses?

Example: Decision tree

Example: Decision tree

Example: Decision tree

Predicting energy consumption by decision tree
Yu, Zhun, et al. "A decision tree method for building energy demand modeling." Energy and Buildings 42.10 (2010): 
1637-1646.
• A large dataset (e.g., RECS) is available 
for building characteristics and energy 
consumption
• There might be a rule to predict energy 
consumption pattern by buildings
• Decision tree is good enough to capture 
these rules to predict energy consumption

Other supervised learning algorithms
●Support vector machine
●Logistic regression
●Linear regression
●Naïve bayes
●Artificial neural network
●And many more…

Unsupervised Learning
●Modeling the features of a dataset without reference to any 
label
●It is often described as “letting the dataset speak for itself.”

Unsupervised Learning
When we are learning to see, nobody 
telling us what there might answers 
are. Instead, we just look.
(Geoffrey Hinton, 1996)

Unsupervised learning
●When we cluster the observations of a dataset, we seek to 
partition them into distinct groups so that the observations 
within each group are quite similar to each other, while 
observations in different groups are quite different from each 
other. No need for data labeling. 
●Challenges:
○No simple goal for the analysis such as prediction
○Hard to assess the results

Unsupervised Learning

K-means clustering
●Simple and elegant
●Partitions a dataset into k distinct, non-overlapping clusters
●To perform k-means clustering
1.
We must first specify the desired number of cluster k
2. Then the algorithm will assign each observation to exactly 
one of the k clusters.

How to choose k?
●There is no single right answer
●Sometimes it’s also problem dependent (e.g., looking for the 
best way to group the data into 3 clusters
●Some indices attempt to capture quality of clustering 
'elbow’ method using 
sum of squared error

Example: Unsupervised learning
Park, June Young, et al. "Apples or oranges? Identification of fundamental load shape profiles for benchmarking buildings using a large and diverse 
dataset." Applied energy 236 (2019): 1280-1295.

Other unsupervised learning algorithms
●Bisecting k-means
●DB scan method
●And many more

Reinforcement Learning (RL)
Reinforcement Learning might be considered to 
encompass all of Artificial Intelligence: An agent is 
placed in an environment and must learn to behave 
successfully. 
In many complex domains, RL is the only feasible 
way to train a program to perform at high levels.

Reinforcement Learning (RL)

Pavlov’s Experiment

Pavlov’s Experiment
Reinforcement learning in the built environment

Reinforcement Learning (RL)
•
Markov Decision Process (MDP)
•
Trial & error via interaction
•
Adapting to environment

Markov Decision Process (MDP)

Markov Decision Process (MDP)

Markov Decision Process (MDP)

Markov Decision Process (MDP)

Markov Decision Process (MDP)
What RL agent should do in a state?

Markov Decision Process (MDP)
What RL agent should do in a state?
Maximize the expected future rewards

Markov Decision Process (MDP)
What RL agent should do in a state?
Maximize the expected future rewards
RL: Define S, A, R, & P 
and solve MDP

•
People use switch as usual
•
Learn adaptive setpoints
•
Save energy consumption
Park et al., LightLearn: An adaptive and occupant centered controller for lighting based on reinforcement learning, Building and Environment, 2019
LightLearn: RL based OCC for lighting

State, Action, and Reward (engineering design)

State-action space design

1. Occupancy 
Occupied
Unoccupied
State-action space design

2. Switch position
Occupied
Unoccupied
Off
Off
Off
On
On
Off
On
State-action space design

3. Indoor light levels
Occupied
Unoccupied
Off
Off
Off
On
On
Off
On
Dark
Comfort
Bright
Comfort
Bright
-
State-action space design

4. Period of day
Occupied
Unoccupied
Off
Off
Off
On
On
Off
On
Dark
Comfort
Bright
Comfort
Bright
-
State-action space design

•
Avoid the curse of dimensionality
•
Transition probability (P) between 26 states 
Describe 1 day with 26 different episodic states

Penalty (-)
Neutral (0)
Reward (+)
occupant discomfort; energy wasting
energy consumption for comfort
occupant comfort; energy saving
Reward assignment

Control law for 
LightLearn operations
Calculate the optimal policy at every midnight

Optimal path for the maximum cumulative reward

Optimal path for the maximum cumulative reward

Optimal path for the maximum cumulative reward

Optimal path for the maximum cumulative reward

Optimal path for the maximum cumulative reward

Optimal path for the maximum cumulative reward

Implementation of 
LightLearn

0
50
100
150
200
250
300
82%
21%
Total operation time (turn-on hours)
LightLearn can save energy ($$$)

LightLearn is adaptive to different 
occupants via interactions
threshold for dark (lux)
experimental rooms

threshold for dark (lux)
experimental rooms
LightLearn is adaptive to different 
occupants via interactions

threshold for dark (lux)
experimental rooms
LightLearn is adaptive to different 
occupants via interactions

## Fetched resources (external URLs)

### Machine Learning Algorithms Pre-Survey (link)
*URL:* https://utaedu.questionpro.com/a/TakeSurvey?tt=Zqcjy8oIKPQECHrPeIW9eQ%3D%3D

[survey link — skipped]

### Machine Learning Algorithms Recording (link)
*URL:* https://www.youtube.com/watch?v=trJywgw1YUo

[YouTube transcript trJywgw1YUo]
so let's move on so the second part is machine learning algorithms so again this is with other instructors and prisoners and we went through the objective bootcamp introduction to machine learning before learning and algorithms that is cross-validation and configuration Matrix and the main part of a lecture two is supervised learning on supervised learning and reinforcement learning so how I organize this lecture contents too is I'm going to introduce these basic algorithms falls into supervised unsupervised and reinforcement learning and then give you some examples from my own domain which is a building energy so I think the building energy domain is quite easy to follow because it's our everyday life so algorithm Theory and then building energy example that's my concept on those explaining these algorithms in lecture three we'll use the building energy data for a learning classification algorithm using k n and decision tree so because I'm going to cover knnn and decision Tree in this lecture contents too so and the lecture content 3 is basically you utilize this k n decision tree knowledge into actual python coding okay so supervise unsupervised and reinforcement learning anyone heard about these words before joining this lecture anyone supervised on supervised and reinforcement learning getting a few notes in the chat do you know within a chat okay all right so let's begin now you hear about this term so this is basically two main classification of animal algorithm people say supervised learning and unsupervised learning and reinforcement learning is kind of combination or mixture of the two as the name implies supervised learning is something supervised something you need to have as a rule or as a label so you need to have the outputs or label to learn on the other hand unsupervised learning There's No Label it's unsupervised nobody supervise the outputs or label but it just gets the input patterns so learn the patterns and inputs that's clustering so supervised learning learning mapping from input to Output the main difference here is the output here okay so I'll put this is the main difference of supervised learning for the supervised learning algorithm either it's a classification or a regression you need to have output so that you can map or you can learn the mapping between the input and output on the other hand unsupervised learning there is no output it only contains the input but the machine learning algorithm will learn the pattern in the input normally we call it clustering in the other name the reinforcement learning is learn to act from rewards in the absence of examples so it's more like a decision-making processes okay so we'll go over the reinforcement learning later on but this is a main idea of classifying the ml algorithms any question on this point everything good I don't think I see any questions all right so let's move on so let's start with the supervised learning so as I said what was that you're good okay so supervised learning is you must have labels outputs targets and the modeling the relationship between features of data some labels associated with the data once this model is determined it can be used to apply labels to new unknown data okay let's say you have uh all the like weather data from previous days if the relative humidity if the temperature of your backyard is this this amount then it will rain in tomorrow or raining six hours later like that then you learn the model based on those weather station data then you can apply this model to predict either be rain or not for your future scenarios that kind of a supervised learning the very important point is labels or outputs in supervised learning there's a two classification again one is here's another classification so there's two types of supervised learning one is a classification and one is a regression okay can anyone differentiate between classification and regression I'll bring my water bottle so please type your ideas what is the classification and regression well I'm bringing my water bottle okay yeah from what I understand here classification is separating items into different uh um I mean items that looks alike you separate them from one another regression is looking at the relationship between items how um what they have in common how they um interact with each other if there is Ops if yeah if one item is influencing the order in one way property okay any other opinion if you have please type in I will bring my water bottle now okay okay I saw one opinion from Daniel Gomez regression is the average okay and I saw the hands up while I'm moving the one can you try yeah okay more related to Features better regressionally related data as it is okay progression is the relationship correlation between two data model OKAY action thanks everyone your inputs DNA classification is putting outputs into different sets while regression is expected pattern okay bully classification grouping regression continuous values oh okay I think holy we got the points all right so classification is more like a binary or the the classes that you want to classifying it so for example if you want to like predict either rain or not for tomorrow that's classification okay on the other hand regression is more on the continuous and numeric value so for example how much will rain or how much it will snow that's more regression so if it contains the numeric value so on the other hand [Music] um you will pass the exam pass or fail is that classification or regression classification classification right job how about your grades on ABCD is it classification or regression classification classification right how about your exam score like one two three four five six seven eight until ninety nine and hundred is it classification or regression yeah classification no that's right go ahead aksha I think it's regression yeah why do you think it's a regression because it's a continuous it can be from one to the maybe 99 yeah numeric values okay yeah so how about uh your um your temperature tomorrow on your city how about this Joseph temperature is it classification or regression temperature tomorrow your prediction picture prediction yeah it's a prediction but it's a classification problem or regression problem yeah because it's a prediction right and prediction on the numeric continuous values okay you got it okay about let me can you come up with the classification then or regression sorry Joseph one example about regression in your domain in your environmental engineering domain uh like um we can say the Stream flow value [Music] like um 100 200 Millennia per seconds and stuff like that otherwise yeah yeah that's good that's good and for example like uh let's say your um like from the sales domain like how much income or the net positive like from the sales on your company is it classification or regression about dollar amount your next year net income is it classification or regression that's immigration yes regression right right everyone clear on the classification regression someone had a question in the chat asking um is it regression because it's taking the past data into account for future predictions um no Daniel so it's a regression because our prediction is related to continuous numeric value so we are all taking into account the past continuous data but the important thing to kind of differentiate between prediction and regression is what is the output okay if the output is like ABCD or true or false or do or not doing it or like some categorical value then it's a classification but if our output is more numeric continuous numeric value then it's a regression problem foreign yeah did you get it Daniel good Five Points all right let me continue so the first algorithm that I'm going to introduce in the classification supervised learning is k n the full name is k nearest neighborhood the intention of selecting those algorithms is Simplicity and easy to learn because I like to make you guys all interested in machine learning and further study on this machine learning topic okay so here's the input data set which is a blue so you have no idea what is a label of this blue okay you have to check out three if I put k equal three this is a parameter that you need to decide and you check out your nearest Neighbors which is this this this from your general thinking how should I classifying this blue or node either orange or white yes try uh say that again yeah so let's say this is you okay okay and here's your close friends and one person I like soccer and two other friends says I like basketball and you guys are same kind of educational background and that's everything is kind of similar how should I say you like soccer or base basketball this blue input is either white or Orange okay yeah is it orange or blue or orange or white I I think it's orange why it's snail to me I think it's near to Blue yeah I'm not sure yeah so let's say using this way this is a y-axis this is x-axis and then x-axis saying air temperature y-axis saying world to immediately and if this is a like rain or not rain I don't know I just made it up this blue point is highly likely following these orange dots because very similar pattern data input they are doing the orange input right so your unknown blue should be orange that's the main idea of K and N so you have to specify Keiko one k equal to k equal three until k equal whatever number let's say this algorithm this specific example I choose k equal three we check out the nearest three neighbors this one this one this one oh I have a two orange and one white so this unknown input should be orange this is how K and N works make sense nah nope no okay so no nearest neighbor okay okay is known K is number that you are beside either three four five it's depending upon your engineering decision so let's say I select a three so three nearest neighbor I have to check out three neighbor nearest neighbor which is this this this and they want right class one is more orange class is more so my input is should be classified as orange orange okay okay okay so let's give me an example okay yeah so given input X I find K example that our nearest x i and use the dsk example for classification use a majority class of K Neighbors okay yeah because it's it's quite straightforward like you have similar things oops so it's a highly likely this will be orange okay all right so here's an example there's a two types of measuring the waves on your soil and these black dots are classified as these waves are like detected by nuclear explosions these white dots are earthquakes because of earthquake okay now your new input here you're checking out the K nearest neighbors K nearest neighbors and then if it's a k equal one then you can check out the what is the nearest neighbor and then classifying your input data as it is okay so this is the decision boundary of classification of the nuclear exposure this black area on the other end this white area is classified as earthquake okay to give me more example now the problem or question is I just randomly say this is a three and this example was what one and five what is a good value for k what is a good number to decide okay this is the problem in k n classification because depending upon what K number you decide your k n algorithm works better or worse so this leads to k n underfitting and overfitting issue I or low k for what problems so if I say k equal one is it underfitting problem or overfitting problem let's move on something to think if I put low k then it's overfitting problem okay because it's a very very perfectly classified all the existing data points but if you have some outliers or noisy and your input data is so sensitive about those outlier and noisy as you can see the decision boundary is very complicated like this so it's more like an overfeeding problem but on the other hand if you put ik right then it should be undefeating problem let's say you have thousand data points here you have thousand data points about your earthquake measurement and if you count down the Thousand data points then you will classify as just a one majority like data points but that is really essentially underfitting problem everything will be classified as the most frequent class in the whole data set there's no learning it just see the what was the major value and predict the military value so high K will create the underfitting problem okay so how to avoid such problems what was the answer what did I say what was the most important lesson I should give to you all cross validation so you have to cross-validate by changing K number k equal 1 to whatever number and keep cross-validated and see the lowest cross-validation error that's how you can come up with the K number okay any question so far can an underfitting overfitting problem I have yes regression analysis we have that integration coefficient which we find out how well our data is correlated but in that case how we find out we have the lowest cross validation error good question or something good question so that is going to so for example this type of problem we have two types of wave measurement and either that wave or that movement or that shake is by earthquake or nuclear explosions what is the accuracy here if computer classify earthquakes and actually earthquake then that's right right and if computer says hey I think based on this wave this is by nuclear explosion and it was really actually by nuclear explosion there is a right situation right are you following with me yes yeah but what is the the worst case scenario what is the wrong like situation from the machine learning perspective can you explain to me when majority of my data is either above the line or maybe the below of the line under or over fitting case maybe yeah yeah and in other words like if the shake was by nuclear explosions but if computers say hey this is by earthquake not nuclear explosion that's the wrong case right so it goes back to the lecture one which is the confusion Matrix so we need to increase this accuracy like you said the coefficient of correlation in your regression analysis we have to increase these accuracy classification accuracy using confusion Matrix by cross-validation so the simple answer here is you have to check out the accuracy by confusion Matrix which is a true positive and two negative rate based on your total data was it clear I think but the predicted energy actually is like the future observed and the future predicted are we are finding the correlation between both how much our model is accurately predicting these variables yeah so that is the our objective right your regression objective is how you our model is explaining the relationship between input and output right in classification your goal is how classify accurate thing like two positive into the negative so the accuracy here is really the the whatever you are referring in the regression analysis okay thank you yeah Okay so if you are unclear then we can discuss later on but let's move on so any question on k n underfitting overfitting okay let's move on so cursive dimensionality a n works well in low dimensional space with plenty of data for example if your two points are here and here their distance you can measure it quite easily and it's not very far away but if you have this point and this point and if you have adding another dimension this point and this point and if it's a multi-dimensional like four or four dimensional five-dimensional space for high dimensional space here means Dimension more greater than 15. the nearest neighbor is very very far away and that means it's not informative as it compared to low dimensional space so if you have so many features which means so many dimensions then K9 will not work very well as it works for the low dimensional space okay here's an example about using the k n in the building image domain so some researchers coming up with Raspberry Pi based robot and then putting some sensors temperature sensor or ultimately sensors and then this like small robot going moving around the the office buildings and check out the relative humidity and temperature and then ask people hey do you feel hot do you feel cold do you feel like normally comfortable those seven seven point answers and then in rule it is making a decision boundary based on the knnn algorithm to what is the right or ultimate air temperature based on their votes so in this case what is a label what is output label that KNE and algorithm used the label is the people's answers is it hot or cold they're answers this is their answers on the other hand their input is relative humidity and air temperature okay So based on these inputs they try to correlate the mapping between input and output all right any question on K N can in an algorithm anything on chat tenor I know right now no right now okay Joe are you good yes I wanted to know though the Canaan algorithm types are we just uh being introduced to them or are we going to be working them later on today we will work on these Canon algorithms using python okay yeah [Music] all right so the next question or next algorithm is a decision tree and I think decision tree is quite straightforward compared to KNE W so you might say that this kind of decision tree is it a mammal yes or no people keep it as a pet yes or no is it farm animal yes or no bird yes or no live in the ocean yes or no so that you can classify your input animals the main idea for the decision tree is figure out which features are the most informative ones to ask questions about considering the effect of the different answers to the questions in terms of how the domain is split up after the answer is received and the likelihood of each of the answers all right let's see it has root node interior node lymph nodes and each non-lift node is a tree specify carried out the descriptive features each of the lift nodes specifier predicted classification for the query all right so here's an example what question would you ask first to coming up with the better decision tree algorithm is it a man or does the person wear glasses I mean for the better decision tree algorithm I think the gender because it is is it because it's less specific okay good try anyone else had different opinion okay let's see together so the first if we choose does the person wear glasses yes no and only Brian applies into yes no for three is it a man yes no one versus two do they have long hair yes or no so the average number of question is 2.25 to get so Brian you only need a one question which is a wine to classify John you need to ask two questions to classify Afra or Alpha three question and three questions so in average you have to ask 2.25 questions but if I start with is it a man like a gender related questions and does the person wear glasses do they have a long hair yes or no only two for Brian two for John to for each then the average is only two questions so from the computational demand perspective or the most efficient algorithm or the most efficient algorithm choose the question of gender like you said so this is how I mean decision tree is quite straightforward but how to make this decision tree is based on the Information Gain that you will having the the shorter or average number of questions okay the question okay so the answer is a two the second question so decision tree is used in building energy domain so predicting energy consumption by decision tree because again like very first discussion Point there's a large data set is available in our domain in building energy so you we can build up the decision tree the classifying what is high amount of energy consumption low energy consumption patterns for example temperatures are high and these hlc Heat Ela these are all the building characteristics that you can ask and then you can build this kind of decision tree algorithm to predict the energy consumption by asking these questions outside of this decision tree and K non-written there are algorithms called support Vector machine logistic regression linear regression naive base and then artificial neural network and many more really people keep adding new supervised learning algorithm this portfolio so these are all there for your self-learning any question on the k n decision tree I have a question on a logistic regression yeah it's like uh I mean I have gone through like some like before this lecture like gone through some videos and try to get some idea about machine learning so the classification thing is clear to me whether like for example with the yes or no I can understand but how you can give uh value in logistic regression right can you just like simply explain how this algorithm works like in logistic regression yeah I'll try my best to simple explanation to you so it sounds weird it's logistic regression but really the logistic regression what it does is classification of zero or one so maybe that what you refer what you watched last time giving that confusion because it name is a regression but it's one zero so what it does is really legit curve and then draw the logic curve and either that is closer to zero or closer to one and then classifying is it closer to zero then it classifies a zero if it's closer to one then it's classified as a one so that's the simplest I can try but I would recommend watching the logistic regression video where I can send you the some some textbook that you can refer okay uh just one thing like uh logistic rejection gives like continuous values right but like you were saying about like sigmoidant function right something like that exactly but uh how can it give like continuous values from sigmoid where that was little bit confusing for me yeah let's talk about that after this like sure okay so what was your name again let me write it my name is muru okay m-i-y-u-r-u okay all right let's talk about that later thank you very much okay okay let's move on to unsupervised learning so unsupervised learning is different from the supervised learning does not have reference to any label it is often described as letting the data speak for itself okay so here's a training data set before in a supervised learning model it says these are blue labels or B labels B labels these are like a labels you put labels on the people the labels on the data set but in in unsupervised learning there's nothing there's no label like this b or a or b or c but just input data itself and then see what is a pattern of it that's the main idea about the um on surprise learning so one of the famous machine learning professor at U of Torino says when we learn when we are learning to see nobody telling us what their might answers are instead we just look just look at it and what is the pattern that's about the unsupervised learning so when we cluster the observation of a data set we seek to partition them into distinct groups like this partition them in a distinct groups because when you look at it when you look this training set you can intuitively understand oh maybe this is a group this is a group this is a group like this right this is a very intuitive process like see the patterns of it and the observations within each group are quite similar to each other while observations in different group are quite different from each other so you really no need for data labeling but just see the pattern and the grouping them based on their pattern but now here's a challenge no simple goal for this analysis there's no such thing there's no prediction rate there's no accuracy right because what is a label what is the right answer we're striving too so that means it's hard to access or evaluate the results there's a challenge of unsupervised learning okay any questions so far okay so here's a original unclustered data and you can cluster them into like this and let's say if you want to classify these data into group of two and maybe you can try this right if you want to group them three uh maybe like this and maybe you want to do in four then I don't know maybe like this so this is the main idea about unsupervised learning so here's a specific algorithm that I would like to explain it means clustering and it's a simple and elegant and partitions a data set into key distinct no overlapping clusters so to perform k-means clustering you firstly specify your desired number of cluster for example ko3 then the algorithm will assign its observation to exec one of the K clusters so for example here erase it again you put k equal three this is what you need like your K and N algorithm then you check it out your neighbors mean value of it and then you have to classify these points so these let's say these green mean value or average value points is here and blue average point is here and red average point is here let's say your new input is closer to here check out the distance to each Center points and this if this is a shorter distance and this new point is clustered as green okay so okay we must first specify the desired number of K then the algorithm will sign each observation to exactly one of the K clusters based on the distance to the center of each clusters any question on this procedure how we will find out the best value of K yep how to choose K that's exactly what I'm going to say so unfortunately there's no single right answer nobody knows sometimes it is depending upon your problem so if someone say Hey how do I cluster the data set into three good bad strange then that you you must put k equal 3. or high medium low then you must say okay go three but there are some indices to capture the quality of the clustering that's the sum of squared errors and there's other like silver scoring so there is couple scoring method and then it goes down these errors are going down because let's say you put 10 data sets and if you put k equal 10 then now it perfectly classified 10 data points into 10 group because it's a 10 individual input data but what's wrong in here actually can you imagine what's wrong in here no I'm not understanding yeah so let's say there are 10 data let's say we have a hundred data point input data let's go back here imagine that these all blue dots are 100 data points number of data points and if you put k equal 100 then it will perfectly classify these hundred data points into 100 groups because that's all individual groups but there is no point of clustering that right the the reason we are using on supplies learning is we want to grouping them by this certain smaller number so having said that if you put the higher number of cluster let's say k equal 10 or k equal 100 or whatever then your errors will decrease but at some point if you have so many low or so high number of K then there's no point of clustering that so some people say we need to use elbow method this is a shape like your elbow like your arms put it in the somewhere here and then pick up these elbow plot or elbow spots and then say Oh three is a good number or someone say five and five is a good number this is related to no free launch theorem you have to check out three and five and see how they are good at it in terms of their the unsupervised learning results no free lunch oops am I answering your question so simple answer here is there's no perfect word the best optimizing way to choose a k it really all depending upon what is your interest but one index is more more K number will decrease the errors all the indexes but if we put higher number k then it's not a like there's no point of clustering that so you have to balance by these kind of elbow method or keep trying and see the results is it clear to you or other students is it clear to you a number uh yes okay so if you can specify which part is unclear in K number then I'll try to answer it over the break how about that haksha it's clear okay okay thank you people said yes in the chat oh okay sorry sorry to see the chat so Tanner Your Role just tell me okay no worries yeah all right so here's some example about using unsupervised learning and uh building energy domain so the main idea about this paper is they try to Cluster the building energy profiles and then try to Cluster those energy profiles into the shape and grouping buildings by their shapes so conventionally we are saying hey there is a school building there's office building there's a factory building that kind of classification is good but it's not good for the energy distribution system the better way is building a is noon Peak or Building B is a is like morning Peak Building C is my evening Peak if we can classify buildings by their patterns and it's a lot better in terms of energy distribution system developing the energy distribution system so the main idea here is we clicked around thousands and thousands and thousands of building energy consumption profiles which is a daily profile and then apply k-means clustering bisecting k-means and GMM clustering algorithms and then with the increasing by K number two to three until K number 10. so like I said there is no optimal way of selecting K so what we observed here is when we choose k equal 3 and K means cluster and logarithms then the results make sense to us from the electrical distribution companies point of view so that's why we select the cable three and K means so this is going back to what Joseph's questions machine learning is something skills but make it this one meaningful is putting your own domain knowledge in that way you will use the machine learning poorly or completely for your own tasks so in this case there's no mathematically find out the right number of K so we try various things and then choose the k-means and k equal 3. so this is the results of G1 and G2 G3 of the K clusters and compare that with the conventional way of building clusters and other unsupwise learning algorithm is like I say bisecting k-means or DB scan method or the GMM method and many more okay any question on unsupervised learning algorithm so I think the main key takeaway lesson here is the difference between supervised and unsupervised learning and that is the existence of labels and because supervised learning has the labels it tries to map being the between inputted output on the other hand unsupervised learning they don't have any mapping or inputted output I mean output itself so it is just a pattern of input data itself okay let's move on for the reinforcement learning so supervisor learning you have input and you have outputs and see the labels and then based on that error you can train a model on supervised learning there is only input and say the patterns and show the outputs on the other hand reinforcement learning is a reward it's not label itself but it's a reward some sort of reward signal to the ml algorithm to train and based on that reward not the outputs like supervisor learning but it's just a reward then it train itself let's move on so reinforcement learning is Agent based modeling so there's an agent and do some actions to the environment and then get a reward and States from the agent and keep iterating this then agent will adopt to the environment and reinforcement learning is getting popular these days and it's its own field so I highly recommend this book to learn more about if you want to know more about your own personal learning it's quite cool method and you may remember the Pavlov's experiment so there is a if you ring a bell and give a food to dog or dog and later on you just ring a bell and the dogs start to save ready to eat food similarly if you want to use the reinforcement learning in the built environment for example building control the human gives the signal to the Computing agent hey your automatic decision was wrong or hey your automatic decision was okay if we if humans can give this kind of this reward to the Computing system or reinforcement learning agent then based on that reward it will ultimately learn what you like and what you don't like and take an automatic action for the building control that's the main idea and reinforcement learning as I said agent do an action and get a student reward and it kept iterating this trend error and then finally the agent will adapt to the environment and it is formalized by Markov decision processes which is mdp this is a mathematical format of expressing your decision-making processes so here I explain the MVP in detail so let's say I have a car and my car can get three states one is good shape one is not good shape and one is a broken okay and we can do some actions either maintaining or ignoring it based on that action you have on reward for example you repair decision as a reward of -10 because if your car is broken and repair into good shape you have to spend so much money that is -10 your action will maintain go to like car shop and maintain your car that is a less cost but still minus one reward if you just ignore your condition then it's a zero nothing happened but if action is ignore and if the car isn't broken then you can get some minus two and then some there is some probability between how your good shape you're gonna go into what conditions okay so there's a states which is the three states that we mentioned actions like for example in word I mean the actions as your repair or ignore maintain reward how much you spend money and transition function is the probability between zero and one now what RL agents should do in a state Here Comes what you should do for your car maintenance you want to maximize the expected future rewards that means to maintain your car in a 10-year plan or 20-year plan you want to minimize your expense on your car while you're like maintaining good condition about your car so that's exactly same what RL agent does in here it tries to minimize maximize the expected future Rewards or minimize your penalty terms in the future so in RL problem you have to Define State action reward and probability and solve these mdp Markov decision processes is what RL task does okay so since I have short amount of time let's go to the building example so here is one example about light learn which is a reinforcement learning based occupancy control for lighting so this is a very conventional light switch toggle switch up and down and it monitors the light levels and has a Computing in here which has a reinforcing learning agent so people use their light switch as usual and but the light learning will adapt learn the adaptives at points and save energy consumption so you basically monitor how people use the light switches and do some automatic actions to the environment and if person occupant like their automated decision then they'll stay there just working that means it's a positive reward but the person doesn't like the automated decision by light learn then he or she will stand up and take override the automatic decision and that is a penalty to give the lighter and light learn have some labels like supervised learning but reward of the negative reward and then try to update these for the future decision so State and action reward is engineering design processes it monitors either person is occupied a space or Not by Bluetooth signal and either the light switch is on or off and if indoor light level is dark Comfort bright and then the period day is um sunset time or sunrise time or midday time or a completely dark time so now we can describe our one day with the 26 different episodic States so that we can calculate the transition probability of that and now we give the penalty term neutral and positive reward when occupant is comforted energy saving for the poly reward and when occupant is discomfort and you're wasting then penalty reward this is a math function so let me go here this is a one day cycle of how light learn works for the with the occupants so at 9 30 occupant is unoccupied and it he enters the room and it was a bright condition then goes out then coming in again at 10 40 10 39 then it goes a dark condition because of the like condition cloud cover so light learn immediately turn on the lights go here and then person just leave the room without turning off the light so light learn decided oh it's a like negative reward or penalty because it's energy wasting so it decide to turning off the lights they go to comfort mode coding here and go to turn on the T turn on the lights keep doing it so this is a one day cycle and from the light learn the reinforcement learning agent's perspective the daily cycle it just play with its occupant so it turn on or turn off by automatic decision and how CD how the reaction from the occupants and the predefined rewards keep playing this every day game with the occupants and the light learned agent it will decide where it will learn the ultimate policy or ultimate rules to control the the light switches to maximize the cumulative reward which means maximize the occupant Comfort while saving unnecessary energy consumption this study tested this light learn with the five different offices five different occupants and obviously it saved the energy consumption based on the conventional like control stereotages this is one of the control parameters as you can see until day 10 they're fluctuating what does that mean that means the light learn is learning and keep iterate interacting hence and just occupants stand up and override the system that's why keep fluctuating control parameters but after 10 days it's kind of stabilized that means it learned the rule it learned the right rules to turn off and turn down but in this occupant B has a some sensitive questions on that but polite learned immediately captured this mood change and then tried to like stabilize and learning the the new patterns of it Okay so that's all I prepared and it's 145. I know it's kind of rushed but if feel free to take a break and this is a lunch break until one hour from now on but I'm more than happy to have any questions at this point all right so the lecture two is over feel free to ask me any question or if you don't have feel free to go for lunch break thank you Dr Kirk yes I had a question about that graph mm-hmm because you said the like on the right near the end where the Orange Line starts changing yep that has to do with the user so these are five different offices in Austin Texas and this was excuse me this was five different people so at the very first 10 days it kept fluctuating and after 30 days we believe that light learned the rule from these people but this occupant B didn't use the light learn at the very beginning but she started to use this weird artificial intelligence after 30 days that's why it shows some fluctuation here and light learn like lately later learned they speak in mind on these days does it answer your question yes that makes more sense thank you yeah any other question or everyone going for the lunch

# Binary Class Classification (NASA and Space) on Reddit data using NLP

Check out the below sentences. It is hardly possible to differentiate between sentences from NASA and Space community. However AI does differentiate sentences easy! In this project, new feature engineered data, boost AI estimation accuracy from 75% to 96%. AI amazingly does such complicate tasks.

```
A) A star shining through Saturn's rings.
B) Online space-related degree.
C) M1: The Incredible Expanding Crab Nebula.
D) Took this with a camcorder since I don't have any fancy telescopes or nothin.
E) I went to ksc for Christmas and got to see what made me interested about spaceflight.
F) I went to the John F. Kennedy Space Center.
```
The A,C,E,and F senteces are from NASA community and B and D are from Space community.


### Project Name
Binary Class Classification (NASA and Space) on Reddit data using NLP


### Description
Space was always my passion and I love observing stars, galaxies, solar systems with binocular.
The [NASA](https://www.reddit.com/r/nasa/) community is for anything related to the National Aeronautics and Space Administration; the latest news, events, current and future missions, and more.
It has 1.3m Members with 282 IN SPACE and it was created on Jul 17, 2008.
The [Space Discussion](https://www.reddit.com/r/space/) is a community for sharing & discussing informative content on: * Astrophysics * Cosmology * Space Exploration * Planetary Science * Astrobiology. It has 17.2m
Members, 5.0k Online, and it were created Jan 26, 2008.
The goal is to develop a binary class classification that would be able to recognize the Nasa community from Space Discussion. 
These two close categories were selected to rise the challenge and see how close AI can get using common ML algorithm libraries in python.




### Table of Contents
The project directory tree structure is provided below.
```
├── Assets
├── Codes
│   ├── Models
│   ├── P01_Gathering_Data.ipynb
│   ├── P02_Cleaning_Data.ipynb
│   ├── P03_Exploratory_Data_Analysis.ipynb
│   ├── P04_01_Modeling.ipynb
│   ├── P04_02_Modeling.ipynb
│   └── P04_03_Voting_Modeling.ipynb
├── DataSet
├── Figures
├── Functions
├── Images
├── LICENSE
└── README.md
```

### Installation

* To run this project you need to have python installed on your local machine. At the moment the project does not come with the env but I will make an env using conda and will add it to the directory. check for updates.  Also, I may provide a docker image for this project too. So stay tuned!
I also prepare a medium about how you can use docker image and Jupyter notebook [here](https://medium.com/@atashnezhad1/in-this-tutorial-we-will-learn-the-very-basics-of-running-the-jupyter-notebook-using-docker-9b347c9058d9).
* List of my global libraries is provided as ```requirements.txt``` file in the env folder, therefore you may use ```pip install -r requirements.txt ``` to install all necessary libraries with no hassle.

* Also use following to find the executable whenver you had hard time to install libraries.
```python
import sys
print(sys.executable)
```
Then use following to install favorite libraries (i.e. wordcloud).
```python
!/Users/amin/anaconda3/bin/python -m pip install wordcloud
```
I used it several times in Part_03 of this project and it works like charm!
### Instruction

#### Gathering data 
Data was received using the API from the Reddit website for two categories. I used my friend [Saied](https://github.com/saiedmighani/Global_warming_NLP_analysis/blob/master/assets/get_reddit_posts.py) function with a little bit of change to receive data from Reddit. You may check out the original function [here](https://github.com/scaress21/reddit_and_quibi/blob/master/code/01A_Gathering_Reddit_Data.ipynb).
the data was save in two formats .csv and .pkl.

#### Cleaning data
Data included 10-15 columns with one column with Reddit comments as text. The NaN values were filtered and the text was cleaned using a series of functions including tokenization, splitting, snitching, removing stop words, stemming, etc.

#### Exploratory Data Analysis
Analyzing the data, It was observed that both categories are pretty close. Space has a higher percentage of 'link', 'rich:video', and 'self' while Nasa has more 'image' numbers.
NASA has a lower average word count compare to Space with a smaller standard deviation. Both subcategories are pretty close in terms of word count. However, the space category has some long texts above 500. For the sentiment score, it is observed that both mean and std are pretty close. It seems both SPACE and NASA forums are pretty close.  It is seen that the negative sentiment scores for space are a little bit higher than NASA. People who are in NASA discussion have a more positive attitude compared to people who are in space discussion.

#### Named Entity Recognition (ner)
Named entity recognition is an information extraction method in which entities that are present in the text are classified into predefined entity types like “Person”,” Place”,” Organization”, etc. Using NER we can get great insights into the types of entities present in the given text dataset. A powerful correlation between enr and target values was observed.

<p align="">
  <img src="Figures/plot_03_19.png" >
</p>

#### New Featured  Data
Following columns were selected and save seperatly as EDA data frame.
```
'ent'
'word_count*' 
'sentiment_score*'
'polarity_score'
'polarity'
'polarity_VSA' 
'text_complexity'
```
It was observed that there is a strong correlation between parameter 'ent' and classes which are promising.
EDA data frame corrolation is seen at the following figure. 
<p align="">
  <img src="Figures/plot_03_26.png" >
</p>

Three set of data frames were prepared including count-vectorized texts, EDA data frame and, merged count-vectorized text and EDA data.


### Modeling-ML algorithms

Logistic Regression, Gradient Boosting Classifier and, MLP Classifier were applied. Algorithms were grid-searched to find the best hyper-parameters and improve the accuracy.
The voting system included three best models along with hyper-parameters were applied which results in maximum accuracy of 96%.
It was observed that using only vectorized text results in lower accuracy compared to the EDA data set. Also using merged data set results in top accuracy. 
Check out the following confusion matrixes. The left one is using Logistic Regression on vectorized data while at the right the Soft voting model used on All_df.
<p align="left">
  <img width="400" src="Figures/plot_04_1.png" >
  <img width="400" src="Figures/plot_04_03_2.png" >
</p>


- Progress in modeling accuracy is seen in the following figure.
<p align="">
  <img src="Figures/plot_04_03_4.png" >
</p>

  

### Conclusion

The best model is the soft voting model including the three best ML algorithms which were achieved through grid search.
In this project, a new set of data were extracted which later used for modeling. The analysis shows that a new engineered set of data (EDA) shows higher accuracy and boosts the ML algorithms.
Merging both vectorized text and Engineered data set (EDA) even helps more and boosts the accuracy above 80%.
Finally having an ensemble model works the best with an accuracy of 96%.
```
|    | model_name                         | data_set_used     |   accuracys |   TN |   FP |   FN |   TP |
|----|------------------------------------|-------------------|-------------|------|------|------|------|
|  0 | LogisticRegression                 | CountVectorizer   |       0.756 | 1186 |  310 |  421 | 1083 |
|  1 | GradientBoostingClassifier         | CountVectorizer   |       0.736 | 1288 |  208 |  578 |  926 |
|  2 | MLPClassifier                      | CountVectorizer   |       0.752 | 1149 |  347 |  381 | 1123 |
|  3 | LogisticRegression                 | EDA_df            |       0.82  | 1456 |   40 |  495 | 1009 |
|  4 | LogisticRegression                 | EDA_df_normalized |       0.832 | 1496 |    0 |  504 | 1000 |
|  5 | GradientBoostingClassifier         | EDA_df            |       0.831 | 1495 |    1 |  504 | 1000 |
|  6 | GradientBoostingClassifier         | EDA_df_normalized |       0.831 | 1495 |    1 |  504 | 1000 |
|  7 | MLPClassifier                      | EDA_df            |       0.824 | 1470 |   26 |  491 | 1013 |
|  8 | MLPClassifier                      | EDA_df_normalized |       0.832 | 1488 |    8 |  499 | 1005 |
|  9 | LogisticRegression                 | All_DF            |       0.828 | 1458 |   38 |  476 | 1028 |
| 10 | MLPClassifier                      | All_DF            |       0.844 |  nan |  nan |  nan |  nan |
| 11 | GradientBoostingClassifier         | All_DF            |       0.878 |  nan |  nan |  nan |  nan |
| 12 | Hard_voting_lr_GB_MLP              | All_DF            |       0.921 | 1481 |   15 |  220 | 1284 |
| 13 | Soft_voting_lr_GB_MLP              | All_DF            |       0.954 | 1491 |    5 |  101 | 1403 |
| 14 | Soft_voting_lr_GB_MLP_different_HP | All_DF            |       0.959 | 1493 |    3 |  128 | 1376 |
```


Here are the classification models ROC curves developed in Part 04 of this study.
The voting models are not included here. It is seen the best models are achieved using merged data frames (EDA and vectorized data from text). The ANN and logistic regression have the best performances. Also, it is seen the EDA data frame boosts the model predictions. Comparing the Normalized EDA with EDA, it turns out that using normalized EDA improves the performance of models.

Three models including, xgboost (using normalized EDA data frame) and ANN (tuned hyper-parameters and using EDA/and Normalized EDA) are in the 3d rank.

<p align="left">
  <img width="650" src="Figures/plot_05_ROC.png" >
</p>


<!-- 
<p align="center">
  <img src="Figures/plot_04_03_5.png" >
</p>

-->








### Suggestions

TFIDF vectorizer can be studied and see if it helps the accuracy of models.
In voting ML algorithm more model can be introduced which it would help for sure.



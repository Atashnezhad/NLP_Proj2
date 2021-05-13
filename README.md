

<p align="center">
  <img src="Images/IMG1.jpg" >
</p>

# Binary Class Classification (NASA and Space) on Reddit data using NLP

### Project Name:
Binary Class Classification (NASA and Space) on Reddit data using NLP


### Description:
Space was always my passion and I love observing stars, galaxies, solar systems with binocular.
The [NASA](https://www.reddit.com/r/nasa/) community is for anything related to the National Aeronautics and Space Administration; the latest news, events, current and future missions, and more.
It has 1.3m Members with 282 IN SPACE and it was created on Jul 17, 2008.
The [Space Discussion](https://www.reddit.com/r/space/) is a community for sharing & discussing informative content on: * Astrophysics * Cosmology * Space Exploration * Planetary Science * Astrobiology. It has 17.2m
Members, 5.0k Online, and it were created Jan 26, 2008.
The goal is to develop a binary class classification that would be able to recognize the Nasa community from Space Discussion. 
These two close categories were selected to rise the challenge and see how close we can get using common ML algorithm libraries in python.

### Table of Contents:
The project directory tree structure is provided below.
```
├── Assets
├── Codes
│   ├── Models
│   ├── P01_Gathering_Data.ipynb
│   ├── P02_Cleaning_Data.ipynb
│   ├── P03_Exploratory_Data_Analysis.ipynb
│   ├── P04_01_Modeling.ipynb
│   ├── P04_02_Modeling.ipynb
│   └── P04_03_Voting_Modeling.ipynb
├── DataSet
├── Figures
├── Functions
├── Images
├── LICENSE
└── README.md
```

### Installation:

* To run this project you need to have python installed on your local machine. At the moment the project is not come with the env but I will make an env using conda and will add to the directory. check for updates.  Also, I may provide a docker image for this project too. So stay tuned!
I also prepare a medium about how you can use docker image and Jupyter notebook [here](https://medium.com/@atashnezhad1/in-this-tutorial-we-will-learn-the-very-basics-of-running-the-jupyter-notebook-using-docker-9b347c9058d9).
* List of my global libraries is provided as ```requirements.txt``` file in the env folder, therefore you may use ```pip install -r requirements.txt ``` to install all necessary libraries with no hassle.
* 
### Instruction:

**Gathering data:** 

Data was received using the API from the Reddit website for two categories. I used my friend [Saied](https://github.com/saiedmighani/Global_warming_NLP_analysis/blob/master/assets/get_reddit_posts.py) function with a little bit of change to recieve data from Reddit. You may check out the original function [here](https://github.com/scaress21/reddit_and_quibi/blob/master/code/01A_Gathering_Reddit_Data.ipynb).
the data was save in two formats .csv and .pkl.

**Cleaning data:** 

the data included 10-15 columns with one column with reddit comments as text. The NaN values were filtered and the text was cleaned using a serious of functions including tokenization, splitting, snitching, removing stop words, stemming, etc.

**Exploratory Data Analysis:** 

The main data frame was analized and following were observed.

- It is seen that both categorise are pretty close. The Space has higher percentage of 'link', 'rich:video', and 'self' while Nasa has more 'image' number.
- Again It is seen that both categorise are pretty close in term of 'over_18'. higher number of people in space answered 'False' to the column 'over_18'.
NASA has a lower average word count compare to Space with a smaller standard deviation. let's look at the plt.hist and compare it with space. similar plot provided above but here bar plots are side by side.
- It is clear that both subcategories are pretty close in terms of word count. However, the space category has some long texts above 500.
- For the sentiment score, it is seen that both mean and std are pretty close. It seems both SPACE and NASA forums are pretty close! Let's plot both NASA and space.
- It is seen that the negative sentiment scores for space are a little bit higher than NASA. People who are in NASA discussion have a more positive attitude compared to people who are in space discussion. Let's double check it and do the summation of sentiments for both space and NASA. Also, the Space has more words compare to NASA.
- Let's focus on text and do count vectorize on data. Three steps are taken as follows:
  - Add some stop words to the general list
  - Apply the new list of stop words list (extend)
  - Apply count vectorize to the data

- Lets see the top words in NASA, SPACE and then see the top overlap words.
  - As it is seen these two topics are very close! The top words for NASA are space, earth, NASA, moon which have three out of four similar to space.
- Number of characters present in each sentence
- Average word length in each sentence. Again both topics are pretty close in term of average word length and number fo characters.
<p align="">
  <img src="Figures/plot_03_10.png" >
</p>

- Inspect which words other than stopwords occur frequently.
<p>
  <img src="Figures/plot_03_11.png" >
</p>

- Topic Modeling exploration with pyLDAvis.
  - The unsupervised correctly detect two main subjects as we expected (high coffs for NASA and Space). NASA and Space!
- Textblob librarie. sentiment polarity was applied.
- Vader Sentiment Analysis was applied too. Vader works better in detecting negative sentiment.
- Named Entity Recognition (ner). Named entity recognition is an information extraction method in which entities that are present in the text are classified into predefined entity types like “Person”,” Place”,” Organization”, etc. By using NER we can get great insights about the types of entities present in the given text dataset. A powerful corrolation between enr and target values was observed.
<p align="">
  <img src="Figures/plot_03_19.png" >
</p>

- Exploration through Parts of Speach Tagging in python.
- Exploring through text complexity.
<p align="">
  <img src="Figures/plot_03_24.png" >
</p>
Again it was observed that both categories are match in term of complexity.
<p align="">
  <img src="Figures/plot_03_25.png" >
</p>

- Following columns were selected and save seperatly as EDA df.
  - cols = 'ent', 'word_count*', 'sentiment_score*', 'polarity_score', 'polarity','polarity_VSA', 'text_complexity'

- EDA df corrolation is see at the following figure. Again it is observed that there is clear coorrolation between ent parameter and target.
<p align="">
  <img src="Figures/plot_03_26.png" >
</p>

- Three set of data frames were prepared including count-vectorized texts, EDA data frame and, merged count-vectorized text and EDA data.


**Modeling-ML algorithms:** 

- Several ML algorithms applied to three set of data frame.
- It was observed that using only vectorized text results in lower accuracy compare to the EDA data set. Also using merged data set results in top accuracy. check out the following confusion matrixes.



<p align="">
  <img src="Figures/plot_04_1.png" >
  <img src="Figures/plot_04_03_2.png" >
  <img src="Figures/plot_04_03_4.png" >
</p>

<p align="center">
  <img src="Figures/plot_03_27.png" >
</p>

<p align="">
  <img src="Figures/plot_03_11.png" >
</p>



<p align="center">
  <img src="Figures/plot_03_14.png" >
</p>



<p align="center">
  <img src="Figures/plot_04_12.png" >
</p>




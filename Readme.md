## P6.  Titanic Data Visuvalization by Gangadhara Naga Sai

### Summary
1.The first plot ,shows us a decreasing trend of survival rates from children to senior individuals.

2.The second plot,shows us the higher survival rates for individuals accompanied by families.

3.The third plot,reflects us "children and women first" ,as they are given preference over men in general.

### Design
I Select the Titanic dataset since its for begginer and no data wrangling is required.
#### Overview
In 1912, the ship RMS Titanic struck an iceberg on its maiden voyage and sank, resulting in the deaths of most of its    passengers and crew. In this project, we will explore the RMS Titanic passenger manifest to determine whether someone survived or did not survive.Demographics and passenger information from 891 of the 2224 passengers and crew on board. 

From the data exploration the data sets are are filtered using numpy and pandas library of python and saved as .csv files ,P2.py code 
upon running will produce all the required datasets.P2.py is available in "data" folder and after running all the datasets will be created in data folder itself.

data visuvalized:
1. Survival Rate vs Age
2. Survival Rate by Number of parents and children of the passenger aboard
3. Survival Rate vs Age_groups grouped by Pclass


### Visuvalizations before feedback:
The html made before feedback can be found in: p6_D3_initial.html

### Feedback from inerviews:


#### 1st Audience. 
What do you notice in the visualization?
> - Rate of survival is given for different age groups
>- Proportion of people survied based on group_age, with respect to different classes is provided.

What questions do you have about the data?
>- For plot 2, the data mentioned on yaxis is not clear,Is it the proportion of people or number of people survived?
>- Even on x-axis ,mention clearly about parch and how data is represented

What relationships do you notice?
> - for 1st plot , rate of survival is high for age group of (0,10)
> - for 2nd Plot ,rate of survival is more for the upper class
> - for 3rd plot, Female survival rate is more in every age group and class.

What do you think is the main takeaway from this visualization?
> Survival rate based upon age,sex and pclass.

Is there something you don’t understand in the graphic?
> 2nd graph is not self explanatory ,provide necessary details about the graphs.

#### 2nd Audience.

> Understandable but ,Did not have proper headings and 2nd plot is not clear.Description about the data set is essential for understanding the plots.1st plot is easily understandable, and the animation was looking good.

####  3rd Audience.

> Explain about the data.
> Is the yaxis number of people survived or its the percentage of people survived?
> What is parch?



### Visuvalizations after Feedback:
Corrections Made:

- Headings ,legends and labels for axes are added.
- plot two is modified ,Because of the using multiple varibles it ended up complex and not interpretable by audence,so i simplyfied it.
- Description for each plot and dataset is added
- I centered all the plots and Description
- Added .css file and filled all cirles with red.


The html made after corrections: p3_D3_final.html


### Resources


- [Data Visualization course](https://www.udacity.com/course/viewer#!/c-ud507-nd)
- [Investigate a dataset exploration from P2](https://github.com/gangadhara691/P2_Investigate_Data)
- [Barplot](http://stackoverflow.com/questions/25478673/add-colors-to-dimple-js-bar-chart-based-on-value-and-add-goal-line)
- [imported barplot library](http://dimplejs.org/examples_viewer.html?id=bars_vertical_grouped_stacked)
- [Kaggle: Predict survival on the Titanic using Excel, Python, R & Random Forests](https://www.kaggle.com/c/titanic)
- [dimple.js Doc](http://dimplejs.org/)

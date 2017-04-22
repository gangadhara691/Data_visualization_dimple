
# coding: utf-8
####################################################################################################
###########       Run this code To Generate Required DataSets     ##################################
####################################################################################################
# # Titanic Data Analysis By Gangadhara Naga Sai
# 
# ## Overview Of Titanic Dataset
#    In 1912, the ship RMS Titanic struck an iceberg on its maiden voyage and sank, resulting in the deaths of most of its    passengers and crew. In this project, we will explore the RMS Titanic passenger manifest to determine whether someone survived or did not survive.Demographics and passenger information from 891 of the 2224 passengers and crew on board the Titanic Dataset is obtained from kaggle (https://www.kaggle.com/c/titanic/data).
# 
# 

# ## Data Wrangling 

# 

import numpy as np
import pandas as pd
from IPython.display import display

get_ipython().magic(u'matplotlib inline')

# Load the dataset
files = 'titanic_data.csv'
data_titanic = pd.read_csv(files)
display(data_titanic.head())


# ### Data Description
# From a sample of the RMS Titanic data, we can see the various features present for each passenger on the ship:
# - **Survived**: Outcome of survival (0 = No; 1 = Yes)
# - **Pclass**: Socio-economic class (1 = Upper class; 2 = Middle class; 3 = Lower class)
# - **Name**: Name of passenger
# - **Sex**: Sex of the passenger
# - **Age**: Age of the passenger (Some entries contain `NaN`)
# - **SibSp**: Number of siblings and spouses of the passenger aboard
# - **Parch**: Number of parents and children of the passenger aboard
# - **Ticket**: Ticket number of the passenger
# - **Fare**: Fare paid by the passenger
# - **Cabin** Cabin number of the passenger (Some entries contain `NaN`)
# - **Embarked**: Port of embarkation of the passenger (C = Cherbourg; Q = Queenstown; S = Southampton)
# 
# Variable Notes
# 
# pclass: A proxy for socio-economic status (SES)
# - 1st = Upper
# - 2nd = Middle
# - 3rd = Lower
# 
# age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
# 
# sibsp: The dataset defines family relations in this way...
# Sibling = brother, sister, stepbrother, stepsister
# Spouse = husband, wife (mistresses and fiancés were ignored)
# 
# parch: The dataset defines family relations in this way...
# Parent = mother, father
# Child = daughter, son, stepdaughter, stepson
# Some children travelled only with a nanny, therefore parch=0 for them.
# 

# In[2]:


data =data_titanic

# Show the dataset 
display(data.head())
data.info()


# From the above info(),We can see columns Age, Cabin and Embarked have missing values.
# 
# Handling the missing values:
#    >Ignore the rows with missing data,
#    
#    >Exclude the variable at all or we might substite it with  mean or median.
#     
#  Age  80% of the data is available,which seems a important variable so not to exclude.
#  
#  Port of embarkation doesn't seem interesting.
#  
#  cabin 23% of the data so decided to exclude.
#  
#  PassengerId,Name,fare doesnt seem to contribute to any survival investigation
# 

# Deleting unwanted columns

#exculding some coloumns
for a in ['Ticket','Cabin','Embarked','Name','PassengerId','Fare']:
    if a in data.columns:
        del data[a]



print "Age median values by Age and Sex:"
#we are grouping by gender and class and taking median of age so we can replace with corrresponding values instead of NaN
print data.groupby(['Sex','Pclass'], as_index=False).median().loc[:, ['Sex','Pclass', 'Age']]
print "Age values for 5 first persons in dataset:"
print data.loc[data['Age'].isnull(),['Age','Sex','Pclass']].head(5)
# apply transformation: Age missing values are filled with regard to Pclass and Sex:
data.loc[:, 'Age'] = data.groupby(['Sex','Pclass']).transform(lambda x: x.fillna(x.median()))
print data.loc[[5,17,19,26,28],['Age','Sex','Pclass']].head(5)
data['Age'] = data['Age'].fillna(data['Age'].mean())


# ## Data Exploration and Visualization

data_s=data



# ### Data set classifing as Men, Women and children 


def group(d,v):
    if (d == 'female') and (v >= 18):
        return 'Woman'
    elif v < 18:
        return 'child'                        
    elif (d == 'male') and (v >= 18): 
        return  'Man'

data['Category'] = data.apply(lambda row:group(row['Sex'], row['Age']), axis=1) 
data.head(5)


# Data set grouped by 'group_age','Sex',"Pclass" 

# We are dividing the Age data into 3 buckets of (0-18),(18-40),(40-90)
# and labeling them as 'Childs','Adults','Seniors' respectively
data['group_age']  = pd.cut(data['Age'], bins=[0,18,40,90], labels=['Childs','Adults','Seniors'])

#finding mean Survival rate grouped by 'group_age','Sex'.
df = data.groupby(['group_age','Sex',"Pclass"]).mean().loc[:,['Survived']]

df.to_csv("titanic_group_age.csv", sep=',', encoding='utf-8')


# dataset grouped by 'Category',"Pclass"
data.to_csv("Category.csv", sep=',', encoding='utf-8')

data_C=data.groupby(['Category',"Pclass"]).mean()
data_C.sort("Survived")["Survived"]
data_C.to_csv("Category.csv", sep=',', encoding='utf-8')


##Data set grouped by Parch
data_C=data.groupby(["Parch"]).mean()
data_C.sort("Survived")["Survived"]
data_C.to_csv("Parch.csv", sep=',', encoding='utf-8')

#Dataset grouped by Age_group and divided into buckets of age with a span of 10 years

data['Age_group']  = pd.cut(data['Age'], bins=range(0,90,10))
data_age=data.groupby(["Age_group"]).mean()

data_age.to_csv("Age_group.csv", sep=',', encoding='utf-8')

#dataset including all the data
data.to_csv("titanic_all.csv", sep=',', encoding='utf-8')



# ## Conclusion
# 
# 
# We observe a order of survival rate based on Age ,Sex and Class:
# 
# |children and women of upper class| 
# |-----------------------------|
# |children and women of middle class| 
# |women of lower class|
# |children of lower class |
# |men of upper class|
# | finally men of the  middle class and lower class have least survival rate|
# 
# The analysis seems that , A female with upper social-economic standing (first class) and Children,had the best chance of survival. Age did not seem to be a major factor.Man in third class, had the lowest chance of survival. Women and children of all classes, were mostly having a higher survival rate than men in general. 


# ## References
# 
# - https://www.kaggle.com/c/titanic/data
# - http://nbviewer.jupyter.org/gist/fonnesbeck/5850463
# - https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.factorplot.html#seaborn.factorplot
# - http://seaborn.pydata.org/index.html

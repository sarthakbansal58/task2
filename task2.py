# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# loading the dataset
df=pd.read_csv("Titanic-Dataset.csv")


# %%
df.head()

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.shape

# %%
df.drop_duplicates(inplace=True)

# %%
df.shape
# it still have 891 rows and 12 columns, so there are no duplicates in the dataset.

# %%
df.info()

# %%
# firstly we will do the univariate analysis of categorical variables, so we will see the distribution of the "Pclass" variable which is the passenger class.
# now we will see the distribution of the target variable "Survived"

plt.subplot(1,2,1)
sns.countplot(x="Survived",data=df)
plt.title("Distribution of Survived")
plt.subplot(1,2,2)
plt.pie(df["Survived"].value_counts(),labels=["Not Survived","Survived"],autopct="%1.1f%%")
plt.title("Percentage of Survived")
plt.show()  




# %%
# distribution of passenger class
plt.subplot(1,2,1)
sns.countplot(x="Pclass",data=df)
plt.title("Distribution of passenger class")
plt.subplot(1,2,2)
plt.pie(df["Pclass"].value_counts(),labels=["class 3","class 2","class 1"],autopct="%1.1f%%")
plt.title("Passenger class analysis")
plt.show()

# %%
# now we see the distribution of sex
plt.subplot(1,2,1)
sns.countplot(x="Sex",data=df)
plt.title("Sex distribution")
plt.subplot(1,2,2)
plt.pie(df["Sex"].value_counts(),labels=["Male","Female"],autopct="%1.1f%%")
plt.title("Sex analysis")
plt.show()


# %%
# Enmbarked variable distribution
plt.subplot(1,2,1)
sns.countplot(x="Embarked",data=df)
plt.title("Embarked distribution")
plt.subplot(1,2,2)
plt.pie(df["Embarked"].value_counts(),labels=["Southampton","Cherbourg","Queenstown"],autopct="%1.1f%%")
plt.title("Embarked analysis")
plt.show()

# %%
# analusis of parch variable which is the number of parents and children aboard the Titanic
df["Parch"].value_counts()
plt.subplot(1,2,1)
sns.countplot(x="Parch",data=df)
plt.title("Parch distribution")
plt.subplot(1,2,2)
plt.pie(df["Parch"].value_counts(),labels=["0","1","2","3","4","5","6"],autopct="%1.1f%%")
plt.title("Parch analysis in percentage")
plt.show()
# means mostly people were travelling alnone

# %%

sns.boxplot(x=df["Age"],data=df)
plt.show()
# from the analysis we can see they are valid values and there are no outliers in the age variable, so we can keep all the values in the dataset.

# %%
print(df["Age"].isnull().sum())

# %%
df["Age"].describe()



# %%
# now we will do the analysis of numerical variables, so we will see the distribution of the "Age" variable which is the age of the passengers
# plt.subplot(1,2,1)
sns.histplot(x="Age",data=df,kde=True,bins=30)
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# %%
# lets do the analusis of Fare variable which is the fare paid by the passengers
sns.histplot(x="Fare",data=df,kde=True,bins=30)
plt.title("fare distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()


# from the anlysis we can see it is highly possitively skewed




# %%
# fare column analyiss
df["Fare"].describe()

# %%
# lets see the distribution of Fare column 

sns.boxplot(x="Fare",data=df)
plt.show()
# from this we can see there are so many passengers who paid very low fare and there are some passengers who paid very high fare, so there are outliers in the fare variable, so we can keep all the values in the dataset because it is a real world data and it is possible that some passengers paid very high fare and some passengers paid very low fare.

# %%
sns.kdeplot(df["Fare"])
plt.show()

# %%
print(df["Fare"].skew())

# %%
# iqr of the data for searching of otliers
q1=df["Fare"].quantile(0.25)
q3=df["Fare"].quantile(0.75)
iqr=q3-q1


max=q3+1.5*(iqr)
print(max) 
# conclusion is that we find our mostly data before 65.6344


# %%
# now we will do the bivariate analysis of categorical variables 

x=pd.crosstab(df["Pclass"],df["Survived"])
sns.heatmap(x)
plt.show()
# from the heatmap we can see that most of the passengers who survived were from class 1 and most of the passengers who did not survive were from class 3.

# %%
# survive ratio among male and female

y=pd.crosstab(df["Sex"],df["Survived"])
sns.heatmap(y)
plt.show()
# we can see that they give priority to female passengers and they give less priority to male passengers

# %%
# now we will do analysis sibsp variable which is the number of siblings and spouses aboard the Titanic
df["SibSp"].value_counts()

sns.countplot(x="SibSp",data=df)
plt.title("SibSp distribution")         
plt.xlabel("Number of Siblings/Spouses")
plt.ylabel("Frequency")
plt.show()

# %%




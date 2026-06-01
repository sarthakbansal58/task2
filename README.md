# Titanic Dataset - Exploratory Data Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset using Python, Pandas, Matplotlib, and Seaborn.

The goal of this analysis is to understand the dataset, identify patterns, visualize distributions, detect outliers, and analyze factors affecting passenger survival.

---

## Dataset Information

The dataset contains information about passengers aboard the Titanic, including:

* Passenger Class (Pclass)
* Survival Status (Survived)
* Sex
* Age
* Fare
* Number of Siblings/Spouses (SibSp)
* Number of Parents/Children (Parch)
* Embarked Port
* Other passenger details

Target Variable:

* Survived

  * 0 = Did Not Survive
  * 1 = Survived

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Analysis Performed

### 1. Data Inspection

* Loaded the dataset
* Checked dataset structure using `info()`
* Examined missing values
* Checked dataset dimensions
* Verified duplicate records

### 2. Univariate Analysis

Categorical Features:

* Survived
* Pclass
* Sex
* Embarked
* Parch
* SibSp

Visualizations Used:

* Count Plots
* Pie Charts

Numerical Features:

* Age
* Fare

Visualizations Used:

* Histograms
* KDE Plots
* Box Plots

### 3. Outlier Analysis

Performed outlier detection on Fare using:

* Box Plot
* Interquartile Range (IQR)

Findings:

* Fare distribution contains several high-value outliers.
* These outliers appear to be valid observations rather than data-entry errors.

### 4. Bivariate Analysis

Analyzed relationships between:

* Pclass vs Survival
* Sex vs Survival

Visualization Used:

* Heatmaps based on Cross-Tabulations

---

## Key Findings

### Survival Distribution

* More passengers did not survive than survived.

### Passenger Class Analysis

* Most passengers traveled in Third Class.
* First-Class passengers had better survival outcomes.

### Gender Analysis

* Male passengers significantly outnumbered female passengers.
* Female passengers had a much higher survival rate.

### Age Analysis

* Most passengers were between 20 and 40 years old.
* Age distribution is approximately right-skewed.

### Fare Analysis

* Fare distribution is highly positively skewed.
* Most passengers paid lower fares.
* A small number of passengers paid exceptionally high fares.

### Family Information

* Most passengers traveled alone or with a small family group.
* Higher values of Parch and SibSp were relatively uncommon.

---

## Learning Outcomes

Through this project, the following concepts were practiced:

* Data Cleaning
* Missing Value Analysis
* Descriptive Statistics
* Univariate Analysis
* Bivariate Analysis
* Outlier Detection
* Data Visualization
* Pattern Recognition
* Feature-Level Inference

---

## Future Improvements

Further analysis can include:

* Correlation Matrix
* Pairplot Analysis
* Survival Rate Analysis
* Feature Engineering
* Machine Learning Model Development

---

## Author

Sarthak Bansal

This project was created as part of learning Data Analysis and Machine Learning fundamentals.

Erista Disti Kirani

Summary

Data Transformation

- Introduction to Data Transformation
- Types of data Transformation
- Challenges in Data Transformation
- Data Transformation Tools
- Excercise on various topics

Introduction to data Transformation

Data transformation refers to the process of converting data from one format or structure into another. its a fundamental step in data integration process.

why is it important

1. Enables data from different to be brought together.
2. Ensure data quality and consistency
3. Facilitates data analysis and business intelligence

Types Data Transformation

1. Normalization: scaling data to a standard range
2. Encoding: Converting categorical data to numerical format.
3. Aggregation: summarizing data for analysis.

Normalization Scalling data to standard range

- purpose: Ensures that each feature contributes equally to the computation in machine learning algorithms.
- common methods: min-max scalling. Z-core normalization
- use cases: neural networks, algorithms that rely on future magnitude.

Encoding Converting categorical data to numerical format

- purpose: machine learning algorithms require numerical input, so categorical data must be converted.
- Common Methods:

one-hot encoding assigning binary columns for each category

label encoding: Assigning a unique integer to each category. (note:this method can introduce ordinal relationships that might not exist.)

Uses cases: Regression analysis classification tasks.

Aggregation

Summarizing data for analysis

purpose: provides a summarized view of data, often to change its granularity.

common methods:

sum

average

count: total number of data points

max: highest value in the dataset

min: lowest value in the dataset

use cases: time series data, group-based analysis:

Challenges in Data Transformation

1. handling missing values
2. dealing with outliers.
3. ensuring data integrity and avoiding data loss.

handling missing values.

purpose:

missing values can arise due to various reasons, such as data entry errors, data information.

handling them is crucial as they can skew analytical results or lead to errors in machine learning models.

common methods:

deletion: removing rows with missing values.

imputation: filling in missing values based on other data points

forward/backward fill: using the previous or next data point to fill the missing value.

dealing with outliers:

purpose:

outliers are data points that differ significantly from other observations.

they can arise due to variability in the data or errors.

common methods:

z-score: identifying values that are a certain number of standard deviations away from the mean.

IQR(interquartile range): values outside 1.5 times the IQR above the third quartile or below the first quartile are considered outliers.

Data Transformation Tools

ETL tools help in collecting data from various sources, modifying it as need, and then storing it in central place.

data wrangling with pandas in python:

Data wrangling is the process of cleaning organizing messy data to make it suitable for analysis.

Data wrangling with pandas in python - discovering

this is initial exploration of dataset. you’ll get a feel for its content, asses the size and identify the type of data.

Data wrangling with pandas in python - structuring

organize the data in way that makes it suitable for analysis. this might involve reshaping the dataset or modifying is layout.

Data wrangling with pandas in python - cleaning

addres data quality issues, such as missing values, duplicates, or incorrect data.

Data wrangling with pandas in python - enriching

Enhance the dataset by adding new columns or integrating with other data sources.

Exercise on various topics

Setting up Apache Airflow

Extract Data

Transform Data

Load Data

Apache Airflow DAG
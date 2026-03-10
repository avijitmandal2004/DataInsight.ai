# DataInsight.ai Automated Report

# Dataset Overview – Superstore Sales
## Dataset Source - Kaggle (https://www.kaggle.com/datasets/fatihilhan/global-superstore-dataset?resource=download)
## Number of Rows - 51,290 rows
## Number of Columns - 27 columns
## Column Names -
1.  Category
2.  City
3.  Country
4.  Customer.ID
5.  Customer.Name
6.  Discount
7.  Market
8.  记录数
9.  Order.Date
10. Order.ID
11. Order.Priority
12. Product.ID
13. Product.Name
14. Profit
15. Quantity
16. Region
17. Row.ID
18. Sales
19. Segment
20. Ship.Date
21. Ship.Mode
22. Shipping.Cost
23. State
24. Sub.Category
25. Year
26. Market2
27. weeknum

## Data Types-
### Numeric Columns
- Discount
- Profit
- Quantity
- Sales
- Shipping.Cost
- Row.ID
- Year
- weeknum
- 记录数
### Date Columns
- Order.Date
- Ship.Date
### Categorical Columns
- Category
- City
- Country
- Customer.ID
- Customer.Name
- Market
- Order.ID
- Order.Priority
- Product.ID
- Product.Name
- Region
- Segment
- Ship.Mode
- State
- Sub.Category
- Market2

## Total missing values: 0

## Data Quality Issues
- Column name `记录数` contains non-English characters.
- Date columns are stored as string format and may require parsing.
- Customer.Name contains special characters.


## Possible Use Case -
This dataset can be used for:
1.Sales performance analysis
2.Regional profit comparison
3.Customer segmentation analysis
4.Time-based sales trend forecasting

# Data Cleaning Summary – Day 4

## Dataset Loaded From
data/raw/small_business_sales.csv

## Original Dataset Shape
(34, 8)

## Missing Value Strategy
1. Checked missing values column-wise
2. No missing values found
3. No rows were dropped

## Data Type Handling
1. Numeric columns ensured as int/float
2. No incorrect types found

## Columns Modified
1. No columns renamed
2. No columns dropped

## NumPy Operations Performed
1. Mean calculated on numeric column
2. Median calculated
3. Standard deviation calculated

## Feature Selection
 Input Features (X): All columns except target
 Target Column (y): sales

## Final Cleaned Dataset Shape
(34, 8)

## Assumptions
1. Dataset is small but structurally clean
2. No missing or corrupt values detected

# Baseline Model Results

## Model Type
Simple Neural Network   [##TensorFlow Sequential Model]

## Features Used
quantity
unit_price

## Target Variable
sales

## Training Parameters
Epochs: 50
Optimizer: Adam
Loss Function: Mean Squared Error
Metric: Mean Absolute Error

## Final Evaluation Result
Final Test MAE: 2537.93

## Observations
1. Loss gradually decreased during training
2. Model performance is basic (baseline)
3. Dataset is very small (34 rows)
4. More data and feature engineering may improve performance



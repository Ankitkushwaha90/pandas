
Here is a comprehensive collection of Pandas code examples, covering basic DataFrame manipulations, data I/O, cleaning, and more. This will serve as a great tutorial.

### 1. Creating DataFrames
```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 22, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)

# Create a DataFrame from a list of lists
data = [['John', 28, 'New York'], ['Anna', 22, 'Paris'], ['Peter', 35, 'Berlin']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print("DataFrame from list of lists:\n", df)
```
### 2. Reading and Writing Data
```python
import pandas as pd

# Reading a CSV file
df = pd.read_csv('data.csv')
print("Data from CSV:\n", df)

# Writing DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# Reading an Excel file
df_excel = pd.read_excel('data.xlsx')
print("Data from Excel:\n", df_excel)

# Writing to Excel
df.to_excel('output.xlsx', index=False)
```
### 3. Basic DataFrame Operations
```python
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Display the first few rows
print("First rows:\n", df.head())

# Get DataFrame info
print("DataFrame Info:\n", df.info())

# Describe the DataFrame (statistics summary)
print("DataFrame Description:\n", df.describe())

# Access a column
print("Column A:\n", df['A'])

# Access multiple columns
print("Columns A and B:\n", df[['A', 'B']])

# Access a specific row by index
print("Second row:\n", df.iloc[1])

# Access a specific element by row and column index
print("Element at (0, 1):", df.iat[0, 1])
```
### 4. Data Selection and Filtering
```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 22, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Select rows where Age > 30
filtered_df = df[df['Age'] > 30]
print("Filtered rows:\n", filtered_df)

# Select rows based on multiple conditions
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'New York')]
print("Filtered with multiple conditions:\n", filtered_df)

# Select rows by index
selected_rows = df.loc[[0, 2]]
print("Selected rows by index:\n", selected_rows)
```
### 5. Data Cleaning
```python
import pandas as pd

# Create a DataFrame with missing data
data = {'Name': ['John', 'Anna', 'Peter', None],
        'Age': [28, None, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Drop rows with missing values
df_dropped = df.dropna()
print("DataFrame with dropped rows:\n", df_dropped)

# Fill missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age': 0})
print("DataFrame with filled values:\n", df_filled)

# Replace specific values
df_replaced = df.replace({'New York': 'NYC'})
print("DataFrame with replaced values:\n", df_replaced)
```
### 6. Handling Duplicates
```python
import pandas as pd

# Create a DataFrame with duplicates
data = {'Name': ['John', 'Anna', 'John', 'Linda'],
        'Age': [28, 22, 28, 32]}
df = pd.DataFrame(data)

# Check for duplicates
duplicates = df.duplicated()
print("Duplicate rows:\n", duplicates)

# Drop duplicate rows
df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates:\n", df_no_duplicates)
```
7. Grouping and Aggregating Data
```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'John', 'Linda'],
        'Age': [28, 22, 28, 32],
        'City': ['New York', 'Paris', 'New York', 'London']}
df = pd.DataFrame(data)

# Group by column and apply aggregation
grouped_df = df.groupby('City').agg({'Age': ['mean', 'max']})
print("Grouped and aggregated DataFrame:\n", grouped_df)

# Group by multiple columns
grouped_df = df.groupby(['City', 'Name']).size().reset_index(name='Count')
print("Grouped by multiple columns:\n", grouped_df)
```
### 8. Merging and Joining DataFrames
```python
import pandas as pd

# Create two DataFrames to merge
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Anna', 'Peter']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Age': [28, 22, 35]})

# Merge DataFrames on a common column
merged_df = pd.merge(df1, df2, on='ID')
print("Merged DataFrame:\n", merged_df)

# Left join (keep all rows from left DataFrame)
left_joined_df = pd.merge(df1, df2, on='ID', how='left')
print("Left joined DataFrame:\n", left_joined_df)

# Right join (keep all rows from right DataFrame)
right_joined_df = pd.merge(df1, df2, on='ID', how='right')
print("Right joined DataFrame:\n", right_joined_df)
```
### 9. Pivoting and Reshaping Data
```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'John', 'Anna'],
        'Year': [2020, 2020, 2021, 2021],
        'Sales': [100, 200, 150, 250]}
df = pd.DataFrame(data)

# Pivot the DataFrame
pivot_df = df.pivot(index='Name', columns='Year', values='Sales')
print("Pivoted DataFrame:\n", pivot_df)

# Melt the DataFrame (unpivot)
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Sales'])
print("Melted DataFrame:\n", melted_df)
```
### 10. Handling Dates and Times
```python
import pandas as pd

# Create a DataFrame with date strings
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [10, 20, 30]}
df = pd.DataFrame(data)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])
print("DataFrame with datetime:\n", df)

# Extract year, month, day from datetime
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print("DataFrame with year, month, day:\n", df)

# Create a date range
date_range = pd.date_range(start='2022-01-01', end='2022-01-10')
print("Date range:\n", date_range)
```
### 11. Plotting with Pandas
```python
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {'Date': pd.date_range(start='2022-01-01', periods=5),
        'Sales': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# Plot the data
df.plot(x='Date', y='Sales', kind='line', marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
```
### 12. Advanced Indexing with MultiIndex
```python
import pandas as pd

# Create a DataFrame with MultiIndex
arrays = [['USA', 'USA', 'Germany', 'Germany'], ['New York', 'Chicago', 'Berlin', 'Munich']]
index = pd.MultiIndex.from_arrays(arrays, names=('Country', 'City'))
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])
print("DataFrame with MultiIndex:\n", df)

# Access data using MultiIndex
print("Sales in Berlin:", df.loc[('Germany', 'Berlin')])

# Access data for a specific country
print("Sales in Germany:\n", df.loc['Germany'])
```
This set of examples covers a wide range of Pandas functionality, from basic DataFrame operations to advanced tasks like merging, pivoting, and date handling.

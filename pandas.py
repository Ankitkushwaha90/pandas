import pandas as pd

# Load data from CSV file
csv_file = 'data.csv'
df = pd.read_csv(csv_file)

# Display the first few rows of the dataframe
print("First few rows of the dataframe:")
print(df.head())

# Summary statistics of numerical columns
print("\nSummary statistics:")
print(df.describe())

# Count the occurrences of each value in the 'Age' column
print("\nAge distribution:")
print(df['Age'].value_counts())

# Average salary
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: {average_salary}")

# Filter data for individuals with age greater than 25
print("\nIndividuals with age greater than 25:")
print(df[df['Age'] > 25])

# Group data by age and calculate the average salary for each age group
age_group_salary = df.groupby('Age')['Salary'].mean()
print("\nAverage Salary by Age:")
print(age_group_salary)

# Save the modified dataframe to a new CSV file
df.to_csv('modified_data.csv', index=False)
print("\nModified data saved to 'modified_data.csv'")

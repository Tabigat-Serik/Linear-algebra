import pandas as pd

# Load the dataset into a Pandas DataFrame
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid_data = pd.read_csv(url)

# Display the first few rows of the dataset
print("Original Dataset:")
print(covid_data.head())

# Clean the data: handle missing values, filter relevant columns
relevant_columns = ['date', 'location', 'new_cases', 'total_cases']
cleaned_data = covid_data[relevant_columns].dropna()

# Convert the 'date' column to datetime format
cleaned_data['date'] = pd.to_datetime(cleaned_data['date'])

# Display the cleaned data
print("\nCleaned Data:")
print(cleaned_data.head())

# Create a new DataFrame that aggregates data on a monthly basis
monthly_aggregated_data = cleaned_data.groupby(['location', pd.Grouper(key='date', freq='M')]).agg({
    'new_cases': 'sum',
    'total_cases': 'max'
}).reset_index()

# Display the aggregated data
print("\nMonthly Aggregated Data:")
print(monthly_aggregated_data.head())

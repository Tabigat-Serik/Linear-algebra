import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a Pandas DataFrame
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid_data = pd.read_csv(url)

# Clean the data: handle missing values, filter relevant columns
relevant_columns = ['date', 'location', 'new_cases', 'total_cases']
cleaned_data = covid_data[relevant_columns].dropna()

# Convert the 'date' column to datetime format
cleaned_data['date'] = pd.to_datetime(cleaned_data['date'])

# Plot the trend of new cases over time for selected countries
selected_countries = ['United States', 'India', 'Brazil', 'United Kingdom', 'Germany']
plt.figure(figsize=(12, 6))
for country in selected_countries:
    country_data = cleaned_data[cleaned_data['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title('Trend of New Cases Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.show()

# Create a bar chart showing the total cumulative cases for the top 10 affected countries
top_countries = cleaned_data.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries by Total Cumulative Cases')
plt.xlabel('Country')
plt.ylabel('Total Cumulative Cases')
plt.xticks(rotation=45)
plt.show()

# Generate a heatmap to show the correlation between different numerical columns
correlation_columns = ['new_cases', 'total_cases', 'new_deaths', 'total_deaths']
correlation_matrix = cleaned_data[correlation_columns].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

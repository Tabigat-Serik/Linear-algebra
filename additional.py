import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load COVID-19 dataset
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid_data = pd.read_csv(url)

# Clean the data
relevant_columns = ['date', 'location', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths']
cleaned_data = covid_data[relevant_columns].dropna()
cleaned_data['date'] = pd.to_datetime(cleaned_data['date'])

# Select countries for comparative analysis
selected_countries = ['USA', 'India', 'Brazil', 'United Kingdom', 'Germany']

# Create a comparative analysis using Matplotlib
plt.figure(figsize=(14, 8))

# Comparative analysis of new cases
plt.subplot(2, 2, 1)
for country in selected_countries:
    country_data = cleaned_data[cleaned_data['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title('Comparative Analysis of New Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()

# Comparative analysis of new deaths
plt.subplot(2, 2, 2)
for country in selected_countries:
    country_data = cleaned_data[cleaned_data['location'] == country]
    plt.plot(country_data['date'], country_data['new_deaths'], label=country)

plt.title('Comparative Analysis of New Deaths')
plt.xlabel('Date')
plt.ylabel('New Deaths')
plt.legend()

# Comparative analysis of total cases
plt.subplot(2, 2, 3)
for country in selected_countries:
    country_data = cleaned_data[cleaned_data['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Comparative Analysis of Total Cases')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()

# Comparative analysis of total deaths
plt.subplot(2, 2, 4)
for country in selected_countries:
    country_data = cleaned_data[cleaned_data['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)

plt.title('Comparative Analysis of Total Deaths')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()

plt.tight_layout()
plt.show()

# Create an interactive comparative analysis using Plotly
fig = px.line(cleaned_data[cleaned_data['location'].isin(selected_countries)],
              x='date', y='new_cases', color='location', facet_col='location',
              labels={'new_cases': 'New Cases', 'date': 'Date'},
              title='Interactive Comparative Analysis of New Cases')
fig.update_layout(xaxis_title='Date', yaxis_title='New Cases')
fig.show()



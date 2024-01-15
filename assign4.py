import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create two hypothetical datasets (matrices)
data_source_1 = pd.DataFrame({
    'Country': ['USA', 'India', 'Brazil'],
    'Population': [331002651, 1380004385, 212559417],
    'GDP': [21433225, 2875145, 1839755]
})

data_source_2 = pd.DataFrame({
    'Country': ['USA', 'India', 'Brazil'],
    'Cases': [28827035, 30458144, 13373174],
    'Deaths': [531056, 401050, 353137]
})

# Merge datasets using matrix multiplication (inner join on 'Country' column)
merged_data = pd.merge(data_source_1, data_source_2, on='Country')

# Display the merged data
print("Merged Data:")
print(merged_data)

# Perform matrix transpose for a different analytical view
transposed_data = merged_data.T

# Display the transposed data
print("\nTransposed Data:")
print(transposed_data)

# Visualize the outcomes
plt.figure(figsize=(12, 5))

# Bar chart for combined data
plt.subplot(1, 2, 1)
sns.barplot(x='Country', y='GDP', data=merged_data, color='skyblue')
plt.title('GDP by Country')

# Heatmap for transposed data
plt.subplot(1, 2, 2)
sns.heatmap(transposed_data, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Transposed Data Heatmap')

plt.tight_layout()
plt.show()

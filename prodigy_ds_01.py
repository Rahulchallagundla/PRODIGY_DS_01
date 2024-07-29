# -*- coding: utf-8 -*-
"""PRODIGY_DS_01

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ptBvLrb4e_tH5KWXCV_9LDFRdrLQ50VX
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data files
population_data = pd.read_csv('/content/API_SP.POP.TOTL_DS2_en_csv_v2_2001050.csv', skiprows=4)
country_metadata = pd.read_csv('/content/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_2001050.csv')
indicator_metadata = pd.read_csv('/content/Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_2001050.csv')

# Filter the data for the year 2020
population_2020 = population_data[['Country Name', '2020']]

# Drop rows with missing values
population_2020 = population_2020.dropna()

# Rename columns for clarity
population_2020.columns = ['Country', 'Population_2020']

# Plot the histogram
plt.figure(figsize=(12, 8))
plt.hist(population_2020['Population_2020'], bins=30, edgecolor='black')
plt.title('Distribution of Total Population by Country in 2020')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.grid(True)
plt.show()
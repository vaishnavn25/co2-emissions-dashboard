# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:31:10 2025

@author: Ghost
"""
import pandas as pd

# Load dataset
df = pd.read_csv("D:\Projects\Datasets\CO2 Emission\cleaned_co2_data_new.csv")


# Drop columns with too many missing values (threshold: 60%)
#df_cleaned = df.dropna(thresh=0.4*len(df), axis=1)

# Fill missing values in numeric columns with 0
#df_cleaned.fillna(0, inplace=True)

# Filter dataset to keep only records from 1900 onwards
#df_filtered = df_cleaned[df["year"] >= 1900]
df_cleaned = df[df["iso_code"] != "0"]

# Save the cleaned data
df_cleaned.to_csv("D:\Projects\Datasets\CO2 Emission\cleaned_co2_data22.csv", index=False)

print("Data cleaned and saved!")

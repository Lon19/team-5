import pandas as pd

df = pd.read_csv('claimant-count-all-wards.csv')

ward_data = {}

for idx, ward in enumerate(df['2011 census frozen ward']):
    ward_data[ward] = {'Total': df['Total'][idx],
                       'Male': df['Male'][idx],
                       'Female': df['Female'][idx],
                       }

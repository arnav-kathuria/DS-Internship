import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\hp\Desktop\EDA.csv")

# Q1

# a
data['Year'] = pd.DatetimeIndex(data['Open Date']).year
sales_by_year = data.groupby('Year')['Sales'].sum()

# b
opened_1991 = data[data['Year'] == 1991].shape[0]

# c
remodeled = data[data['Store Type'].str.contains('Remodel')].shape[0]

# d
correlation = data['Sales'].corr(data['Total Sq. Ft.'])

# e
profitable_sd = data.groupby('Super Division')['Sales'].sum().idxmax()

# f
active_stores = data[data['Status'].str.lower() == 'active'].shape[0]

# g
avg_sqft = data.groupby('Super Division')['Total Sq. Ft.'].mean().idxmax()

# Q2

# a
state_avg_sales = data.groupby('State')['Sales'].mean().sort_values(ascending=False).head(3)

# b
data['Month'] = pd.DatetimeIndex(data['Open Date']).month
best_month = data.groupby('Month')['Sales'].mean().idxmax()

# c
closed = data[data['Status'].str.lower() == 'closed']
outlet_type_closed = closed['Outlet Type'].value_counts()

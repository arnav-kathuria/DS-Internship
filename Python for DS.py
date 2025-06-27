import pandas as pd
import numpy as np

sales_df = pd.read_csv(r"C:\Users\hp\Desktop\SalesData.csv")
diamonds_df = pd.read_csv(r"C:\Users\hp\Desktop\diamonds.csv")
imdb_df = pd.read_csv(r"C:\Users\hp\Desktop\imdb.csv")

# Q1

q1 = sales_df.groupby("Item")["Sale_amt"].min()
q1 = q1.reset_index() # used reset_index because of group by

# Q2

sales_df["OrderDate"] = pd.to_datetime(sales_df["OrderDate"])
sales_df["Year"] = sales_df["OrderDate"].dt.year

q2 = sales_df.groupby(["Year", "Region"])["Sale_amt"].sum()
q2 = q2.reset_index()

# Q3

reference_date = pd.to_datetime("2022-01-01")
sales_df["days_diff"] = reference_date - sales_df["OrderDate"]
sales_df["days_diff"] = sales_df["days_diff"].dt.days

# Q4

grouped = sales_df.groupby("Manager")["SalesMan"].unique()
q4 = grouped.reset_index()
q4 = q4.rename(columns={"SalesMan": "list_of_salesmen"})

# Q5

salesmen_count = sales_df.groupby("Region")["SalesMan"].nunique()
total_sales = sales_df.groupby("Region")["Sale_amt"].sum()

q5 = pd.DataFrame()
q5["Region"] = salesmen_count.index
q5["salesmen_count"] = salesmen_count.values
q5["total_sales"] = total_sales.values

# Q6

total_sales_all = sales_df["Sale_amt"].sum()
sales_by_manager = sales_df.groupby("Manager")["Sale_amt"].sum()

percent_sales = (sales_by_manager / total_sales_all) * 100
q6 = percent_sales.reset_index()
q6 = q6.rename(columns={"Sale_amt": "percent_sales"})

# Q7

q7 = imdb_df.iloc[4]["imdb_rating"]

# Q8

shortest_duration_index = imdb_df["duration"].idxmin()
longest_duration_index = imdb_df["duration"].idxmax()

shortest_title = imdb_df.loc[shortest_duration_index, "title"]
longest_title = imdb_df.loc[longest_duration_index, "title"]

q8 = (shortest_title, longest_title)

# Q9

imdb_df["release_date"] = pd.to_datetime(imdb_df["release_date"], errors="coerce")

q9 = imdb_df.sort_values(
    by=["release_date", "imdb_rating"],
    ascending=[True, False]
)

# Q10

q10 = imdb_df[
    (imdb_df["duration"] >= 1800) &
    (imdb_df["duration"] <= 10800)
]

# Q11

duplicates = diamonds_df.duplicated()
q11 = duplicates.sum()

# Q12

q12 = diamonds_df.dropna(subset=["carat", "cut"])

# Q13

q13 = diamonds_df.select_dtypes(include=[np.number])

# Q14

depth_condition = diamonds_df["depth"] > 60
volume_value = diamonds_df["x"] * diamonds_df["y"] * diamonds_df["z"]

diamonds_df["volume"] = np.where(depth_condition, volume_value, 8)

# Q15

price_mean = diamonds_df["price"].mean()
diamonds_df["price"] = diamonds_df["price"].fillna(price_mean)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score

df = pd.read_excel(r"C:\Users\hp\Desktop\DS Internship - Modeling - Data.xlsx")

df_clean = df.dropna()
 # remove useless features
df_clean = df_clean.drop(columns=['ChangeDate', 'Store ID'])

# categorical columns to one-hot vectors
df_encoded = pd.get_dummies(df_clean, drop_first=True)

# remove sales from features
X = df_encoded.drop(columns=['Sales']) 
y = df_encoded['Sales']

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model training
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

# key driver for sales
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': lr.coef_
}).sort_values(by='Coefficient', key=abs, ascending=False).head(10)

# evaluate model performance
mape = mean_absolute_percentage_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

# most important features
print("Most significant features\n", coefficients)

# removing highly similar features
corr_matrix = df_clean.corr(numeric_only=True).abs()
mask = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
upper_triangle = corr_matrix.where(mask)
to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > 0.9)]
df_clean = df_clean.drop(columns=to_drop)

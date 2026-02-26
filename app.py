import pandas as pd 
import numpy as np 

#data loads
df = pd.read_csv('psx_data.csv')
print(df.head(5))

#cleaning the Price column and convert values type to float
df["Price"] = df["Price"].astype(str).str.replace(",", "", regex=False).astype(float)

#Ignoring the missing and invalid values
df["Price"] = pd.to_numeric(df["Price"].astype(str).str.replace(",", "", regex=False), errors='coerce')
df = df.dropna(subset=["Price"])


#Using Numpy to find Mean & Std Deviation
mean_price = np.mean(df["Price"])
std_price = np.std(df["Price"])

print(f"Mean: {mean_price: .2f}")
print(f"Std: {std_price: .2f}")


#Using Pandas to find same results
mean_price = df["Price"].mean()
std_price = df["Price"].std()

print(f"Mean: {mean_price: .2f}")
print(f"Std: {std_price: .2f}")


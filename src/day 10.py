import pandas as pd
data = {"CustomerID": [101,102,103,104,105,106],
        "Name": ["Amit","Talha",None,"Amaan","Priya","Ali"],
        "Age": [25,None,30,35,48,90],
        "City": ["Banglore","Mumbai","Kolkata","Meena","Delhi",None],
        "PaymentMethod": ["UPI","Card","Cash","UPI",None,"Card"]}
df = pd.DataFrame(data)

#inspect dataset 

print("First row :\n", df.head())
print("\nDataset info:")
print(df.info())

#missing value

print("\nMissing values per column:")
print(df.isna().sum())

# fill missing values (statistical approch)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])

# check data types before correction 

print("\nData types BEFORE conversion:")
print(df.dtypes)

# convert datatypes

df["Age"] = df["Age"].astype(int)

print("\nData types AFTER conversion:")
print(df.dtypes)


# DUBLICATE HANDLING

# CHECK DUBLICATE ROWS

print("\nNumber of dublicate rows:")
print(df.dublicated().sum())

#  REMOVE DUBLICATES

df = df.drop_dublicates()

# TASK 1

import pandas as pd

df = pd.read_csv("customer_orders.csv")
print("Shape before cleaning:", df.shape)

print("\nMissing values in each column:")
print(df.isna().sum())

df["order_id"].fillna(df["order_id"].median(), inplace=True)
df["amount"].fillna(df["amount"].median(), inplace=True)
df["quantity"].fillna(df["quantity"].median(), inplace=True)

df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)

# TASK 2

import pandas as pd

df = pd.read_csv("customer_orders_clean.csv")

print("Data types before cleaning:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False)

df["Price"] = df["Price"].astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData types after cleaning:")
print(df.dtypes)

#TASK 3

import pandas as pd

df = pd.read_csv("customer_orders_location.csv")

print("Before Cleaning:")
print(df["Location"].unique())
df["Location"] = df["Location"].str.strip()

df["Location"] = df["Location"].str.title()

print("\nAfter Cleaning:")
print(df["Location"].unique())





































































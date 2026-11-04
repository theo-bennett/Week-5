# Optional task: analyse the dataset with pandas.
# Install first with:  pip install pandas

import pandas as pd

df = pd.read_csv("PartC/student.csv")

print("Total records:", len(df))
print("\nColumn headings:", list(df.columns))
print("\nFirst 5 records:")
print(df.head())

print("\nStudents per course:")
print(df["course"].value_counts())

print("\nAverage score:", round(df["score"].mean(), 2))
print("\nAverage score by course:")
print(df.groupby("course")["score"].mean().round(2))
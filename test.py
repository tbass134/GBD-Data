import pandas as pd

df = pd.read_csv("GBD-DATA-INPUT-SOURCES-1.csv", usecols=["Location", "Risk", "Sex", "Age Start", "Age End"])
df["Age"] = round(df["Age End"] - df["Age Start"] / 365)
df = df.drop(["Age Start", "Age End"], axis=1)
df = df[df["Location"] != "United States of America" ]
df.to_csv("GBD-DATA-INPUT-SOURCES-test.csv", index=False)
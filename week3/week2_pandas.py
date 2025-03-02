import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=7)
print(dates)

df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
})

print(df2)
print(df2.dtypes)

index = pd.date_range("1/1/2013", periods=6)
df = pd.DataFrame(np.random.randn(6, 3), index=index, columns=["A", "B", "C"])
print(df.head())
print(df.tail(3))

print(df.index)

print(df.columns)

print(df.to_numpy())

print(df2.to_numpy())

print(df.describe())

print(df.T)

print(df.sort_index())

print(df.sort_values(by="B"))

print(df["A"])

print(df[0:3])

print(df["20130102":"20130104"])

print(df.loc[dates[0]])

print(df.loc[:, ["A", "B"]])

print(df.loc["20130102":"20130104", ["A", "B"]])

print(df.loc["20130102", ["A", "B"]])

print(df.loc[dates[0], "A"])

print(df.at[dates[0], "A"])

print(df.iloc[3])

print(df.iloc[3:5, 0:2])

print(df.iloc[[1, 2, 4], [0, 2]])

print(df.iloc[1:3, :])

print(df.iloc[:, 1:3])

print(df.iat[1, 1])

print(df[df["A"] > 0])

print(df[df > 0])

df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)

# df2[df2["E"].isin(["two", "four"])]

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1)

df["F"] = s1
print(df)

df.at[dates[0], "A"] = 0

df.iat[0, 1] = 0

df.loc[:, "D"] = np.array([5] * len(df))

print(df)

df2 = df.copy()

df2[df2 > 0] = -df2

print(df2)

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

print(s.str.lower())

rng = pd.date_range("1/1/2012", periods=100, freq="s")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts.resample("5Min").sum()

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

ts = pd.Series(np.random.randn(len(rng)), rng)

print(ts)

ts_utc = ts.tz_localize("UTC")
print(ts_utc)

ts_utc.tz_convert("US/Eastern")
print(ts)
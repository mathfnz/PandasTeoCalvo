# %%
import pandas as pd

ages: list[int] = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

names: list[str] = [
    "Teo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Tito"
]

series_age = pd.Series(ages)
print(series_age)
# %%
# sorting the age Series
series_age = series_age.sort_values()
print(series_age)
# %%
# the index its integrate to the value, so I can't use the index
# iloc -> i location
series_age.iloc[0]

# %%
series_age.iloc[-1]

# %%
series_age.iloc[:3]

# %%
series_age = pd.Series(ages, index=names)
print(series_age)

# %%
series_age["Pedro"]
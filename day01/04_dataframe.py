#%%
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

series_ages = pd.Series(ages)
series_names = pd.Series(names)

# %%
df = pd.DataFrame()
df["Ages"] = series_ages
df["Names"] = series_names
print(df)

# %%
df["Names"]

# %% traz a linha toda com todas as informacoes
df.iloc[2]
df.iloc[2]["Names"]

# %% idade da ultima pessoa
df.iloc[-1]["Ages"]
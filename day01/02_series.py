# %%
import pandas as pd

idades: list[int] = [
                    32, 38, 30, 31, 35, 25,
                    29, 31, 37, 27, 23, 36, 33, 32
                ]

series_age = pd.Series(idades)

# %%
age_average = series_age.mean()
age_variable = series_age.var()
summary_age = series_age.describe()

# %%
print(age_variable)
print(summary_age)

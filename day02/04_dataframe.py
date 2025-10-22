# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
print(df_clientes)

# %%
df_clientes.head(10)

# %%
df_clientes.tail()
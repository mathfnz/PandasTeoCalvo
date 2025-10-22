# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
print(df_clientes)

# %% 10 primeiros
df_clientes.head(10)

# %% 5 ultimos
df_clientes.tail()

# %% (linha, coluna)
df_clientes.shape

# %% nome das colunas
df_clientes.columns

# %% quantidade de index
df_clientes.index

# %%
df_clientes.info()

# %% traz os tipos de valores de cada serie, e essas series se tornam o indice
df_clientes.dtypes

# %% fTwitch
df_clientes.dtypes["flTwitch"]

# %% renomear colunas

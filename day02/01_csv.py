# %%
import pandas as pd

PATH = "../data/clientes.csv"
# lendo o arquivo
df_clientes = pd.read_csv(PATH, sep=";")
print(df_clientes)

# %%
# jogando o arquivo para -> day02 - tirando o index
df_clientes.to_csv("clientes_alterados.csv", index=False)

# %%
# lendo o arquivo
df_clientes = pd.read_csv("clientes_alterados.csv")
print(df_clientes)

# %%
df_clientes.to_excel("clientes_excel.xlsx", index=False)
df_clientes = pd.read_excel("clientes_excel.xlsx")
print(df_clientes)

# %%

# %%
import pandas as pd

df_transacoes = pd.read_csv("../data/transacoes.csv")
print(df_transacoes)

# %% qtd de linhas
df_transacoes.shape
renamed_columns = {
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}
# %%
df_transacoes.rename(columns=renamed_columns, inplace=True)

# %%
print(df_transacoes)

# %% lendo uma coluna
df_transacoes[["IdCliente"]]

# %% lendo mais de uma
df_transacoes[["IdCliente", "qtPontos"]]

# %%
# SELECT idCliente, qtPontos FROM df LIMIT 5

df_transacoes[["IdCliente", "qtPontos"]].sample(5)

# %% reordenar colunas
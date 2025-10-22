# %%
import pandas as pd

URL = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

url_wikipedia = pd.read_html(URL)
print(url_wikipedia)

# %%
len(url_wikipedia)
import pandas as pd
from tools.utils import gen_bar_domains

df = pd.read_csv('data/domains.csv')

fig = gen_bar_domains(df)

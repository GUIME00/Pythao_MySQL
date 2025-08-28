import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# 4. Agrupe os pedidos por forma de pagamento e calcule o valor médio de frete.
df_pedidos = pd.read_sql("SELECT * FROM pedidos", con=engine)
media_frete = df_pedidos.groupby("forma_pagamento")["valor_frete"].mean()
print(media_frete)
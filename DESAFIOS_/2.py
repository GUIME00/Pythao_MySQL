import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# 2. Calcule o valor total do estoque (preço_venda * estoque_atual)
df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
df_produtos["valor_total_estoque"] = df_produtos["preco_venda"] * df_produtos["estoque_atual"]
print(df_produtos[["produto_id", "valor_total_estoque"]])
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# 5. Liste os 5 produtos com menor margem de lucro (preco_venda - preco_custo)
df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
df_produtos["margem_lucro"] = df_produtos["preco_venda"] - df_produtos["preco_custo"]
produtos_menor_margem = df_produtos.nsmallest(5, "margem_lucro")
print(produtos_menor_margem[["produto_id", "margem_lucro"]])
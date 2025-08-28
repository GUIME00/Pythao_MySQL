import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# 3. Filtre os fornecedores da cidade de "Maringá" e status "Ativo".
df_fornecedores = pd.read_sql("SELECT * FROM fornecedores", con=engine)
fornecedores_filtrados = df_fornecedores[(df_fornecedores["cidade"] == "Maringá") & (df_fornecedores["status_fornecedor"] == "Ativo")]
print(fornecedores_filtrados)
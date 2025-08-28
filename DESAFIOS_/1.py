import pandas as pd
from sqlalchemy import create_engine
 
#1 Liste os produtos com status "Descontinuado".
engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")
 
df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
 
ativos = df_produtos[df_produtos["status_produto"] == "Descontinuado"]
print(ativos)
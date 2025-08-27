import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# mysql+pymysql://: define que estamos usando o driver pymysql para conectar ao MySQL
# root: usuário do MySQL
# 123456: senha do MySQL
# localhost: endereço do servidor MySQL
# sistema_vendas: nome do banco de dados

# df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
# print(df_produtos.head())
# print(df_produtos.shape)
# print(df_produtos.info())
# print(df_produtos.describe())
# print(df_produtos.columns)

# print(df_produtos.isnull().sum())

# df_produtos['dimensoes'] = df_produtos['dimensoes'].fillna(0)

# print(df_produtos.isnull().sum())

# print(df_produtos.info())

# ativos = df_produtos[df_produtos['status_produto'] == 'Ativo']

# abaixo_min = ativos[ativos['estoque_atual'] < ativos['estoque_minimo']]

# print(abaixo_min[['nome_produto', 'estoque_atual', 'estoque_minimo']])

# df = pd.read_sql(""" SELECT c.nome_categoria, p.preco_venda FROM produtos p JOIN categorias c ON p.categoria_id = c.categoria_id """, con=engine)

# media_por_categoria = df.groupby('nome_categoria')['preco_venda'].mean()
# print(media_por_categoria)

# Prática
# Listar os produtos mais vendidos (em quantidade) e o total vendido por produto

df_vendas = pd.read_sql(""" SELECT p.nome_produto, SUM(v.quantidade) AS total_vendido
                            FROM vendas v
                            JOIN produtos p ON v.produto_id = p.produto_id
                            GROUP BY p.nome_produto
                            ORDER BY total_vendido DESC """, con=engine)

print(df_vendas)
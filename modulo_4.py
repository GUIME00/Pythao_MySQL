import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

query = """SELECT
    p.nome_produto,
    SUM(i.quantidade) AS total_vendido
FROM itens_pedido i
JOIN produtos p ON i.produto_id = p.produto_id
GROUP BY p.nome_produto
ORDER BY total_vendido DESC
LIMIT 10 """

df = pd.read_sql(query, con=engine)

# MATPLOTLIB
plt.figure(figsize=(12, 6))
plt.bar(df['nome_produto'], df['total_vendido'], color='darkblue') # bar = vertical e barh = horizontal
plt.xlabel('Total Vendido')
plt.ylabel('Produtos')
plt.title('Top 10 Produtos Mais Vendidos')
plt.xticks(rotation=45, ha='right')
plt.show()

# GRÁFICO DE PIZZA
plt.figure(figsize=(8, 8))
plt.pie(df['total_vendido'], labels=df['nome_produto'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
# plt.pie(df['total_vendido'], labels=df['nome_produto'], autopct='%1.1f%%')
plt.title('TOP 10 dos Produtos Mais Vendidos')
# plt.axis('equal')
plt.show()

query2 = """
SELECT
    data_pedido AS mes,
    COUNT(*) AS total_pedidos
FROM pedidos
GROUP BY mes
ORDER BY mes
LIMIT 12
"""
df_mensal = pd.read_sql(query2, con=engine)
plt.figure(figsize=(12, 6))
plt.plot(df_mensal['mes'], df_mensal['total_pedidos'], marker='o', linestyle='-', color='green')
plt.xlabel('Mês')
plt.ylabel('Total de Pedidos')
plt.title('Total de Pedidos por Mês')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")


# LENDO DADOS DE PRODUTOS 
df = pd.read_sql("SELECT preco_custo, preco_venda, estoque_atual FROM produtos", con=engine)

# CONVERTE COLUNAS EM ARRAY
preco_custo = df['preco_custo'].to_numpy()
preco_venda = df['preco_venda'].to_numpy()
estoque_atual = df['estoque_atual'].to_numpy()

# print(preco_custo)

print("Preço médio de venda:", np.mean(preco_venda))
print("Preço mediano de venda:", np.median(preco_venda))
print("Desvio padrão de venda:", np.std(preco_venda))
print("Produto mais caro:", np.max(preco_venda))
print("Produto mais barato:", np.min(preco_venda))


# CALCULAR LUCRO UNITÁRIO
lucro_unitario = preco_venda - preco_custo
print("Lucro unitário:", lucro_unitario)

# LUCRO TOTAL
lucro_total = np.sum(lucro_unitario * estoque_atual)
print("Lucro total por produto em estoque:", lucro_total)

indices = lucro_unitario < 10
producoes_com_lucro_baixo = df[indices]
print(producoes_com_lucro_baixo[['preco_custo', 'preco_venda', 'estoque_atual']])

# ÍNDICE DE RENTABILIDADE
indice_rentabilidade = (lucro_unitario / preco_custo) * 100
df['rentabilidade'] = np.round(indice_rentabilidade, 2)
print(df[['preco_custo', 'preco_venda', 'rentabilidade']])

# PRODUTOS COM RENTABILIDADE ABAIXO DA MÉDIA
media_rentabilidade = df['rentabilidade'].mean()
produtos_com_rentabilidade_baixa = df[df['rentabilidade'] < media_rentabilidade]
print(produtos_com_rentabilidade_baixa[['preco_custo', 'preco_venda', 'rentabilidade']])
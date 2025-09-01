import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

query = """
SELECT
    p.nome_produto,
    SUM(i.quantidade) AS total_vendido,
    AVG(i.preco_unitario) AS preco_medio,
    SUM(i.quantidade * i.preco_unitario) AS faturamento
FROM itens_pedido i
JOIN produtos p ON p.produto_id = i.produto_id
GROUP BY p.produto_id
"""

df = pd.read_sql(query, con=engine)

print(df)

x = df[['total_vendido', 'preco_medio']] # Features/Entradas
y = df['faturamento'] # Target/Saída

# treinar o modelo
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(x_treino, y_treino)

# fazer previsões
y_pred = modelo.predict(x_teste)

# avaliar o modelo
mse = mean_squared_error(y_teste, y_pred)
r2 = r2_score(y_teste, y_pred)

print(f"MSE: {mse:.2f}") # Erro Quadrático Médio
print(f"R²: {r2:.2f}") # Coeficiente de Determinação
print(f"RMSE: {math.sqrt(mse):.2f}") # Raiz do Erro Quadrático Médio
# Este modelo é capaz de prever o faturamento com base nas vendas e no preço médio dos produtos.

# Prever um dado novo
novo_produto = pd.DataFrame([[500,35.00]], columns=['total_vendido', 'preco_medio'])

previsao = modelo.predict(novo_produto)
print(f"Previsão de faturamento estimado para 500 unidades a R$ 35,00 do novo produto: R$ {previsao[0]:.2f}")

plt.figure(figsize=(10, 6))
# plt.scatter(y_teste, y_pred, color='blue')
# plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
# plt.title("Comparação entre Valores Reais e Previsto")
# plt.xlabel("Valores Reais")
# plt.ylabel("Valores Previsto")
# plt.show()
plt.plot(y_teste.values[:70], label='Valores Reais', marker='o')
plt.plot(y_pred[:70], label='Valores Previsto', marker='x')
plt.title("Comparação entre Valores Reais e Previsto")
plt.xlabel("Amostras")
plt.ylabel("Valores")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
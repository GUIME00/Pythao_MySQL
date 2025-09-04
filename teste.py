import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

url_bitcoin = "bitcoin_historico.csv"
# ETAPA 1 - Leitura e organização dos dados

df_bitcoin = pd.read_csv(url_bitcoin)

# Converta a coluna Data para o tipo datetime
df_bitcoin['Data'] = pd.to_datetime(df_bitcoin['Data'], format='%d.%m.%Y')

# Ordene os dados da mais antiga para a mais recente
df_bitcoin = df_bitcoin.sort_values('Data')

# ETAPA 2 - Limpeza e transformação dos dados

df_bitcoin['Último'] = pd.to_numeric(df_bitcoin['Último'], errors='coerce')
df_bitcoin['Abertura'] = pd.to_numeric(df_bitcoin['Abertura'], errors='coerce')
df_bitcoin['Máxima'] = pd.to_numeric(df_bitcoin['Máxima'], errors='coerce')
df_bitcoin['Mínima'] = pd.to_numeric(df_bitcoin['Mínima'], errors='coerce')
df_bitcoin['Vol.'] = pd.to_numeric(df_bitcoin['Vol.'], errors='coerce')
df_bitcoin['Var%'] = pd.to_numeric(df_bitcoin['Var%'], errors='coerce')

# Trate os sufixos da coluna Vol. (K,M,B) transformando em valores numéricos reais
df_bitcoin['Vol.'] = df_bitcoin['Vol.'].str.replace('K', 'e3').str.replace('M', 'e6').str.replace('B', 'e9').astype(float)

# ETAPA 3 - Separação dos dados

# Treino: de 01.01.2020 até 16.08.2025
df_treino = df_bitcoin[(df_bitcoin['Data'] >= '2020-01-01') & (df_bitcoin['Data'] <= '2025-08-16')]

# Teste: de 17.08.2025 até 01.09.2025
df_teste = df_bitcoin[(df_bitcoin['Data'] > '2025-08-17') & (df_bitcoin['Data'] <= '2025-09-01')]

# ETAPA 4 - Treinamento do modelo
X = df_treino.drop(['Data', 'Último'], axis=1)
y = df_treino['Último']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# ETAPA 5 - previsão e avaliação do modelo
# Realizando previsões
y_pred = model.predict(X_val)

# Avaliando o modelo utilizando
# Erro médio quadrático 
mse = mean_squared_error(y_val, y_pred)
# Coeficiente de determinação
r2 = r2_score(y_val, y_pred)

# Etapa 6 - Visualização dos resultados

plt.figure(figsize=(12, 6))
plt.plot(y_val.index, y_val, label='Real', color='blue', marker='o')
plt.plot(y_val.index, y_pred, label='Previsto', color='red', marker='x')
plt.title('Previsão do Preço do Bitcoin')
plt.xlabel('Data')
plt.ylabel('Preço(USD)')
plt.legend()
plt.show()
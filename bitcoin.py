import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

url_bitcoin = "bitcoin_historico.csv"
# ETAPA 1 - Leitura e organização dos dados
# Leia o arquivo csv
df_bitcoin = pd.read_csv(url_bitcoin)

# Converta a coluna Data para o tipo datetime
df_bitcoin['Data'] = pd.to_datetime(df_bitcoin['Data'])

# Ordene os dados da mais antiga para a mais recente
df_bitcoin = df_bitcoin.sort_values('Data')

# ETAPA 2 - Limpeza e transformação dos dados
# Converta as colunas
df_bitcoin['Último'] = df_bitcoin['Último'].str.replace(',', '.').astype(float)
df_bitcoin['Abertura'] = df_bitcoin['Abertura'].str.replace(',', '.').astype(float)
df_bitcoin['Máxima'] = df_bitcoin['Máxima'].str.replace(',', '.').astype(float)
df_bitcoin['Mínima'] = df_bitcoin['Mínima'].str.replace(',', '.').astype(float)
df_bitcoin['Vol.'] = df_bitcoin['Vol.'].str.replace('.', '').str.replace(',', '.').astype(float)
df_bitcoin['Var%'] = df_bitcoin['Var%'].str.replace('%', '').str.replace(',', '.').astype(float)

# Trate os sufixos da coluna Vol. (K,M,B) transformando em valores numéricos reais
df_bitcoin['Vol.'] = df_bitcoin['Vol.'].str.replace('K', 'e3').str.replace('M', 'e6').str.replace('B', 'e9').astype(float)

# ETAPA 3 - Separação dos dados
# Separe dados em:
# Treino: de 01.01.2020 até 16.08.2025
df_treino = df_bitcoin[(df_bitcoin['Data'] >= '01.01.2020') & (df_bitcoin['Data'] <= '16.08.2025')]

# Teste: de 17.08.2025 até 01.09.2025
df_teste = df_bitcoin[(df_bitcoin['Data'] > '17.08.2025') & (df_bitcoin['Data'] <= '01.09.2025')]

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
# Crie um gráfico de linha para comparar os valores reais e previstos
# O eixo X deve ser a Data e o eixo Y deve ser o valor da cotação

plt.figure(figsize=(12, 6))
plt.plot(y_val.index, y_val, label='Real', color='blue')
plt.plot(y_val.index, y_pred, label='Previsto', color='red')
plt.title('Previsão do Preço do Bitcoin')
plt.xlabel('Data')
plt.ylabel('Var%')
plt.legend()
plt.show()
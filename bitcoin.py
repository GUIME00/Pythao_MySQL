import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# ETAPA 1 - Leitura e organização dos dados

url_bitcoin = "bitcoin_historico.csv"

df_bitcoin = pd.read_csv(url_bitcoin)

# Converter coluna Data para datetime
df_bitcoin['Data'] = pd.to_datetime(df_bitcoin['Data'], format='%d.%m.%Y')

# Ordenar da data mais antiga para a mais recente
df_bitcoin = df_bitcoin.sort_values('Data').reset_index(drop=True)


# ETAPA 2 - Limpeza e transformação dos dados


# Remover caracteres como "," e converter para número
for col in ['Último', 'Abertura', 'Máxima', 'Mínima']:
    df_bitcoin[col] = (
        df_bitcoin[col].astype(str)
        .str.replace(',', '', regex=False)
        .astype(float)
    )

# Tratar coluna "Vol."
def converter_volume(valor):
    if pd.isna(valor) or valor == '-':
        return 0
    valor = valor.replace(',', '.')
    if 'K' in valor:
        return float(valor.replace('K', '')) * 1e3
    elif 'M' in valor:
        return float(valor.replace('M', '')) * 1e6
    elif 'B' in valor:
        return float(valor.replace('B', '')) * 1e9
    else:
        return float(valor)

df_bitcoin['Vol.'] = df_bitcoin['Vol.'].astype(str).apply(converter_volume)

# Tratar coluna "Var%"
df_bitcoin['Var%'] = (
    df_bitcoin['Var%']
    .astype(str)
    .str.replace('%', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)


# ETAPA 3 - Separação dos dados (treino e teste)

df_treino = df_bitcoin[(df_bitcoin['Data'] >= '2020-01-01') & (df_bitcoin['Data'] <= '2025-08-16')]
df_teste = df_bitcoin[(df_bitcoin['Data'] >= '2025-08-17') & (df_bitcoin['Data'] <= '2025-09-01')]


# ETAPA 4 - Preparação para treinamento

X = df_treino.drop(['Data', 'Último'], axis=1)
y = df_treino['Último']

# Divisão em treino/validação
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = LinearRegression()
model.fit(X_train, y_train)


# ETAPA 5 - Avaliação do modelo

y_pred = model.predict(X_val)

# Métricas
mse = mean_squared_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

print(f"Erro Médio Quadrático (MSE): {mse:.2f}")
print(f"Coeficiente de Determinação (R²): {r2:.2f}")


# ETAPA 6 - Visualização dos resultados

plt.figure(figsize=(12, 6))
plt.plot(y_val.values, label='Real', color='blue', marker='o')
plt.plot(y_pred, label='Previsto', color='red', marker='x')
plt.title('Previsão do Preço do Bitcoin')
plt.xlabel('Observações')
plt.ylabel('Preço (USD)')
plt.legend()
plt.show()
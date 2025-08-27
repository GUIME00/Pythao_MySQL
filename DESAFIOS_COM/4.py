import pymysql
import pandas as pd

# SE CONECTA AO BANCO DE DADOS
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='sistema_vendas',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


# # AGRUPE OS PEDIDOS POR FORMA DE PAGAMENTO E CALCULE O VALOR MÉDIO DE FRETE - USANDO PANDAS
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM pedidos")
        pedidos = cursor.fetchall()

    # CONVERTE PARA DATAFRAME
    df = pd.DataFrame(pedidos)

    # AGRUPA POR FORMA DE PAGAMENTO E CALCULA A MÉDIA DE FRETE
    media_frete = df.groupby('forma_pagamento')['valor_frete'].mean().reset_index()
    print(media_frete)

except Exception as e:
    print(f"Erro ao agrupar pedidos: {e}")
finally:
    conexao.close()
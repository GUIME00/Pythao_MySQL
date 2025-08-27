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

# # LISTE OS PRODUTOS COM STATUS "DESCONTINUADO" - USANDO PANDAS
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos WHERE status_produto = 'DESCONTINUADO'")
        produtos = cursor.fetchall()

    # CONVERTE PARA DATAFRAME
    df = pd.DataFrame(produtos)

    # MOSTRA OS DADOS
    print(df[['nome_produto', 'preco_venda', 'status_produto']])

except Exception as e:
    print(f"Erro ao listar produtos: {e}")
finally:
    conexao.close()
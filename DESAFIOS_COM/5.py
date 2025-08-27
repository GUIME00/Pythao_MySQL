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


# # LISTE OS 5 PRODUTOS COM MENOR MARGEM DE LUCRO (preco_venda - preco_custo) - USANDO PANDAS
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

    # CONVERTE PARA DATAFRAME
    df = pd.DataFrame(produtos)

    # CALCULA A MARGEM DE LUCRO
    df['margem_lucro'] = df['preco_venda'] - df['preco_custo']

    # LISTA OS 5 PRODUTOS COM MENOR MARGEM DE LUCRO
    produtos_menor_margem = df.nsmallest(5, 'margem_lucro')
    print(produtos_menor_margem)

except Exception as e:
    print(f"Erro ao listar produtos: {e}")
finally:
    conexao.close()
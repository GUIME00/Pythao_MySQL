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


# # FILTRE OS FORNECEDORES DA CIDADE DE "Maringá" E STATUS "Ativo" - USANDO PANDAS
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM fornecedores WHERE cidade = 'Maringá' AND status_fornecedor = 'Ativo'")
        fornecedores = cursor.fetchall()

    # CONVERTE PARA DATAFRAME
    df = pd.DataFrame(fornecedores)

    # MOSTRA OS DADOS
    print(df[['nome_fornecedor', 'cidade', 'status_fornecedor']])

except Exception as e:
    print(f"Erro ao listar fornecedores: {e}")
finally:
    conexao.close()
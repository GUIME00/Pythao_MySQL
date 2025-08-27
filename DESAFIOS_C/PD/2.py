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

# CALCULE O VALOR TOTAL DO ESTOQUE (preco_venda * estoque_atual) - USANDO PANDAS
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

    # CONVERTE PARA DATAFRAME
    df = pd.DataFrame(produtos)

    # CALCULA O VALOR TOTAL DO ESTOQUE
    df['valor_total_estoque'] = df['preco_venda'] * df['estoque_atual']
    valor_total = df['valor_total_estoque'].sum()
    print(f"Valor total do estoque: {valor_total}")

except Exception as e:
    print(f"Erro ao calcular valor total do estoque: {e}")
finally:
    conexao.close()
import pymysql

# SE CONECTA AO BANCO DE DADOS
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='sistema_vendas',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# CALCULE O VALOR TOTAL DO ESTOQUE (preco_venda * estoque_atual)
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT SUM(preco_venda * estoque_atual) AS valor_total_estoque FROM produtos")
        resultado = cursor.fetchone()
        print(f"Valor total do estoque: {resultado['valor_total_estoque']}")

except Exception as e:
    print(f"Erro ao calcular valor total do estoque: {e}")
finally:
    conexao.close()
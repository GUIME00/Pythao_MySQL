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

# AGRUPE OS PEDIDOS POR FORMA DE PAGAMENTO E CALCULE O VALOR MÉDIO DE FRETE
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT forma_pagamento, AVG(valor_frete) AS media_frete FROM pedidos GROUP BY forma_pagamento")
        resultados = cursor.fetchall()

    # MOSTRA OS DADOS
        for resultado in resultados:
            print(f"Forma de Pagamento: {resultado['forma_pagamento']} - Média de Frete: {resultado['media_frete']}")

except Exception as e:
    print(f"Erro ao agrupar pedidos: {e}")
finally:
    conexao.close()
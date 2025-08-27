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

# # LISTE OS PRODUTOS COM STATUS "DESCONTINUADO"
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos WHERE status_produto = 'DESCONTINUADO'")
        produtos = cursor.fetchall()

    # MOSTRA OS DADOS
        for produto in produtos:
            print(f"Produto: {produto['nome_produto']} - Preço: {produto['preco_venda']} - Status: {produto['status_produto']}")

except Exception as e:
    print(f"Erro ao listar produtos: {e}")
finally:
    conexao.close()
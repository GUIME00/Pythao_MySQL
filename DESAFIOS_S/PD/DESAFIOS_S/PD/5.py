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

# LISTE OS 5 PRODUTOS COM MENOR MARGEM DE LUCRO (preco_venda - preco_custo)
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos ORDER BY (preco_venda - preco_custo) ASC LIMIT 5")
        produtos = cursor.fetchall()

    # MOSTRA OS DADOS
        for produto in produtos:
            print(f"Produto: {produto['nome_produto']} - Margem de Lucro: {produto['preco_venda'] - produto['preco_custo']}")

except Exception as e:
    print(f"Erro ao listar produtos: {e}")
finally:
    conexao.close()
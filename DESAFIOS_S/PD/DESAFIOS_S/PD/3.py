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

# FILTRE OS FORNECEDORES DA CIDADE DE "Maringá" E STATUS "Ativo"
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM fornecedores WHERE cidade = 'Maringá' AND status_fornecedor = 'Ativo'")
        fornecedores = cursor.fetchall()

    # MOSTRA OS DADOS
        for fornecedor in fornecedores:
            print(f"Fornecedor: {fornecedor['nome_fornecedor']} - CNPJ: {fornecedor['cnpj']} - Cidade: {fornecedor['cidade']} - Status: {fornecedor['status_fornecedor']}")

except Exception as e:
    print(f"Erro ao listar fornecedores: {e}")
finally:
    conexao.close()
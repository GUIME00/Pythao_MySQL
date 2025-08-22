import pymysql

conexao = pymysql.connect(
    host='localhost',             # ENDEREÇO DO BANCO DE DADOS  
    user='root',                  # USUÁRIO
    password='123456',            # SENHA DO SEU MYSQL
    database='sistema_escolar',   # NOME DO SEU BANCO DE DADOS
    charset='utf8mb4',            # PADRÃO DE ACENTUAÇÃO
    cursorclass=pymysql.cursors.DictCursor # RETORNA LINHAS COMO DICIONÁRIOS (CHAVE:COLUNA)
)

""" # ENVIANDO UM SELECT PARA O BANCO DE DADOS
with conexao.cursor() as cursor:
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall() # RETORNA TODOS OS ALUNOS
    
    # MOSTRA OS DADOS
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']} - Email: {aluno['email']} - Semestre: {aluno['semestre_atual']}") """


# ESSE CÓDIGO INSERE UM NOVO ALUNO NO BANCO DE DADOS
""" with conexao.cursor() as cursor:
    sql = "INSERT INTO alunos (nome, email, telefone, data_nascimento, curso_id, semestre_atual, status_aluno, data_matricula) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    valores = ("Luciana Souza", "luciana@melo.com","4999999999", "2001-03-12", 1, 2, "Ativo", "2024-08-01")
    cursor.execute(sql, valores)
    conexao.commit() # SALVANDO BANCO """


""" # ESSE CÓDIGO ATUALIZA UM ALUNO NO BANCO DE DADOS
with conexao.cursor() as cursor:
    sql = "UPDATE alunos SET telefone = %s WHERE aluno_id = %s" # WHERE - IMPORTANTE PARA ESPECIFICAR
    valores = ("(49) 9999-4578", 601)
    cursor.execute(sql, valores)
    conexao.commit() # SALVANDO BANCO  """


""" # DELETAR DADOS DO BANCO DE DADOS
try:
    with conexao.cursor() as cursor:
        sql = "DELETE FROM alunos WHERE aluno_id = %s"
        valores = (601,)
        cursor.execute(sql, valores)
        conexao.commit() # SALVANDO BANCO
except Exception as e:
    print(f"Erro ao deletar aluno: {e}")
finally:
    conexao.close() """


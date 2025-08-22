import pymysql

# SE CONECTA AO BANCO DE DADOS
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='sistema_escolar',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

#LISTA TODOS OS ALUNOS COM NOME, EMAIL, SEMESTRE E STATUS
try:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall() # RETORNA TODOS OS ALUNOS

    # MOSTRA OS DADOS
        for aluno in alunos:
            print(f"Aluno: {aluno['nome']} - Email: {aluno['email']} - Semestre: {aluno['semestre_atual']} - Status: {aluno['status_aluno']}")

# PERMITE CADASTRAR UM NOVO ALUNO COM DADOS DIGITADOS PELO USUÁRIO
    aluno = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    semestre = input("Digite o semestre do aluno: ")
    status = input("Digite o status do aluno: ")

    with conexao.cursor() as cursor:
        sql = "INSERT INTO alunos (nome, email, semestre_atual, status_aluno) VALUES (%s, %s, %s, %s)"
        valores = (aluno, email, semestre, status)
        cursor.execute(sql, valores)
        conexao.commit() # SALVANDO BANCO
except Exception as e:
    print(f"Erro ao cadastrar aluno: {e}")
finally:
    conexao.close()
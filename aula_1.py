import pymysql
# 1: Consulta Básica Crie uma função que liste todas as disciplinas disponíveis no sistema, mostrando: 
# - ID da disciplina 
# - Nome da disciplina 
# - Carga horária 
# - Número de alunos matriculados

# def listar_disciplinas():
#     conexao = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='123456',
#         database='sistema_escolar',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     try:
#         with conexao.cursor() as cursor:
#             cursor.execute("SELECT id, nome, carga_horaria, num_alunos FROM disciplinas VALUES (%s, %s, %s, %s)")
#             disciplinas = cursor.fetchall()
#             for disciplina in disciplinas:
#                 print(f"ID: {disciplina['id']}, Nome: {disciplina['nome']}, Carga Horária: {disciplina['carga_horaria']}, Alunos Matriculados: {disciplina['num_alunos']}")
#     finally:
#         conexao.close()
# listar_disciplinas()


# 2: Relatório de Turmas Desenvolva uma função que gere um relatório de todas as turmas, incluindo:
# - Código da turma 
# - Disciplina 
# - Professor
# - Semestre 
# - Número de alunos matriculados 
# - Média geral da turma

# def relatorio_turmas():
#     conexao = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='123456',
#         database='sistema_escolar',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     try:
#         with conexao.cursor() as cursor:
#             cursor.execute("SELECT codigo, disciplina, professor, semestre, num_alunos, media_geral FROM turmas VALUES (%s, %s, %s, %s, %s, %s)")
#             turmas = cursor.fetchall()
#             for turma in turmas:
#                 print(f"Código: {turma['codigo']}, Disciplina: {turma['disciplina']}, Professor: {turma['professor']}, Semestre: {turma['semestre']}, Alunos Matriculados: {turma['num_alunos']}, Média Geral: {turma['media_geral']}")
#     finally:
#         conexao.close()
# relatorio_turmas()

# 3: Sistema de Busca Implemente um sistema de busca que permita encontrar alunos por: 
# - Nome (busca parcial) 
# - Email 
# - Status 
# - Curso

# def buscar_alunos(criterio, valor):
#     conexao = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='123456',
#         database='sistema_escolar',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     try:
#         with conexao.cursor() as cursor:
#             sql = f"SELECT * FROM alunos WHERE {criterio} LIKE %s"
#             cursor.execute(sql, ('%' + valor + '%',))
#             alunos = cursor.fetchall()
#             for aluno in alunos:
#                 print(f"ID: {aluno['aluno_id']}, Nome: {aluno['nome']}, Email: {aluno['email']}, Status: {aluno['status_aluno']}, Curso: {aluno['curso_id']}")
#     finally:
#         conexao.close()
# buscar_alunos('nome', 'Ana')

# 4: Análise de Performance Crie funções para analisar: 
# - Alunos com média acima de 8.0 
# - Disciplinas com maior índice de reprovação 
# - Cursos com maior número de formandos


# def analisar_performance():
#     conexao = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='123456',
#         database='sistema_escolar',
#         cursorclass=pymysql.cursors.DictCursor
#     )

#     try:
#         with conexao.cursor() as cursor:
            
#             # 1. Alunos com média > 8.0
#             cursor.execute("SELECT aluno_id, nome, media FROM alunos WHERE media > 8.0")
#             alunos = cursor.fetchall()
#             print("Alunos com média acima de 8.0:")
#             for aluno in alunos:
#                 print(f"ID: {aluno['aluno_id']}, Nome: {aluno['nome']}, Média: {aluno['media']}")
#             print("-"*60)

#             # 2. Disciplinas com índice de reprovação > 0.5
#             cursor.execute("SELECT disciplina_id, nome_disciplina, indice_reprovacao FROM disciplinas WHERE indice_reprovacao > 0.5")
#             disciplinas = cursor.fetchall()
#             print("Disciplinas com maior índice de reprovação:")
#             for disciplina in disciplinas:
#                 print(f"ID: {disciplina['disciplina_id']}, Nome: {disciplina['nome_disciplina']}, Índice de Reprovação: {disciplina['indice_reprovacao']}")
#             print("-"*60)

#             # 3. Cursos com mais de 100 formandos
#             cursor.execute("SELECT curso_id, nome_curso, num_formandos FROM cursos WHERE num_formandos > 100")
#             cursos = cursor.fetchall()
#             print("Cursos com maior número de formandos:")
#             for curso in cursos:
#                 print(f"ID: {curso['curso_id']}, Nome: {curso['nome_curso']}, Número de Formandos: {curso['num_formandos']}")
#             print("-"*60)

#     finally:
#         conexao.close()

# # Chamada da função
# analisar_performance()
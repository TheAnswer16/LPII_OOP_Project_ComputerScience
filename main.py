from service.aluno_dao import *
from service.professor_dao import *
from service.disciplina_dao import *
from service.curso_dao import *

print ("---------- BEM VINDO ----------\n\n")

print("O que você deseja realizar? \n\n")

professores = []
alunos = []
disciplinas = []
cursos = []

op = 0

while op != 5:

    print("1 - Gerenciar Alunos\n")
    print("2 - Gerenciar Professores\n")
    print("3 - Gerenciar Disciplinas\n")
    print("4 - Gerenciar Cursos\n")
    print("5 - Sair\n")

    op = int(input())

    if (op == 1):
        aluno = cadastrarAluno()
        alunos.append(aluno)
    elif(op == 2):
        professor = cadastrarProfessor()
        professores.append(professor)
    elif(op == 3):
        disciplina = cadastrarDisciplina(professores)
        disciplinas.append(disciplina)
    elif(op == 4):
        curso = cadastrarCurso(disciplinas, alunos)
        cursos.append(curso)
    elif(op == 5):
        break
    else:
        print("Digite uma opção válida!\n")

print ("Alunos Cadastrados: \n")

for index, a in enumerate(alunos):

    print("Matricula: " + a.get_matricula() + "\n")
    print("Nome: " + a.get_nome() + "\n")
    print("Data de nascimento " + a.get_data_nasc() + "\n\n")


print ("Professores Cadastrados: \n")

for index, p in enumerate(professores):

    print("Matricula" + p.get_matricula() + "\n")
    print("Nome: " + p.get_nome() + "\n")
    print("Data de nascimento " + p.get_data_nasc() + "\n\n")

print ("Disciplinas Cadastradas \n")

for index, d in enumerate(disciplinas):

    print("Nome: " + d.get_nome() + "\n")
    print("Professores: \n")
    
    for p in d.get_professores():

        print("\\" + p.get_nome() + "\n")

print ("\n\n Cursos Cadastrados: ")

for index, c in enumerate(cursos):

    print("Nome: " + c.get_nome() + "\n")
    print("Disciplinas: \n")

    for d in c.get_disciplinas():

        print("\\" + d.get_nome() + "\n")

    print("Alunos(as): \n")

    for a in c.get_alunos():

        print("\\" + d.get_nome() + "\n")
        


    
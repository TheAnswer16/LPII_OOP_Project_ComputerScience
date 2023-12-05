from models.Curso import Curso

def cadastrarCurso(disciplinas, alunos):

    if len(disciplinas) <= 0:
        print("Nenhuma disciplina cadastrada")
        return

    if len(alunos) <= 0:
        print("Nenhum(a) aluno(a) cadastrada")
        return

    print("Digite o nome do curso: \n")
    nome_curso = str(input())

    print("Digite o tipo do curso (Superior, Téncico, etc): ")
    tipo_curso = str(input())

    print("Digite o numero das disciplinas desse curso separando por ','\n")
    print("Exemplo: '1,2,3'")

    for index, d in enumerate(disciplinas):
        print (str(index) + ' - ' + d.get_nome())
    
    disciplinas_curso = str(input())
        
    disciplinas_curso = disciplinas_curso.split(',')

    dc = []

    for x in disciplinas_curso:
        dc.append(disciplinas[int(x)])

    print("Digite o numero dos alunos desse curso separando por ','\n")
    print("Exemplo: '1,2,3'")

    for index, a in enumerate(alunos):
        print (str(index) + ' - ' + a.get_nome())
    
    alunos_curso = str(input())
        
    alunos_curso = alunos_curso.split(',')

    ac = []

    for x in alunos_curso:
        ac.append(alunos[int(x)])

    curso = Curso(nome_curso, tipo_curso, dc, ac)

    return curso
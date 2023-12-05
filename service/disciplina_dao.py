from models.Disciplina import Disciplina

def cadastrarDisciplina(professores):

    if len(professores) <= 0:
        print("Nenhum professor cadastrado")
        return

    print("Digite o nome da disciplina: \n")
    nome_disciplina = str(input())

    print("Digite o numero dos professores dessa disciplina separando por ','\n")
    print("Exemplo: '1,2,3'")

    for index, p in enumerate(professores):
        print (str(index) + ' - ' + p.get_nome())
    
    professores_disciplina = str(input())
        
    professores_disciplina = professores_disciplina.split(',')

    pd = []

    for x in professores_disciplina:
        pd.append(professores[int(x)])

    disciplina = Disciplina(nome_disciplina, pd)

    return disciplina





        

from models.Professor import Professor

def cadastrarProfessor():

    print("Digitar matricula: \n")
    matricula = str(input())

    print("Digitar nome: \n")
    nome = str(input())

    print("Digitar CPF: \n")
    cpf = str(input())

    print("Digitar data de nascimento: \n")
    data_nasc = str(input())

    print("Digitar endereco: \n")
    endereco = str(input())

    print("Digitar bairro: \n")
    bairro = str(input())

    print("Digitar numero: \n")
    numero = str(input())

    print("Digitar cidade: \n")
    cidade = str(input())

    print("Digitar estado: \n")
    estado = str(input())

    professor = Professor(matricula, nome, cpf, data_nasc, endereco, bairro, numero, cidade, estado)

    return professor
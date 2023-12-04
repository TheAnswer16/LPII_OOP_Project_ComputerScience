from models.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, matricula, nome, cpf, data_nasc, endereco, bairro, numero, cidade, estado):
        super().__init__(matricula, nome, cpf, data_nasc, endereco, bairro, numero, cidade, estado)

    def realiza_atividade(self):
        print("Preparando prova...")

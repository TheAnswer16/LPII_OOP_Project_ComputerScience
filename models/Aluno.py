from models.Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula, nome, cpf, data_nasc, endereco, bairro, numero, cidade, estado, interno):
        super().__init__(matricula, nome, cpf, data_nasc, endereco, bairro, numero, cidade, estado)
        self.interno = interno
        
    def realiza_atividade(self):
        print("Estudando para prova...")
    

    def get_interno(self):
        
        if self.interno == 1:
            return "Sim"
        else:
            return "Nao"

    def set_interno(self, interno):
        self.interno = interno


class Pessoa:
    def __init__(self, matricula, nome, cpf, data_nasc, endereco, bairro, numero, cidade, estado):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def realiza_atividade(self):
        pass
    
    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_data_nasc(self):
        return self.data_nasc

    def set_data_nasc(self, data_nasc):
        self.data_nasc = data_nasc

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_bairro(self):
        return self.bairro

    def set_bairro(self, bairro):
        self.bairro = bairro

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

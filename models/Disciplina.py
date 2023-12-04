class Disciplina:
    def __init__(self, nome, tipo, professores):
        self.nome = nome
        self.tipo = tipo
        self.professores = professores

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo
        
    def get_professores(self):
        return self.professores
    
    def set_professores(self, professores):
        self.professores = professores

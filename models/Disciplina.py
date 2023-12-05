class Disciplina:
    def __init__(self, nome, professores):
        self.nome = nome
        self.professores = professores

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
        
    def get_professores(self):
        return self.professores
    
    def set_professores(self, professores):
        self.professores = professores

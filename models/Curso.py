class Curso:
    def __init__(self, nome, tipo,disciplinas, alunos):
        self.nome = nome
        self.tipo = tipo
        self.disciplinas = disciplinas
        self.alunos = alunos

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_disciplinas(self):
        return self.disciplinas

    def set_disciplinas(self, disciplinas):
        self.disciplinas = disciplinas

    def get_alunos(self):
        return self.alunos
    
    def set_alunos(self, alunos):
        self.alunos = alunos

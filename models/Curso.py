class Curso:
    def __init__(self, nome, disciplinas):
        self.nome = nome
        self.disciplinas = disciplinas

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_disciplinas(self):
        return self.disciplinas

    def set_disciplinas(self, disciplinas):
        self.disciplinas = disciplinas

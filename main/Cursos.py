class Curso:
    def __init__(self, cod_curso: str, descricao: str):
        self.cod_curso = cod_curso
        self.descricao = descricao

    def __str__(self):
        return f"Curso(código='{self.cod_curso}', descrição='{self.descricao}')"

    def atualizar_descricao(self, nova_descricao: str):
        self.descricao = nova_descricao
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(dados: dict):
        return Curso(**dados)
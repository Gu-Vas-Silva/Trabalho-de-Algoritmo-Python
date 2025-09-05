class Curso:
    def __init__(self, codigo: str, descricao: str):
        self.codigo = codigo
        self.descricao = descricao

    def __str__(self):
        return f"Curso(código='{self.codigo}', descrição='{self.descricao}')"

    def atualizar_descricao(self, nova_descricao: str):
        self.descricao = nova_descricao
    
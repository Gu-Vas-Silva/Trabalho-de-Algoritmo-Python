class Categoria:
    def __init__(self, cod_categoria: str, descricao: str):
        self.cod_categoria = cod_categoria
        self.descricao = descricao

    def __str__(self):
        return f"Categoria(cod_categoria='{self.cod_categoria}', descricao='{self.descricao}')"

    def atualizar_descricao(self, nova_descricao: str):
        self.descricao = nova_descricao

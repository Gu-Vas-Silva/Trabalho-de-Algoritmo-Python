class Livro:
    def __init__(self, cod_livro: str, titulo: str, cod_autor: str, cod_categoria: str,
                 ano_publicacao: int, disponibilidade: bool = True):
        self.cod_livro = cod_livro
        self.titulo = titulo
        self.cod_autor = cod_autor
        self.cod_categoria = cod_categoria
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade

    def __str__(self):
        status = "Disponível" if self.disponibilidade else "Indisponível"
        return (f"Livro(cod_livro='{self.cod_livro}', titulo='{self.titulo}', "
                f"cod_autor='{self.cod_autor}', cod_categoria='{self.cod_categoria}', "
                f"ano_publicacao={self.ano_publicacao}, disponibilidade='{status}')")

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            return True
        return False

    def devolver(self):
        self.disponibilidade = True

    def atualizar_titulo(self, novo_titulo: str):
        self.titulo = novo_titulo

class Livro:
    autores_dict = {}
    categorias_dict = {}
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
            if self.disponibilidade is True:
                return "disponivel"
            return "indisponivel"

    def atualizar_disponibilidade(self, disponivel: bool):
        self.disponibilidade = disponivel


    def descricao_autores(self):
        autor = self.autores_dict.get(self.cod_autor)
        if autor:
            return f"{autor.nome} ({autor.descricao_cidade()})"
        return "autor não encontrado"

    def descricao_categorias(self):
        return self.categorias_dict.get(self.cod_categoria, "categoria não encontrada")
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(dados: dict):
        return Livro(**dados)
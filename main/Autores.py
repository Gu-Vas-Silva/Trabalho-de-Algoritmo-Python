class Autor:
    cidades_dict = {}
    def __init__(self, cod_autor: str, nome: str, cod_cidade: str):
        self.cod_autor = cod_autor
        self.nome = nome
        self.cod_cidade = cod_cidade

    def __str__(self):
        return (f"Autor(cod_autor='{self.cod_autor}', nome='{self.nome}', "
                f"cod_cidade='{self.cod_cidade}')")

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def atualizar_cidade(self, novo_cod_cidade: str):
        self.cod_cidade = novo_cod_cidade

    def descricao_cidade(self):
        cidade = self.cidades_dict.get(self.cod_cidade)
        if cidade:
            return f"{cidade.descricao} - {cidade.estado}"
        return "Cidade não encontrada"
         
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(dados: dict):
        return Autor(**dados)
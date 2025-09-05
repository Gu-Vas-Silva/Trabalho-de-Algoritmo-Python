class Cidade:
    def __init__(self, cod_cidade: str, descricao: str, estado: str):
        self.cod_cidade = cod_cidade
        self.descricao = descricao
        self.estado = estado

    def __str__(self):
        return (f"Cidade(cod_cidade='{self.cod_cidade}', "
                f"descricao='{self.descricao}', estado='{self.estado}')")

    def atualizar_descricao(self, nova_descricao: str):
        self.descricao = nova_descricao

    def atualizar_estado(self, novo_estado: str):
        self.estado = novo_estado
from datetime import date, datetime, timedelta

class Emprestimo:
    livro_dict = {}
    aluno_dict = {}
    def __init__(self, cod_emprestimo: str, cod_livro: str, cod_aluno: str,
                 data_emprestimo, data_devolucao, devolvido: bool = False):
        self.cod_emprestimo = cod_emprestimo
        self.cod_livro = cod_livro
        self.cod_aluno = cod_aluno
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.devolvido = devolvido
 
    def __str__(self):
        status = "Devolvido" if self.devolvido else "Pendente"
        return (f"Emprestimo(cod_emprestimo='{self.cod_emprestimo}', cod_livro='{self.cod_livro}', "
                f"cod_aluno='{self.cod_aluno}', data_emprestimo={self.data_emprestimo}, "
                f"data_devolucao={self.data_devolucao}, status='{status}')")    

    def atualizar_devolucao(self, devolvido: bool):
        self.devolvido = devolvido
        
    def livro_atrasado(self):
        livro = self.livro_dict.get(self.cod_livro)
        if self.devolvido == False:
            if date.today() > self.data_devolucao:
                return f"{livro.titulo}"
            

    def livros_por_periodo(self, data_inicial, data_final):
         if self.data_emprestimo >= data_inicial and self.data_emprestimo <=data_final:
             return True
         return False
             
    def categoria_livro(self):
        livro = self.livro_dict.get(self.cod_livro)
        if livro.titulo :
            return f'{livro.titulo}, {livro.descricao_categorias()}'
    
    def aluno_emprestimo(self):
        aluno = self.aluno_dict.get(self.cod_aluno)
        if aluno.codAluno:
            return f"{aluno.nome}, {aluno.cidade_descricao()}"
        return "aluno nao encontrado"

    def to_dict(self):
        return {
            "cod_emprestimo": self.cod_emprestimo,
            "cod_livro": self.cod_livro,
            "cod_aluno": self.cod_aluno,
            "data_emprestimo": self.data_emprestimo.strftime("%d/%m/%Y"),
            "data_devolucao": self.data_devolucao.strftime("%d/%m/%Y"),
            "devolvido": self.devolvido
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
        cod_emprestimo=dados["cod_emprestimo"],
        cod_livro=dados["cod_livro"],
        cod_aluno=dados["cod_aluno"],
        data_emprestimo=datetime.strptime(dados["data_emprestimo"], "%d/%m/%Y").date(),
        data_devolucao=datetime.strptime(dados["data_devolucao"], "%d/%m/%Y").date(),
        devolvido=dados["devolvido"]
    )

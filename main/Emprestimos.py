from datetime import date, timedelta

class Emprestimo:
    livro_dict = {}
    aluno_dict = {}
    def __init__(self, cod_emprestimo: str, cod_livro: str, cod_aluno: str,
                 data_emprestimo: date, data_devolucao: date, devolvido: bool = False):
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
    
    def livro_disponivel(self):
        livro = self.livro_dict.get(self.cod_livro)
        if livro.disponibilidade is True:
             return True
        else:
            return False

    def emprestimo_livro(self):
        livro = self.livro_dict.get(self.cod_livro)
        if self.livro_disponivel() is True:
            self.data_emprestimo = date.today()
            self.data_devolucao = self.data_emprestimo + timedelta(days = 7)
            livro.disponibilidade = False
            self.devolvido = 'Não'
            return f"{self.devolvido}, emprestado"
        return "livro não disponivel para emprestimo"

    def livros_emprestados(self):
        livro = self.livro_dict.get(self.cod_livro)
        if self.livro_disponivel() is False:
            return f"{livro.titulo}"
        
    def livro_atrasado(self):
        livro = self.livro_dict.get(self.cod_livro)
        if self.devolvido == 'Não':
            if date.today() > self.data_devolucao:
                return f"{livro.titulo}"
            

    def livros_por_periodo(self, data_inicial, data_final):
         livro = self.livro_dict.get(self.cod_livro)
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
        return self.__dict__

    @staticmethod
    def from_dict(dados: dict):
        return Emprestimo(**dados)

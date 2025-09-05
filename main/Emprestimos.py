from datetime import date

class Emprestimo:
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

    def marcar_como_devolvido(self):
        self.devolvido = True

import ArvoreBinaria
class Aluno:
    def __init__(self, cod_aluno: str, nome: str, cod_curso: str, cod_cidade: str):
        self.cod_aluno = cod_aluno
        self.nome = nome
        self.cod_curso = cod_curso
        self.cod_cidade = cod_cidade

    def __str__(self):
        return (f"Aluno(cod_aluno='{self.cod_aluno}', nome='{self.nome}', "
                f"cod_curso='{self.cod_curso}', cod_cidade='{self.cod_cidade}')")

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def atualizar_curso(self, novo_cod_curso: str):
        self.cod_curso = novo_cod_curso

    def atualizar_cidade(self, novo_cod_cidade: str):
        self.cod_cidade = novo_cod_cidade

indeceAluno = ArvoreBinaria()

aluno1 = Aluno(1, "Eduardo", 1, 1)
indeceAluno.inserir(aluno1.cod_aluno, aluno1)



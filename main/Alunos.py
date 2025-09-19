<<<<<<< Updated upstream
import json
=======
from main.ArvoreBinaria import ArvoreBinaria
>>>>>>> Stashed changes
class Aluno:
    cursos_dict = {}
    cidades_dict = {}
    def __init__(self, codAluno, nome, cod_curso, cod_cidade):
        self.codAluno = codAluno
        self.nome = nome
        self.cod_curso = cod_curso
        self.cod_cidade = cod_cidade

    def __str__(self):
        return (f"Aluno codAluno:'{self.codAluno}', nome:'{self.nome}', "
                f"cod_curso:'{self.cod_curso}', cod_cidade:'{self.cod_cidade}')")

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def atualizar_curso(self, novo_cod_curso: str):
        self.cod_curso = novo_cod_curso

    def atualizar_cidade(self, novo_cod_cidade: str):
        self.cod_cidade = novo_cod_cidade
    
    def curso_descricao(self):
        return self.cursos_dict.get(self.cod_curso, "Curso não encontrado")
     
    def cidade_descricao(self):
        cidade = self.cidades_dict.get(self.cod_cidade)
        if cidade:
            return f"{cidade.descricao} - {cidade.estado}"
        return "Cidade não encontrada"
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(dados: dict):
        return Aluno(**dados)

<<<<<<< Updated upstream
=======
indeceAluno = Arvore()

aluno1 = Aluno(1, "Eduardo", 1, 1)
indeceAluno.inserir(aluno1.cod_aluno, aluno1)
indeceAluno.buscarCod()
>>>>>>> Stashed changes



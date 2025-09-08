from Alunos import Aluno
from ArvoreBinaria import Arvore
from Autores import Autor
from Categorias import Categoria
from Cidades import Cidade
from Cursos import Curso
from Emprestimos import Emprestimo
from Livros import Livro
from dados import salvar_objeto, buscar_por_posicao, carregar_todos

ARQ_ALUNOS = "alunos.txt"

indiceAluno = Arvore()

aluno3 = Aluno(3, "Carlos", 1, 1)
aluno4 = Aluno(4, "Jorge", 2, 1)

# Salvar alunos no arquivo e registrar no índice
for aluno in [aluno3, aluno4]:
    linha = salvar_objeto(aluno, ARQ_ALUNOS)  
    indiceAluno.inserir(aluno.codAluno, linha)

linha = indiceAluno.buscarCod(2)
print(buscar_por_posicao(ARQ_ALUNOS, linha, Aluno))

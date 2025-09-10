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
ARQ_AUTOR = "autores.txt"
ARQ_CATEGORIA = "categorias.txt"
ARQ_CIDADE = "cidades.txt"
ARQ_CURSO = "cursos.txt"
ARQ_EMPRESTIMO = "emprestimos.txt"
ARQ_LIVRO = "livros.txt"

indice = Arvore()
alunos_existentes = carregar_todos(ARQ_ALUNOS, Aluno)
for i, aluno in enumerate(alunos_existentes):
    indice.inserir(aluno.codAluno, i)

autores_existentes = carregar_todos(ARQ_AUTOR, Autor)
for i, autor in enumerate(autores_existentes):
    indice.inserir(autor.cod_autor, i)

autor1 = Autor(1, 'Joao', 1)
autor2 = Autor(2, 'Carlos', 2)
for autor in [autor1, autor2]:
    linha = salvar_objeto(autor, ARQ_AUTOR)  
    indice.inserir(autor.cod_autor, linha)

linha = indice.buscarCod(2)
print(buscar_por_posicao(ARQ_AUTOR, linha, Autor))

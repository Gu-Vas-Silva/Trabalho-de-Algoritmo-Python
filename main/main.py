from Alunos import Aluno
from ArvoreBinaria import Arvore
from Autores import Autor
from Categorias import Categoria
from Cidades import Cidade
from Cursos import Curso
from Emprestimos import Emprestimo
from Livros import Livro
from dados import salvar_objeto, buscar_por_posicao, carregar_todos, excluir_por_posicao
from datetime import date

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
    cursos = carregar_todos(ARQ_CURSO, Curso)
    Aluno.cursos_dict = {c.cod_curso: c.descricao for c in cursos}
    cidade = carregar_todos(ARQ_CIDADE, Cidade)
    Aluno.cidades_dict = {c.cod_cidade: c for c in cidade}
    print(aluno.nome, aluno.curso_descricao(), aluno.cidade_descricao())
    
autores_existentes = carregar_todos(ARQ_AUTOR, Autor)
for i, autor in enumerate(autores_existentes):
    indice.inserir(autor.cod_autor, i)
    cidade = carregar_todos(ARQ_CIDADE, Cidade)
    Autor.cidades_dict = {c.cod_cidade : c for c in cidade}
    print(autor.nome, autor.descricao_cidade())

categorias_existentes = carregar_todos(ARQ_CATEGORIA, Categoria)
for i, categoria in enumerate(categorias_existentes):
    indice.inserir(categoria.cod_categoria, i)

cidades_existentes = carregar_todos(ARQ_CIDADE, Cidade)
for i, cidade in enumerate(cidades_existentes):
    indice.inserir(cidade.cod_cidade, i)

cursos_existentes = carregar_todos(ARQ_CURSO, Curso)
for i, curso in enumerate(cursos_existentes):
    indice.inserir(curso.cod_curso, i)

livros_existentes = carregar_todos(ARQ_LIVRO, Livro)
for i, livro in enumerate(livros_existentes):
    indice.inserir(livro.cod_livro, i)
    autores = carregar_todos(ARQ_AUTOR, Autor)
    categorias = carregar_todos(ARQ_CATEGORIA, Categoria)
    Livro.autores_dict = {a.cod_autor: a for a in autores}
    Livro.categorias_dict = {c.cod_categoria: c.descricao for c in categorias}
    print(livro.titulo, livro.descricao_autores(), livro.descricao_categorias(), livro.emprestar())

emprestimos_existentes = carregar_todos(ARQ_EMPRESTIMO, Emprestimo)
for i, emp in enumerate(emprestimos_existentes):
    indice.inserir(emp.cod_emprestimo, i)
    livro = carregar_todos(ARQ_LIVRO, Livro)
    Emprestimo.livro_dict = {l.cod_livro: l for l in livro}
    if emp.livro_disponivel() is True :
        print ('Livro disponivel.')
        print(emp.categoria_livro())
    else:
        print('Livro Indisponivel.')


#cod_exclusao = 4
#linha = indice.buscarCod(cod_exclusao)

#excluir_por_posicao(ARQ_ALUNOS, linha)

#indice.reconstruir(ARQ_ALUNOS, Aluno, carregar_todos)

#indice.ordem()

print("joia")

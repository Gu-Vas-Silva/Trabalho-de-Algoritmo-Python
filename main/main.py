from Alunos import Aluno
from ArvoreBinaria import Arvore
from Autores import Autor
from Categorias import Categoria
from Cidades import Cidade
from Cursos import Curso
from Emprestimos import Emprestimo
from Livros import Livro
from dados import salvar_objeto, buscar_por_posicao, carregar_todos, excluir_por_posicao
from datetime import datetime

ARQ_ALUNOS = "alunos.txt"
ARQ_AUTOR = "autores.txt"
ARQ_CATEGORIA = "categorias.txt"
ARQ_CIDADE = "cidades.txt"
ARQ_CURSO = "cursos.txt"
ARQ_EMPRESTIMO = "emprestimos.txt"
ARQ_LIVRO = "livros.txt"

indice_autor = Arvore()
indice_alunos = Arvore()
indice_livros = Arvore()
indice_emprestimo = Arvore()
alunos_existentes = carregar_todos(ARQ_ALUNOS, Aluno)
autores_existentes = carregar_todos(ARQ_AUTOR, Autor)
categorias_existentes = carregar_todos(ARQ_CATEGORIA, Categoria)
cidades_existentes = carregar_todos(ARQ_CIDADE, Cidade)
cursos_existentes = carregar_todos(ARQ_CURSO, Curso)
livros_existentes = carregar_todos(ARQ_LIVRO, Livro)
emprestimos_existentes = carregar_todos(ARQ_EMPRESTIMO, Emprestimo)

for i, aluno in enumerate(alunos_existentes):
    indice_alunos.inserir(aluno.codAluno, aluno)
    Aluno.cursos_dict = {c.cod_curso: c.descricao for c in cursos_existentes}
    Aluno.cidades_dict = {c.cod_cidade: c for c in cidades_existentes}
    print(aluno.nome, aluno.curso_descricao(), aluno.cidade_descricao())
    
for i, autor in enumerate(autores_existentes):
    indice_autor.inserir(autor.cod_autor, autor)
    Autor.cidades_dict = {c.cod_cidade : c for c in cidades_existentes}
    print(autor.nome, autor.descricao_cidade())

contlivrod = 0
contlivroe = 0
for i, livro in enumerate(livros_existentes):
    indice_livros.inserir(livro.cod_livro, livro)
    Livro.autores_dict = {a.cod_autor: a for a in autores_existentes}
    Livro.categorias_dict = {c.cod_categoria: c.descricao for c in categorias_existentes}
    print(livro.titulo, livro.descricao_autores(), livro.descricao_categorias(), livro.emprestar())
    if livro.disponibilidade is True:
        contlivrod += 1
    else:
        contlivroe += 1
indice_livros.ordem()
print(f"Quantidade de livros disponiveis: {contlivrod}")
print(f"Quantidade de livros emprestados: {contlivroe}")


cont = 0
data_i = datetime.strptime("09/09/2025", "%d/%m/%Y").date()
data_f = datetime.strptime("12/09/2025", "%d/%m/%Y").date()
for i, emp in enumerate(emprestimos_existentes):
    indice_emprestimo.inserir(emp.cod_emprestimo, emp)
    livro = carregar_todos(ARQ_LIVRO, Livro)
    aluno = carregar_todos(ARQ_ALUNOS, Aluno)
    Emprestimo.livro_dict = {l.cod_livro: l for l in livro}
    Emprestimo.aluno_dict = {a.codAluno: a for a in aluno}
    if emp.livro_disponivel() is True :
        print ('Livro disponivel.')
        print(emp.categoria_livro())
    else:
        print('Livro indisponivel.')
    print (emp.aluno_emprestimo())
    print (emp.emprestimo_livro())
    print (emp.livros_emprestados())
    print (emp.livro_atrasado())
    if emp.livros_por_periodo(data_i, data_f):
        cont+=1
    print(f"quantidade dentro do periodo: {cont}")

#cod_exclusao = 1
#linha = indice.buscarCod(cod_exclusao)

#excluir_por_posicao(ARQ_EMPRESTIMO, linha)

#indice.reconstruir(ARQ_EMPRESTIMO, Emprestimo, carregar_todos)

#indice.ordem()

print("joia")

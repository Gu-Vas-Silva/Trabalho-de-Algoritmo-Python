from Alunos import Aluno
from ArvoreBinaria import Arvore
from Autores import Autor
from Categorias import Categoria
from Cidades import Cidade
from Cursos import Curso
from Emprestimos import Emprestimo
from Livros import Livro
from dados import salvar_objeto, carregar_todos, excluir_do_arquivo
from datetime import datetime, date, timedelta
import time

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
indice_categoria = Arvore()
indice_cidade = Arvore()
indice_emprestimo = Arvore()
indice_curso = Arvore()

def carregar_arquivos(arquivo):
    if arquivo == ARQ_ALUNOS:
        alunos_existentes = carregar_todos(ARQ_ALUNOS, Aluno)
        for aluno in alunos_existentes:
            indice_alunos.inserir(aluno.codAluno, aluno)
        return alunos_existentes
    elif arquivo == ARQ_AUTOR:
        autores_existentes = carregar_todos(ARQ_AUTOR, Autor)
        for autor in autores_existentes:
            indice_autor.inserir(autor.cod_autor, autor)
        return autores_existentes
    elif arquivo == ARQ_CATEGORIA:
        categorias_existentes = carregar_todos(ARQ_CATEGORIA, Categoria)
        for categoria in categorias_existentes:
            indice_categoria.inserir(categoria.cod_categoria, categoria)
        return categorias_existentes
    elif arquivo == ARQ_CIDADE:
        cidades_existentes = carregar_todos(ARQ_CIDADE, Cidade)
        for cidade in cidades_existentes:
            indice_cidade.inserir(cidade.cod_cidade, cidade)
        return cidades_existentes
    elif arquivo == ARQ_EMPRESTIMO:
        emprestimos_existentes = carregar_todos(ARQ_EMPRESTIMO, Emprestimo)
        for emprestimo in emprestimos_existentes:
            indice_emprestimo.inserir(emprestimo.cod_emprestimo, emprestimo)
        return emprestimos_existentes
    elif arquivo == ARQ_CURSO:
        cursos_existentes = carregar_todos(ARQ_CURSO, Curso)
        for curso in cursos_existentes:
            indice_curso.inserir(curso.cod_curso, curso)
        return cursos_existentes
    elif arquivo == ARQ_LIVRO:
        livros_existentes = carregar_todos(ARQ_LIVRO, Livro)
        for livro in livros_existentes:
            indice_livros.inserir(livro.cod_livro, livro)
        return livros_existentes
    else: 
        return "arquivo não encontrado"

def inserir_aluno():
    carregar_arquivos(ARQ_ALUNOS)
    carregar_arquivos(ARQ_CURSO)
    carregar_arquivos(ARQ_CIDADE)
    nome = input("Nome do aluno: ")
    codAluno = int(input("Código do aluno: "))
    if indice_alunos.buscarCod(codAluno):
        print("Código do aluno já existe. Tente novamente.")
        return
    cod_curso = int(input("Código do curso: "))
    if not indice_curso.buscarCod(cod_curso):
        print("Código do curso não encontrado. Tente novamente.")
        return
    cod_cidade = int(input("Código da cidade: "))
    if not indice_cidade.buscarCod(cod_cidade):
        print("Código da cidade não encontrado. Tente novamente.")
        return
    novo_aluno = Aluno(codAluno, nome, cod_curso, cod_cidade)
    salvar_objeto(novo_aluno, ARQ_ALUNOS)
    indice_alunos.inserir(novo_aluno.codAluno, novo_aluno)
    print("Aluno inserido com sucesso!")

def inserir_autor():
    carregar_arquivos(ARQ_AUTOR)
    carregar_arquivos(ARQ_CIDADE)
    nome = input("Nome do autor: ")
    cod_autor = int(input("Código do autor: "))
    if not indice_autor.buscarCod(cod_autor):
        print("Código do autor já existe. Tente novamente.")
        return
    cod_cidade = int(input("Código da cidade: "))
    if not indice_cidade.buscarCod(cod_cidade):
        print("Código da cidade não encontrado. Tente novamente.")
        return
    novo_autor = Autor(cod_autor, nome, cod_cidade)
    salvar_objeto(novo_autor, ARQ_AUTOR)
    indice_autor.inserir(novo_autor.cod_autor, novo_autor)
    print("Autor inserido com sucesso!")

def inserir_categoria():
    carregar_arquivos(ARQ_CATEGORIA)
    descricao = input("Descrição da categoria: ")
    cod_categoria = int(input("Código da categoria: "))
    if not indice_categoria.buscarCod(cod_categoria):
        print("Código da categoria já existe. Tente novamente.")
        return
    nova_categoria = Categoria(cod_categoria, descricao)
    salvar_objeto(nova_categoria, ARQ_CATEGORIA)
    indice_categoria.inserir(nova_categoria.cod_categoria, nova_categoria)
    print("Categoria inserida com sucesso!")

def inserir_cidade():
    carregar_arquivos(ARQ_CIDADE)
    nome = input("Nome da cidade: ")
    estado = int(input("Estado da cidade: "))
    cod_cidade = int(input("Código da cidade: "))
    if not indice_cidade.buscarCod(cod_cidade):
        print("Código da cidade já existe. Tente novamente.")
        return
    nova_cidade = Cidade(cod_cidade, nome, estado)
    salvar_objeto(nova_cidade, ARQ_CIDADE)
    indice_cidade.inserir(nova_cidade.cod_cidade, nova_cidade)
    print("Cidade inserida com sucesso!")

def inserir_curso():
    carregar_arquivos(ARQ_CURSO)
    descricao = input("Descrição do curso: ")
    cod_curso = int(input("Código do curso: "))
    if not indice_curso.buscarCod(cod_curso):
        print("Código do curso já existe. Tente novamente.")
        return
    novo_curso = Curso(cod_curso, descricao)
    salvar_objeto(novo_curso, ARQ_CURSO)
    indice_curso.inserir(novo_curso.cod_curso, novo_curso)
    print("Curso inserido com sucesso!")

def inserir_livro():
    carregar_arquivos(ARQ_AUTOR)
    carregar_arquivos(ARQ_CATEGORIA)
    carregar_arquivos(ARQ_LIVRO)
    titulo = input("Título do livro: ")
    cod_livro = int(input("Código do livro: "))
    if indice_livros.buscarCod(cod_livro):
        print("Código do livro já existe. Tente novamente.")
        return
    cod_autor = int(input("Código do autor: "))
    if not indice_autor.buscarCod(cod_autor):
        print("Código do autor não encontrado. Tente novamente.")
        return
    cod_categoria = int(input("Código da categoria: "))
    if not indice_categoria.buscarCod(cod_categoria):
        print("Código da categoria não encontrado. Tente novamente.")
        return
    ano_publicacao = int(input("Ano de publicação: "))
    novo_livro = Livro(cod_livro, titulo, cod_autor, cod_categoria, ano_publicacao)
    salvar_objeto(novo_livro, ARQ_LIVRO)
    indice_livros.inserir(novo_livro.cod_livro, novo_livro)
    Livro.autores_dict = {a.cod_autor: a for a in carregar_arquivos(ARQ_AUTOR)}
    Livro.categorias_dict = {c.cod_categoria: c for c in carregar_arquivos(ARQ_CATEGORIA)}
    Autor.cidades_dict = {c.cod_cidade: c for c in carregar_arquivos(ARQ_CIDADE)}   
    print("autor: ", novo_livro.descricao_autores())
    print("categoria: ", novo_livro.descricao_categorias())
    print("Livro inserido com sucesso!")

def inserir_emprestimo():
    carregar_arquivos(ARQ_EMPRESTIMO)
    carregar_arquivos(ARQ_LIVRO)
    carregar_arquivos(ARQ_ALUNOS)
    cod_emprestimo = int(input("Código do empréstimo: "))
    if indice_emprestimo.buscarCod(cod_emprestimo):
        print("Código do empréstimo já existe. Tente novamente.")
        return
    cod_livro = int(input("Código do livro: "))
    if not indice_livros.buscarCod(cod_livro):
        print("Código do livro não encontrado. Tente novamente.")
        return
    else:
        livro = indice_livros.buscarCod(cod_livro)
        if livro.disponibilidade is False:
            print("Livro indisponível para empréstimo. Tente outro livro.")
            return
        else:
            codAluno = int(input("Código do aluno: "))
            if not indice_alunos.buscarCod(codAluno):
                print("Código do aluno não encontrado. Tente novamente.")
                return       
            data_emprestimo = date.today()
            data_devolucao = data_emprestimo + timedelta(days=7)
            novo_emprestimo = Emprestimo(cod_emprestimo, cod_livro, codAluno, data_emprestimo, data_devolucao)
            salvar_objeto(novo_emprestimo, ARQ_EMPRESTIMO)
            Emprestimo.livro_dict = {l.cod_livro: l for l in carregar_arquivos(ARQ_LIVRO)}
            Emprestimo.aluno_dict = {a.codAluno: a for a in carregar_arquivos(ARQ_ALUNOS)}
            Aluno.cidades_dict = {c.cod_cidade: c for c in carregar_arquivos(ARQ_CIDADE)}
            print("aluno: ", novo_emprestimo.aluno_emprestimo())
            print("categoria: ", novo_emprestimo.categoria_livro())
            indice_emprestimo.inserir(novo_emprestimo.cod_emprestimo, novo_emprestimo)
            print("Empréstimo inserido com sucesso!")
            livro.atualizar_disponibilidade(False)

def consultar_aluno():
    carregar_arquivos(ARQ_ALUNOS)
    curso = carregar_arquivos(ARQ_CURSO)
    cidade = carregar_arquivos(ARQ_CIDADE)
    codAluno = int(input("Código do aluno a consultar: "))
    aluno = indice_alunos.buscarCod(codAluno)
    if aluno:
        Aluno.cursos_dict = {c.cod_curso: c.descricao for c in curso}
        Aluno.cidades_dict = {c.cod_cidade: c for c in cidade}
        print(aluno.nome, aluno.curso_descricao(), aluno.cidade_descricao())
    else:
        print("Aluno não encontrado.")
        print("Alunos disponíveis:")
        indice_alunos.ordem()

def consultar_autor():
    carregar_arquivos(ARQ_AUTOR)
    cidade = carregar_arquivos(ARQ_CIDADE)
    cod_autor = int(input("Código do autor a consultar: "))
    autor = indice_autor.buscarCod(cod_autor)
    if autor:
        Autor.cidades_dict = {c.cod_cidade : c for c in cidade}
        print(f"{autor.nome}, {autor.descricao_cidade()}")
    else:
        print("Autor não encontrado.")
        print("Autores disponíveis:")
        indice_autor.ordem()

def consultar_livro():
    carregar_arquivos(ARQ_LIVRO)
    cod_livro = int(input("Código do livro a consultar: "))
    autor = carregar_arquivos(ARQ_AUTOR)
    categoria = carregar_arquivos(ARQ_CATEGORIA)
    livro = indice_livros.buscarCod(cod_livro)
    if livro:
            Livro.autores_dict = {a.cod_autor: a for a in autor}
            Livro.categorias_dict = {c.cod_categoria: c.descricao for c in categoria}
            print(livro.titulo, livro.descricao_autores(), livro.descricao_categorias(), livro.disponibilidade)
    else:
        print("Livro não encontrado.")
        print("Livros disponíveis:")
        indice_livros.ordem()

def consultar_emprestimo():
    carregar_arquivos(ARQ_EMPRESTIMO)
    cod_emprestimo = int(input("Código do empréstimo a consultar: "))
    emprestimo = indice_emprestimo.buscarCod(cod_emprestimo)
    if emprestimo:
        livro = carregar_arquivos(ARQ_LIVRO)
        aluno = carregar_arquivos(ARQ_ALUNOS)
        Emprestimo.livro_dict = {l.cod_livro: l for l in livro}
        Emprestimo.aluno_dict = {a.codAluno: a for a in aluno}
        print(emprestimo)
        print(emprestimo.categoria_livro())
        print(emprestimo.aluno_emprestimo())
    else:
        print("Empréstimo não encontrado.")
        print("Empréstimos disponíveis:")
        indice_emprestimo.ordem()

def consultar_categoria():
    carregar_arquivos(ARQ_CATEGORIA)
    cod_categoria = int(input("Código da categoria a consultar: "))
    categoria = indice_categoria.buscarCod(cod_categoria)
    if categoria:
        print(categoria)
    else:
        print("Categoria não encontrada.")
        print("Categorias disponíveis:")
        indice_categoria.ordem()

def consultar_cidade():
    carregar_arquivos(ARQ_CIDADE)
    cod_cidade = int(input("Código da cidade a consultar: "))
    cidade = indice_cidade.buscarCod(cod_cidade)
    if cidade:
        print(cidade)
    else:
        print("Cidade não encontrada.")
        print("Cidades disponíveis:")
        indice_cidade.ordem()

def consultar_curso():
    carregar_arquivos(ARQ_CURSO)
    cod_curso = int(input("Código do curso a consultar: "))
    curso = indice_curso.buscarCod(cod_curso)
    if curso:
        print(curso)
    else:
        print("Curso não encontrado.")
        print("Cursos disponíveis:")
        indice_curso.ordem()

def excluir_aluno():
    carregar_arquivos(ARQ_ALUNOS)
    codAluno = int(input("Código do aluno a excluir: "))
    aluno = indice_alunos.buscarCod(codAluno)
    if aluno:
        indice_alunos.excluir(codAluno)
        excluir_do_arquivo(ARQ_ALUNOS, codAluno, Aluno)
        indice_alunos.reconstruir(ARQ_ALUNOS, Aluno, carregar_todos)
        print("Aluno excluído com sucesso.")
    else:
        print("Aluno não encontrado.")

def excluir_autor():
    carregar_arquivos(ARQ_AUTOR)
    cod_autor = int(input("Código do autor a excluir: "))
    autor = indice_autor.buscarCod(cod_autor)
    if autor:
        indice_autor.excluir(cod_autor)
        excluir_do_arquivo(ARQ_AUTOR, cod_autor, Autor)
        indice_alunos.reconstruir(ARQ_AUTOR, Autor, carregar_todos)
        print("Autor excluído com sucesso.")
    else:
        print("Autor não encontrado.")

def excluir_livro():
    carregar_arquivos(ARQ_LIVRO)
    cod_livro = int(input("Código do livro a excluir: "))
    livro = indice_livros.buscarCod(cod_livro)
    if livro:
        indice_livros.excluir(cod_livro)
        excluir_do_arquivo(ARQ_LIVRO, cod_livro, Livro)
        indice_livros.reconstruir(ARQ_LIVRO, Livro, carregar_todos)
        print("Livro excluído com sucesso.")
    else:
        print("Livro não encontrado.")

def excluir_emprestimo():
    carregar_arquivos(ARQ_EMPRESTIMO)
    cod_emprestimo = int(input("Código do empréstimo a excluir: "))
    emprestimo = indice_emprestimo.buscarCod(cod_emprestimo)
    if emprestimo:
        indice_emprestimo.excluir(cod_emprestimo)
        excluir_do_arquivo(ARQ_EMPRESTIMO, cod_emprestimo, Emprestimo)
        indice_emprestimo.reconstruir(ARQ_EMPRESTIMO, Emprestimo, carregar_todos)
        print("Empréstimo excluído com sucesso.")
    else:
        print("Empréstimo não encontrado.")

def excluir_categoria():
    carregar_arquivos(ARQ_CATEGORIA)
    cod_categoria = int(input("Código da categoria a excluir: "))
    categoria = indice_categoria.buscarCod(cod_categoria)
    if categoria:
        indice_categoria.excluir(cod_categoria)
        excluir_do_arquivo(ARQ_CATEGORIA, cod_categoria, Categoria)
        indice_categoria.reconstruir(ARQ_CATEGORIA, Categoria, carregar_todos)
        print("Categoria excluída com sucesso.")
    else:
        print("Categoria não encontrada.")

def excluir_cidade():
    carregar_arquivos(ARQ_CIDADE)
    cod_cidade = int(input("Código da cidade a excluir: "))
    cidade = indice_cidade.buscarCod(cod_cidade)
    if cidade:
        indice_cidade.excluir(cod_cidade)
        excluir_do_arquivo(ARQ_CIDADE, cod_cidade, Cidade)
        indice_cidade.reconstruir(ARQ_CIDADE, Cidade, carregar_todos)
        print("Cidade excluída com sucesso.")
    else:
        print("Cidade não encontrada.")

def excluir_curso():
    carregar_arquivos(ARQ_CURSO)
    cod_curso = int(input("Código do curso a excluir: "))
    curso = indice_curso.buscarCod(cod_curso)
    if curso:
        indice_curso.excluir(cod_curso)
        excluir_do_arquivo(ARQ_CURSO, cod_curso, Curso)
        indice_curso.reconstruir(ARQ_CURSO, Curso, carregar_todos)
        print("Curso excluído com sucesso.")
    else:
        print("Curso não encontrado.")

def devolver_livro():
    carregar_arquivos(ARQ_EMPRESTIMO)
    carregar_arquivos(ARQ_LIVRO)
    cod_emprestimo = int(input("Código do empréstimo para devolução: "))
    emprestimo = indice_emprestimo.buscarCod(cod_emprestimo)
    if emprestimo:
        livro = indice_livros.buscarCod(emprestimo.cod_livro)
        if livro:
            livro.atualizar_disponibilidade(True)
            emprestimo.atualizar_devolucao(True)
            print(f"Livro '{livro.titulo}' devolvido com sucesso.")
        else:
            print("Livro associado ao empréstimo não encontrado.")
    else:
        print("Empréstimo não encontrado.")

def consultar_livros_atrasados():
    print("Livros atrasados:")
    cont = 0
    emprestimos_existentes = carregar_arquivos(ARQ_EMPRESTIMO)
    livro = carregar_arquivos(ARQ_LIVRO)
    for emprestimo in emprestimos_existentes:
        emprestimo.livro_dict = {l.cod_livro: l for l in livro}
        livro_atrasado = emprestimo.livro_atrasado()
        if livro_atrasado:
            print(f"- {livro_atrasado}")
            cont += 1
    if cont == 0:
        print("Nenhum livro atrasado.")
            

def consultar_livros_emprestados():
    print("Livros emprestados:")
    cont = 0
    emprestimos_existentes = carregar_arquivos(ARQ_EMPRESTIMO)
    livro = carregar_arquivos(ARQ_LIVRO)
    for emprestimo in emprestimos_existentes:
        emprestimo.livro_dict = {l.cod_livro: l for l in livro}
        if not emprestimo.devolvido:
            livro = indice_livros.buscarCod(emprestimo.cod_livro)
            if livro:
                print(f"- {livro.titulo}")
                cont += 1
    if cont == 0:
        print("Nenhum livro emprestado.")

def quantidade_emprestimos_periodo():
    emprestimos_existentes = carregar_arquivos(ARQ_EMPRESTIMO)
    data_inicial_str = input("Data inicial (dd/mm/aaaa): ")
    data_final_str = input("Data final (dd/mm/aaaa): ")
    try:
        data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y").date()
        data_final = datetime.strptime(data_final_str, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")
        return
    if data_inicial > data_final:
        print("Data inicial não pode ser maior que a data final.")
        return
    cont = 0
    for emprestimo in emprestimos_existentes:
        if emprestimo.livros_por_periodo(data_inicial, data_final):
            cont += 1
    print(f"Quantidade de empréstimos no período: {cont}")

def mostrar_livros_ordem():
    print("Livros disponíveis:")
    indice = Arvore()
    livros_existentes = carregar_arquivos(ARQ_LIVRO)
    autores_existentes = carregar_arquivos(ARQ_AUTOR)
    categorias_existentes = carregar_arquivos(ARQ_CATEGORIA)
    cont_emp = 0
    cont_disp = 0
    for livro in livros_existentes:
        livro.autores_dict = {a.cod_autor: a for a in autores_existentes}
        livro.categorias_dict = {c.cod_categoria: c for c in categorias_existentes}
        livros_ordem = livro.mostrar_livros()
        indice.inserir(livros_ordem, livros_ordem)
        indice.ordem()
        if livro.disponibilidade:
            cont_disp += 1
        else:
            cont_emp += 1
    print(f"Total de livros disponíveis: {cont_disp}")
    print(f"Total de livros emprestados: {cont_emp}")

def menu():
    while True:
        print("\nMenu Principal")
        print("==============")
        time.sleep(0.5)
        print("1. Inserir algum objeto")
        print("2. Consultar algum objeto por código")
        print("3. Excluir algum objeto por código")
        print("4. Devolver livro")
        print("5. Consultar livros atrasados")
        print("6. Consultar quantidade de livros emprestados por periodo")
        print("7. Consultar livros em ordem de código")
        print("8. Sair")

        escolha = input("Escolha uma opção: ")
        time.sleep(1)
        if escolha == '1':
            while True:
                print("\n--- Inserir ---")
                print("1. Inserir Aluno")  
                print("2. Inserir Autor")
                print("3. Inserir Categoria")
                print("4. Inserir Cidade")
                print("5. Inserir Curso")
                print("6. Inserir Livro")
                print("7. Inserir Empréstimo")
                print("8. Voltar ao Menu Principal")
                escolha2 = input("Escolha uma opção: ")

                if escolha2 == '1': inserir_aluno()
                elif escolha2 == '2': inserir_autor()
                elif escolha2 == '3': inserir_categoria()
                elif escolha2 == '4': inserir_cidade()
                elif escolha2 == '5': inserir_curso()
                elif escolha2 == '6': inserir_livro()
                elif escolha2 == '7': inserir_emprestimo()
                elif escolha2 == '8': break
                else: print("Opção inválida.")

        elif escolha == '2':
            while True:
                print("\n--- Consultar ---")
                print("1. Consultar Aluno por código")
                print("2. Consultar Autor por código")
                print("3. Consultar Categoria por código")
                print("4. Consultar Cidade por código")
                print("5. Consultar Curso por código")
                print("6. Consultar Livro por código")
                print("7. Consultar Empréstimo")
                print("8. Voltar ao Menu Principal")
                escolha3 = input("Escolha uma opção: ")

                if escolha3 == '1': consultar_aluno()
                elif escolha3 == '2': consultar_autor()
                elif escolha3 == '3': consultar_categoria()
                elif escolha3 == '4': consultar_cidade()
                elif escolha3 == '5': consultar_curso()
                elif escolha3 == '6': consultar_livro()
                elif escolha3 == '7': consultar_emprestimo()
                elif escolha3 == '8': break
                else: print("Opção inválida.")

        elif escolha == '3':
            while True:
                print("\n--- Excluir ---")
                print("1. Excluir Aluno")
                print("2. Excluir Autor")
                print("3. Excluir Categoria")
                print("4. Excluir Cidade")
                print("5. Excluir Curso")
                print("6. Excluir Livro")
                print("7. Excluir Empréstimo")
                print("8. Voltar ao Menu Principal")
                escolha4 = input("Escolha uma opção: ")

                if escolha4 == '1': excluir_aluno()
                elif escolha4 == '2': excluir_autor()
                elif escolha4 == '3': excluir_categoria()
                elif escolha4 == '4': excluir_cidade()
                elif escolha4 == '5': excluir_curso()
                elif escolha4 == '6': excluir_livro()
                elif escolha4 == '7': excluir_emprestimo()
                elif escolha4 == '8': break
                else: print("Opção inválida.")
        elif escolha == '4':
            devolver_livro()
        elif escolha == '5':
            consultar_livros_atrasados()
        elif escolha == '6':
            quantidade_emprestimos_periodo()
        elif escolha == '7':
            mostrar_livros_ordem()
        elif escolha == '8':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida.")
menu()

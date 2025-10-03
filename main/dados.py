import json
import os

def salvar_objeto(objeto, arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            linha_num = sum(1 for _ in f)
    else:
        linha_num = 0
    with open(arquivo, "a", encoding="utf-8") as f:
        linha = json.dumps(objeto.to_dict(), ensure_ascii=False)  
        f.write(linha + "\n")

    return linha_num

def carregar_todos(arquivo, classe):
    objetos = []
    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            pass
        return objetos

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            objetos.append(classe.from_dict(json.loads(linha)))
    return objetos

def excluir_do_arquivo(arquivo, valor_chave, classe):
    objetos = carregar_todos(arquivo, classe)
    chave_map = {
        "Aluno": "codAluno",
        "Autor": "cod_autor",
        "Categoria": "cod_categoria",
        "Cidade": "cod_cidade",
        "Curso": "cod_curso",
        "Livro": "cod_livro",
        "Emprestimo": "cod_emprestimo"
    }
    atributo_chave = chave_map[classe.__name__]
    objetos_filtrados = [obj for obj in objetos if getattr(obj, atributo_chave) != valor_chave]
    with open(arquivo, "w", encoding="utf-8") as f:
        for obj in objetos_filtrados:
            linha = json.dumps(obj.to_dict(), ensure_ascii=False)
            f.write(linha + "\n")

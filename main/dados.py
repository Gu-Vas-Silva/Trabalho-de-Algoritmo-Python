import json
import os

def salvar_objeto(objeto, arquivo):
    """Salva um objeto no arquivo e retorna a linha onde foi salvo"""
    # Conta quantas linhas já existem antes de salvar
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            linha_num = sum(1 for _ in f)
    else:
        linha_num = 0

    with open(arquivo, "a", encoding="utf-8") as f:
        linha = json.dumps(objeto.to_dict(), ensure_ascii=False)  # <<< acentos legíveis
        f.write(linha + "\n")

    return linha_num

def buscar_por_posicao(arquivo, linha_num, classe):
    """Busca objeto pela linha (posição no índice)"""
    with open(arquivo, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f):
            if i == linha_num:
                return classe.from_dict(json.loads(linha.strip()))
    return None

def carregar_todos(arquivo, classe):
    """Carrega todos os objetos de um arquivo"""
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

def excluir_por_posicao(arquivo, linha_num):
    """Exclui fisicamente uma linha do arquivo (remove o objeto)"""
    if not os.path.exists(arquivo):
        return False

    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    if linha_num < 0 or linha_num >= len(linhas):
        return False  # posição inválida

    # remove a linha desejada
    del linhas[linha_num]

    # reescreve o arquivo sem ela
    with open(arquivo, "w", encoding="utf-8") as f:
        f.writelines(linhas)

    return True
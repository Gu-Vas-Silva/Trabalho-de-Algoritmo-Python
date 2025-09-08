import json

def salvar_objeto(objeto, arquivo):
    """Salva um objeto no arquivo e retorna a linha onde foi salvo"""
    with open(arquivo, "a", encoding="utf-8") as f:
        linha = json.dumps(objeto.to_dict())
        f.write(linha + "\n")

    # número da linha = total de linhas no arquivo - 1
    with open(arquivo, "r", encoding="utf-8") as f:
        return sum(1 for _ in f) - 1

def buscar_por_posicao(arquivo, linha_num, classe):
    """Busca objeto pela linha (posição no índice)"""
    with open(arquivo, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f):
            if i == linha_num:
                return classe.from_dict(json.loads(linha.strip()))
    return None

def carregar_todos(arquivo, classe):
    objetos = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            objetos.append(classe.from_dict(json.loads(linha.strip())))
    return objetos
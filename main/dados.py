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

def buscar_por_posicao(arquivo, linha_num, classe):
    with open(arquivo, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f):
            if i == linha_num:
                return classe.from_dict(json.loads(linha.strip()))
    return None

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

def excluir_por_posicao(arquivo, linha_num):
    if not os.path.exists(arquivo):
        return False
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    if linha_num < 0 or linha_num >= len(linhas):
        return False  
    del linhas[linha_num]
    with open(arquivo, "w", encoding="utf-8") as f:
        f.writelines(linhas)

    return True
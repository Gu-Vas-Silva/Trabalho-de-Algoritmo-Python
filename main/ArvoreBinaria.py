class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, chave, valor):
        if self.raiz is None:
            self.raiz = Node(chave, valor)
        else:
            self._inserirRecursivo(self.raiz, chave, valor)

    def _inserirRecursivo(self, noAtual, chave, valor):
        if chave < noAtual.chave:
            if noAtual.esquerda is None:
                noAtual.esquerda = Node(chave, valor)
            else:
                self._inserirRecursivo(noAtual.esquerda, chave, valor)
        else:
            if noAtual.direita is None:
                noAtual.direita = Node(chave, valor)
            else:
                self._inserirRecursivo(noAtual.direita, chave, valor)
    
    def ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            if no.esquerda:
                self.ordem(no.esquerda)
                print(no.valor)
            if no.direita:
                self.ordem(no.direita)

    def buscarCod(self, chave, no=None):
        if no is None:
            no = self.raiz
        if no is None:
            return None
        if chave == no.chave:
            return no.valor
        elif chave < no.chave:
            return self.buscarCod(chave, no.esquerda)
        else:
            return self.buscarCod(chave, no.direita)
    
    def reconstruir(self, arquivo, classe, carregar_todos_func):
        self.raiz = None 
        objetos = carregar_todos_func(arquivo, classe)
        chave_map = {
            "Aluno": "codAluno",
            "Autor": "cod_autor",
            "Categoria": "cod_categoria",
            "Cidade": "cod_cidade",
            "Curso": "cod_curso",
            "Livro": "cod_livro",
            "Emprestimo": "cod_emprestimo"
        }
        nome_classe = classe.__name__
        if nome_classe not in chave_map:
            raise ValueError(f"Classe {nome_classe} não tem chave mapeada")

        atributo_chave = chave_map[nome_classe]

        for i, obj in enumerate(objetos):
            chave = getattr(obj, atributo_chave)
            self.inserir(chave, i)
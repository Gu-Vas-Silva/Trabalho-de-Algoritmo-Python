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
        if self.raiz == None:
            self.raiz = Node(valor)
        else:
            self.inserirRecursivo(self.raiz, chave, valor)

    def inserirRecursivo(self, noAtual, chave, valor):
        if chave < noAtual.chave:
            if noAtual.esquerda is None:
                noAtual.esquerda = Node(valor)
            else:
                self.inserirRecursivo(noAtual.esquerda, chave, valor)
        else:
            if noAtual.direita is None:
                noAtual.direita = Node(valor)
            else:
                self.inserirRecursivo(noAtual.direita, chave, valor)
    
    def ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            if no.esquerda:
                self.ordem(no.esquerda)
            if no.valor.status == 0:
                print(no.valor)
            if no.direita:
                self.ordem(no.direita)
    def acharNo(self, no, chave):
        return self.buscarCod(no, chave, self.raiz)

    def buscarCod(self, chave, no):
        if no == None:
            return None
        if chave == no.chave:
            return no.valor
        elif chave < no.chave:
            return self.buscarCod(chave, no.esquerda)
        else:
            return self.buscarCod(chave, no.direita)
    
    def excluir(self, exclusao):
        exclusao.status = 1
        return exclusao
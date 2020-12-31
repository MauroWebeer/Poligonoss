class Poligono:
    def __init__(self, nome):
        self.nome = nome #iterador de nomes


class Pentagono(Poligono):
    def __init__(self, nome, quantidade_arestas, valor_arestas):
        super().__init__(nome, quantidade_arestas)
        self.valor_arestas = valor_arestas

class Hexagono(Poligono):
    def __init__(self, nome, quantidade_arestas, valor_arestas):
        super().__init__(nome, quantidade_arestas)
        self.valor_arestas = valor_arestas
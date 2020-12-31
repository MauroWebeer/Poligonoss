from Poligono import Poligono

class Regular(Poligono):
    def __init__(self, nome, quant_arestas, aresta_1, apotema):
        super().__init__(nome)
        self.quant_arestas = quant_arestas
        self.aresta_1 = aresta_1
        self.apotema = apotema
        self.area = 0

    def calculando_area_regular(self):
        area = (float(self.quant_arestas)*float(self.apotema))/2
        self.area = float(area)

    def __str__(self):
        return f"O Polígono {self.nome} é um polígono regular de {self.quant_arestas} lados de área {self.area}."
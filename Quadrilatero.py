from Poligono import Poligono

class Quadrilatero(Poligono):
    def __init__(self, nome, aresta_1, aresta_2, aresta_3, tipo):
        super().__init__(nome)
        self.aresta_1 = aresta_1
        self.aresta_2 = aresta_2
        self.aresta_3 = aresta_3
        self.tipo = tipo
        self.area = 0

    def calculando_area_trapezio(self):
        area = ((float(self.aresta_1) + float(self.aresta_2)) * float(self.aresta_3))/2
        self.area = float(area)

    def calulando_area_retangulo(self):
        area = float(self.aresta_1) * float(self.aresta_2)
        self.area = float(area)

    def calculando_area_quadrado(self):
        area = float(self.aresta_1) ** 2
        self.area = float(area)

    def __str__(self):
        return f"O Polígono {self.nome} é um Quadrilátero do tipo {self.tipo} de área {self.area}."
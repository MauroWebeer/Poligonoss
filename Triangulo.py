from Poligono import Poligono
import collections

class Triangulo(Poligono):
    def __init__(self, nome, aresta_1, aresta_2, aresta_3):
        super().__init__(nome)
        self.aresta_1 = aresta_1
        self.aresta_2 = aresta_2
        self.aresta_3 = aresta_3
        self.tipo = 'vazio'
        self.area = 0

    def verificar_tipo_triangulo(self):
        #### DESCOBRIR TIPO USANDO ARESTAS####
        if float(self.aresta_1) == float(self.aresta_2) and float(self.aresta_1) == float(self.aresta_3):
            self.tipo = 'Equilátero'
        elif float(self.aresta_1) != float(self.aresta_2) and float(self.aresta_1) != float(self.aresta_3):
            self.tipo = 'Escaleno'
        else:
            self.tipo = 'Isósceles'


    def calculando_area_triangulo(self):
        p = float((self.aresta_1 + self.aresta_2 + self.aresta_3) / 2)
        area = float((p * (p - self.aresta_1) * (p - self.aresta_2) * (p - self.aresta_3)) ** (1/2))
        self.area = area

    def __str__(self):
        return f"O Polígono {self.nome} é um triângulo {self.tipo} de área {self.area}."

    @staticmethod
    def verificando_existencia_triangulo(lista):
        condicao_existencia = 0
        lista = [int(val) for val in lista]
        if lista[0]+lista[1] > lista[2]:
            condicao_existencia += 1
        if lista[1] + lista[2] > lista[0]:
            condicao_existencia += 1
        if lista[2] + lista[0] > lista[1]:
            condicao_existencia += 1
        if condicao_existencia == 3:
            return True
        else:
            return False
from Poligono import Poligono
from Triangulo import Triangulo
from Quadrilatero import Quadrilatero
from Regular import Regular

#----------------------start-main-function------------------------#
def main():
    count = 0
    print("Bem Vindo!!!")
    while True:
        ### ESCOLHA DA QUANTIDADE DE ARESTAS ###
        escolha = input(f'Quantas arestas tem seu polígono?')
        while True:
            if verificando_numeros_de_arestas(escolha) == True:
                break
            else:
                escolha = input(f'''Desculpa, nossas opções são apenas valores interios maiores que 2.
    Digite novamente a quantiade de arestas:''')

        ### OPÇÕES DE POLIGONOS ###

        ### TRIANGULO ###
        if str(escolha) == str(3):
            count = count + 1
            nome = f'P{count}'
            valor_arestas = [input(f'Insira o valor da {i + 1}ª aresta') for i in range(3)]

            ### DESIGUALDADE TRIANGULAR PARA EXISTENCIA DE TRIANGULOS ###
            while not Triangulo.verificando_existencia_triangulo(valor_arestas):
                print("Não existe triângulo com estas medidas de arestas")
                valor_arestas = [input(f'Insira o valor da {i + 1}ª aresta') for i in range(3)]

            ### CRIANDO OBJETO - TRIANGULO ###
            poligono_1 = Triangulo(nome, float(valor_arestas[0]), float(valor_arestas[1]), float(valor_arestas[2]))
            poligono_1.calculando_area_triangulo()
            poligono_1.verificar_tipo_triangulo()
            print(poligono_1)

        ### QUADRILATEROS ###
        if str(escolha) == str(4):
            count += 1
            nome = f'P{count}'
            tipo_quadr = input(f'''Selecione um dos tipos de quadrilátero disponível:
            (1)Retângulo
            (2)Quadrado
            (3)Trapézio''')

            while not verificando_tipo_de_quadr(tipo_quadr):
                tipo_quadr = input(f"""Escolha uma opção válida:
                (1)Retângulo
                (2)Quadrado
                (3)Trapézio""")

            #### QUADRILÁTEO - PEGAR DUAS ARESTAS###
            if str(tipo_quadr) == str(1):
                valor_arestas = [input(f'Insira o valor da {i + 1}ª aresta') for i in range(2)]
                poligono_2 = Quadrilatero(nome, valor_arestas[0], valor_arestas[1], '', 'Retângulo')
                poligono_2.calulando_area_retangulo()
                print(poligono_2)

            elif str(tipo_quadr) == str(2):
                valor_arestas = [input(f'Insira o valor da {i + 1}ª aresta') for i in range(1)]
                poligono_3 = Quadrilatero(nome, valor_arestas[0], '', '', 'Quadrado')
                poligono_3.calculando_area_quadrado()
                print(poligono_3)

            else:
                lista_bases = ['base maior', 'base menor', 'altura']
                valor_arestas = [input(f'Insira o valor da {base} aresta') for base in lista_bases]
                poligono_4 = Quadrilatero(nome, valor_arestas[0], valor_arestas[1], valor_arestas[2], 'Trapézio')
                poligono_4.calculando_area_trapezio()
                print(poligono_4)

        ### POLIGONOS REGULARES DE ORDEM MAIOR QUE QUATRO###
        if int(escolha) > int(4):
            count += 1
            nome = f'P{count}'
            print("""Esta opção é para Polígonos regulares de ordem maior que 4.
            Será necessário saber a apótema do polígono.""")
            lista_bases = ['aresta', 'apotema']
            valor_arestas = [input(f'Insira o valor da {base}') for base in lista_bases]
            poligono_5 = Regular(nome, escolha, valor_arestas[0], valor_arestas[1])
            poligono_5.calculando_area_regular()
            print(poligono_5)

#----------------------start-aux-functions------------------------#
def verificando_numeros_de_arestas(numero_arestas):
    if (numero_arestas.isdigit()):
        if int(numero_arestas) > int(2):
            return True

def verificando_tipo_de_quadr(tipo_quadr):
    valores = ['1','2','3']
    if str(tipo_quadr) in valores:
        return True
    else:
        False


#-----------------------end-function-------------------------#


if __name__=="__main__":
    main()
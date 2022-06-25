# Enunciados das questões:

# "Os juros compostos são a força mais poderosa do universo e a maior invensão da humanidade, porque permitem uma confiável e sistemática acumulação de riquezas." ~Albert Einstein.

# (A) Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.

# (B) Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais.

import matplotlib.pyplot as plt

def tratar(vI, r, a, p):

    #variáveis dos inputs:
    valorInicial = vI
    rendimento = r
    aporte = a 
    periodos = p
    listaX = []
    listaY = []
    #===================

    if periodos <= 0 :
        print("\n Você deve inserir pelo menos 1 período! \n")
        aplicacao()
    else:
        for periodo in range(1,periodos+1):
            valorRendido =  ((valorInicial * rendimento)/100) + valorInicial
            valorInicial = valorRendido + aporte
            listaX.append(periodo)
            listaY.append(valorInicial)
            print("Após", periodo, "períodos: R$",  round(valorInicial,2))
        print("\n")
        plt.plot(listaX, listaY)
        plt.show()
    
def aplicacao():
    print("\n")
    valorInicial = float(input("Valor inicial: "))
    rendimento = float(input("Rendimento em porcentagem: "))
    aporte = float(input("Aporte a cada período: "))
    periodos = int(input("Número de períodos: "))
    print("\n")
    tratar(valorInicial, rendimento, aporte, periodos)
    
aplicacao()





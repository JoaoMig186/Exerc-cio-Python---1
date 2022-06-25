# Enunciado das questões:

# (A) Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano.

# (B) Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual, entre 2013 e 2020.

# (C) Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.

import pandas as pd
import matplotlib.pyplot as plt

pibs_pais = pd.read_csv('tabelaPIBs.csv')

def questaoA():
    
    print("\n(Escolha um país e um ano para ver o PIB do país no ano escolhido.)\n")

    #Inputs País e Ano
    pais = str(input("País: "))
    ano = str(input("Ano: "))

    #Código para caso o ano estiver errado, mostrar mensagem que não foi encontrado o ano. (Não está funcionando.)
    '''ano_quantidade = len(pibs_pais.columns)
    anos_ = []
    for anos in range(1,ano_quantidade):
        index = pibs_pais.columns[anos]
        anos_.append(index)
        print(anos_)'''   
        
    #Pegar o tamanho da coluna de países
    pib_quantidade = len(pibs_pais['País'])
    #Pegar os países pelo índice no tamnho da coluna de países.
    for index in range(0,pib_quantidade):
        if pibs_pais['País'][index] == pais:
            #Pegar o PIB do país no ano.
            pib = pibs_pais.loc[index]
            print(f"O PIB do(a) {pais} é de: U${pib[ano]} trilhões.")
            app()
    if pais != pibs_pais['País'][index]:
        print("Erro! Nome do país não encontrado. \n")
        questaoA()

#Código para caso o ano estiver errado, mostrar mensagem que não foi encontrado o ano. (Não está funcionando.)    
''' elif pais not in anos_:
        print("Erro! Ano não encontrado \n")
        questaoA()'''
        
def questaoB():

    print("\n(Escolha um país para ver a variação do PIB com o passar dos anos.)\n")
    
    pais = str(input("País: "))

    pib_quantidade = len(pibs_pais['País'])
    for index in range(0,pib_quantidade):
        if pibs_pais['País'][index] == pais:
            pib = pibs_pais.loc[index]  

            #Cálculos da variação
            parte1 = float(pib[8]) - float(pib[1])
            parte2 = float(pib[1]) / 100
            parte3 = parte1/parte2
            print(f"A variação do PIB do(a) {pais} é de {round(parte3,2)} % entre 2013 e 2020.")
            app()

    if pais != pibs_pais['País'][index]:
        print("Erro! Nome do país não encontrado. \n")
        questaoB()
     


def questaoC():
    
    print("\n(Escolha um país para ver o gráfico de PIB's com o passar dos anos.)\n")

    pais = str(input("País: "))
    pib_quantidade = len(pibs_pais['País'])

    #Lista de PIBs vazia (e vai ser adicionado no for abaixo) e lista de anos já os valores estabelecidos.
    pibs = []
    anos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    for index in range(0,pib_quantidade):
        if pibs_pais['País'][index] == pais:
            pib = pibs_pais.loc[index]

            #For para pegar o index dos anos e adicionar na lista de PIBs. O + 1 é para pular a casa País.
            for ind in range(0, len(anos)):
                pibs.append(pib[ind+1])
            plt.plot(anos,pibs)
            plt.show()
            app()

    if pais != pibs_pais['País'][index]:
        print("Erro! Nome do país não encontrado. \n")
        questaoC()

def listas():
    print("\nLista de países:\nAlemanha\nBrasil\nCanadá\nChina\nCoreia do Sul\nEspanha\nEUA\nFrança\nÍndia\nIndonésia\nItália\nJapão\nMéxico\nReino Unido\nRússia")
    print("\nLista de Anos:\n2013\n2014\n2015\n2016\n2017\n2018\n2019\n2020")

def app() :
    print("\n")
    escolha = str(input("Escolha qual questão deseja (A, B ou C maiúsculos) ou 0 para sair: "))
    print("\n")
    if escolha == "A":
        questaoA()
        print("\n")
    elif escolha == "B":
        questaoB()
        print("\n")
    elif escolha == "C":
        questaoC()
        print("\n")
    elif escolha == "0":
        exit()
    else: 
        print("Você digitou uma opção inválida")
        app()

listas()
app()

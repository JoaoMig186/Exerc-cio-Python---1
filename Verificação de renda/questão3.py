# Enunciado da questão.

# Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, no máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte. Esses valores não devem ser totalmente desprezados, mas não podem funcionar como um norte para o orçamento doméstico de todas as famílias.

# Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo.

print("\n")
rendaMensal = float(input("Entre com a sua renda: "))
print("\n")
valorMoradia = float(input("Entre com o valor gasto com moradia: "))
valorEducacao = float(input("Entre com o valor gasto com educação: "))
valorTransporte = float(input("Entre com o valor gasto com transporte: "))
valido = True
print("\n")
if (rendaMensal < 0) or (valorMoradia < 0) or (valorEducacao < 0) or (valorTransporte < 0):
    valido = False

def validacoes():
    #Iníco da validação da moradia.
    porcentagemMoradia = (valorMoradia*100)/rendaMensal
    porcentagemMoradiaROUND = round(porcentagemMoradia,2) 
    gastoMaximoMoradia = (rendaMensal*0.3)
    gastarMaximoMoradiaROUND = round(gastoMaximoMoradia,2)
    if valorMoradia > gastoMaximoMoradia:
        print(f"Os gastos com moradia são de {porcentagemMoradiaROUND}% da renda mensal e estão acima dos 30% máximo recomendável. O gasto máximo em reais com moradia poderia ser de R$ {gastarMaximoMoradiaROUND}")
        print("----------------------------------------------")
    else:
        print(f"Os gastos com moradia são de {porcentagemMoradiaROUND}% da renda mensal e estão dentro dos 30% máximo recomendável.")
        print("----------------------------------------------")
    #Fim da validação da moradia.

    #Início da validação da educação.
    porcentagemEducacao = (valorEducacao*100)/rendaMensal
    porcentagemEducacaoROUND = round(porcentagemEducacao,2)
    gastoMaximoEducacao = (rendaMensal*0.2)
    gastoMaximoEducacaoROUND = round(gastoMaximoEducacao,2)
    if valorEducacao > gastoMaximoEducacao:
        print(f"Os gastos com educação são de {porcentagemEducacaoROUND}% da renda mensal e estão acima dos 20% máximo recomendável. O gasto máximo em reais com educação poderia ser de R$ {gastoMaximoEducacaoROUND}")
        print("----------------------------------------------")
    else:
        print(f"Os gastos com educação são de {porcentagemEducacaoROUND}% da renda mensal e estão dentro dos 20% máximo recomendável.")
        print("----------------------------------------------")
    #Fim da validação da educação.

    #Início da validação de transporte.
    porcentagemTransporte = (valorTransporte*100)/rendaMensal
    porcentagemTransporteROUND = round(porcentagemTransporte,2)
    gastoMaximoTransporte = (rendaMensal*0.15)
    gastoMaximoTransporteROUND = round(gastoMaximoTransporte,2)
    if valorTransporte > gastoMaximoTransporte:
        print(f"Os gastos com transporte são de {porcentagemTransporteROUND}% da renda mensal e estão acima dos 15% máximo recomendável. O gasto máximo em reais com transporte poderia ser de R$ {gastoMaximoTransporteROUND} \n")
    else:
        print(f"Os gastos com transporte são de {porcentagemTransporteROUND}% da renda mensal e estão dentro dos 15% máximo recomendável. \n")
    #Fim da validação de transporte.
if valido == False: 
    print("Foi passado um valor negativo em uma das entradas. Impossível realizar as operações. \n")
    exit()
else:
    validacoes()



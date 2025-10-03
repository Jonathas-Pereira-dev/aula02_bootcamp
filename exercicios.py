import math 

##Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

#numero_01 = int(input("Digite o primeiro número: "))
#numero_02 = int(input("Digite o segundo número: "))

#divisao_inteira = numero_01 // numero_02

#print("A divisão inteira de", numero_01, "por", numero_02, "é:", divisao_inteira)

##10. Escreva um programa que calcula a área de um írculo, recebendo o raio como entrada.

#raio_indicado = float(input("Digite o raio do círculo: "))
#area_indicada = 2 * math.pi * raio_indicado

#print(f"{area_indicada:.2f}")

#data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
#lista_dia_mes_ano = data_usuario.split("/")
#print(f"Dia: {lista_dia_mes_ano[0]}")
#print(f"Mês: {lista_dia_mes_ano[1]}")
#print(f"Ano: {lista_dia_mes_ano[2]}")

#numero = int(input("Digite um número inteiro: "))
#if isinstance(numero, int ):
   # print("O número digitado é um número inteiro.") 
#else:
    #print("O número digitado não é um número inteiro.")

idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")
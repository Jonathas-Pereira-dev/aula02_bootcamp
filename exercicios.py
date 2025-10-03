import math 

##Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

#numero_01 = int(input("Digite o primeiro número: "))
#numero_02 = int(input("Digite o segundo número: "))

#divisao_inteira = numero_01 // numero_02

#print("A divisão inteira de", numero_01, "por", numero_02, "é:", divisao_inteira)

##10. Escreva um programa que calcula a área de um írculo, recebendo o raio como entrada.

raio_indicado = float(input("Digite o raio do círculo: "))
area_indicada = 2 * math.pi * raio_indicado

print(f"{area_indicada:.2f}")

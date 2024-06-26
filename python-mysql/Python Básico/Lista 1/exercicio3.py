#(3) - Escreva um programa que resolva uma equação de segundo grau.
# ax² + bx + c = 0

import math

print("====== Equação de segundo grau ======\n")
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))

delta = (valorB ** 2) - 4 * valorA * valorC
print("\nValor de Delta: ", delta)

x1 = (-valorB + (math.sqrt(delta))) / (2 * valorA)
x2 = (-valorB - (math.sqrt(delta))) / (2 * valorA)

print("\nValor de X¹: ", x1)
print("\nValor de X²: ", x2)
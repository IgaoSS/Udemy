#(5) - Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

print("\n============= Calculadora =============\n")

valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
operacao = input("Informe o sinal da operação a ser executada: ")

if operacao == '+':
    print("O resultado é: " + str(valor1 + valor2))
elif operacao == '-':
    print("O resultado é: " + str(valor1 - valor2))
elif operacao == '*':
    print("O resultado é: " + str(valor1 * valor2))
elif operacao == '/':
    print("O resultado é: " + str(valor1 / valor2))
elif operacao == '**':
    print("O resultado é: " + str(valor1 ** valor2))
else:
    print("Operação inválida")
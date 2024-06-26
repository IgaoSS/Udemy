#This code show the first print
print("Hello world!");

#This code show the second print
print("Another messsage!");

#Conditional Structure
x = 1;
y = 2;

if (x > y):
    print('X é maior que Y')
elif (x == y):
    print('X é igual a Y')
else:
    print('X é menor que Y')

#Repetition structure
for i in range(1,10):
    print(i * 2)

'''Adicionando um index para pegar a lista'''
lista1 = [1,4,4,4,5,6,7,8,"teste"]
for idx, i in enumerate(lista1):
    print("Elemento da posição [", idx, "]: ", i)

#Comando input
num = input("Digite um número: ")
print("O número digitado é: ", num)

#Concantenar strings
a = "Igor"
b = "Sousa"

concatenar = a + ' ' + b
print(concatenar[0:2])

#Deixar texto em minúsculo
print(concatenar.lower())

#Deixar o texto em maiúsculo
print(concatenar.upper())

#Função strip() ele remove espaços desnecessários no fim
print(concatenar.strip())

#Função split() converte a sequência em uma lista
#Caso informe uma letra, ele quebrará na letra, ela não exibirá
listaX = 'Igor Sousa da Silva'
print(listaX.split(" "))
print(listaX.split("a"))

#Método find() informa a posição de uma palavra ou caracter
print(listaX.find("da"))
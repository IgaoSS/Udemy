#(4) - Escreva um programa que ordene uma lista numérica com três elementos.

num1 = input("Informe o primeiro valor para a lista: ")
num2 = input("Informe o segundo valor para a lista: ")
num3 = input("Informe o terceiro valor para a lista: ")

lista = num1 + "," + num2 + "," + num3
lista = lista.split(",")
print("Lista inicial: ", lista);

for x in range(len(lista)):
    menor = x;

    for y in range(x+1, len(lista)):
        if lista[y] < lista[menor]:
            menor = y;

    if lista[x] != lista[menor]:
        aux = lista[x];
        lista[x] = lista[menor];
        lista[menor] = aux;

print("Lista ordenada: ", lista)

##print("Exibição da lista original: ", lista)
##print("Exibição da lista ordenada: ", sorted(lista))

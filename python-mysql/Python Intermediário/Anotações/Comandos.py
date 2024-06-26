############## LISTA PARTE 1 ##############
lista1 = ["Abacaxi", "Banana", "Cereja", "Damasco"];
lista2 = [15,12,14,13,11];
lista3 = [15,12,14,13,11];

# Para adicionar elemento na lista
lista1.append("Framboesa");
print("Lista com novo elemento adicionado: ", lista1);

# Para chegar se um valor está contido na lista
if 12 in lista2:
    print("O valor buscado está na lista!");
else:
    print("O valor buscado não se encontra na lista!");

# Para apagar um elemento da lista
'''O 0 indica a posição que vai começar removendo'''
'''O 1 indica quantos elementos serão removidos'''
del lista1[0:1]
print("Lista com elementos removidos: ", lista1);

'''Para remover todos elementos da lista'''
del lista1[:]
print("Lista com todos elementos removidos: ", lista1);

# Ordenar lista
'''Inverter a ordem da lista'''
lista2.reverse();
print("Lista invertida: ", lista2);

'''O sorted, ele requer que a sua nova lista seja atribuída a uma variável'''
listaOrdenada = sorted(lista2);
print("Lista ordenada com sorted(): ", listaOrdenada);

'''Sort aplica a função direto na lista referenciada'''
lista2.sort();
print("Lista ordenada com sort(): ", lista2);

'''Para fazer a lista ficar em ordem decrescente, só adicionar o parâmetro reverse=true'''
lista2.sort(reverse=True);
print("Lista ordenada em ordem decrescente: ", lista2);
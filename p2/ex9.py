#Intercalar Listas: Crie duas listas de números com o mesmo tamanho.
#Escreva um programa que gere uma nova lista contendo os
#elementos das duas listas intercalados (um elemento de cada lista por vez).

lista1=[1,3,5,7,9]
lista2=[0,2,4,6,8]
lista3=[]
for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)

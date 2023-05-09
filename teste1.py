#Números não multiplos de 5, divisíveis por 7 entre 2000 e 3200

inicio = 2000
fim = 3201
intervalo = fim - inicio
lista = []

for i in range(intervalo):
    if inicio % 5 != 0 and inicio % 7 == 0:
        lista.append(inicio)
    if i <= fim:
        inicio += 1

print(lista)


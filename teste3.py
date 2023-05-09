#Fatorial de um número
n = 7
r = 0
for i in range(n-1, 1, -1):
    r = n * i
    n = r

print(r)

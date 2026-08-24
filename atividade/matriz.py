matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()

soma = 0

for linha in matriz:
    for valor in linha:
        soma += valor
print(soma)
print()

for i in range (len(matriz)):
    print(matriz[i][i])
print()

maior = 0
for linha in matriz:
    for valor in linha:
        if maior < valor:
            maior = valor
print(maior)

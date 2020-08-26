## Hi! This code does the sum between digits from a number.
## Author: Juliana Furtado

x = int(input("Digite um número inteiro: "))
x = str(x)
n = len(x)
x = int(x)
counter = 0
soma = 0

while (counter != n):
    counter = counter + 1
    div = x // 10**(n-counter)
    x = x % 10**(n-counter)
    soma = soma + div
print(soma)

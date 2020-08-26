## Hi! This code show all odd numbers.
## Author: Juliana Furtado

# Here the code require you to put an integer positive number. 
x = int(input("Digite o valor de n: "))  
while x <= 0:
    x = int(input("Digite o valor de n: "))

counter = 0
soma = 0
while soma != x:
    counter = counter + 1
    resto = counter % 2
    if resto != 0:
        print(counter)
        soma = soma + 1

## Hi! This code does the factorial calculation from a natural number.
## Author: Juliana Furtado
## Look fatorial2.py to see easier factorial's calculation.
    
x = int(input("Digite o valor de n: "))
while x < 0:
    x = int(input("Digite o valor de n: "))

real_n = 0
if x > 0:
    if x == 1:
        real_n = 1
        print(real_n)
    else:
        counter = 0
        previous_n = x
        while counter < (x-1):
            counter = counter + 1
            real_n = previous_n * (x-counter)
            previous_n = real_n
        print(real_n)
else:
    real_n = 1
    print(real_n)

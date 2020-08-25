# Este programa recebe um número inteiro maior ou igual a 2 como parâmetro
# e devolve o maior número primo menor ou igual ao número passado à função

def maior_primo(n):
    den = n-1
    while (n > 2):
        resto = n % den
        if (resto == 0):
            n = n-1
            den = n-1
        else:
            if (den == 2):
                break
            else:
                den = den-1
    return n
                
                
        

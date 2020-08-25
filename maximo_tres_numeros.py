def maximo(x, y, z):
    if (x > y):
        if (x > z):
            maior_numero = x
        else:
            maior_numero = z

    elif (y > x):
        if (y > z):
            maior_numero = y
        else:
            maior_numero = z

    else:
        if (z > y):
            maior_numero = z
        else:
            maior_numero = y
            
    return maior_numero


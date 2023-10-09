#ruweschatter getal
def ruweschatter(getal):
    i = 0
    vermenigvuldiger = 1
    while vermenigvuldiger**2 <= getal:
        i += 1
        vermenigvuldiger += 1
    return vermenigvuldiger - 1, i

#vierkantswortel
def vierkantswortel(getal, factor = 0.001):
    start, i = ruweschatter(getal)
    vermenigvuldiger = start + factor

    while factor < getal - vermenigvuldiger ** 2 and vermenigvuldiger ** 2 < getal:
        vermenigvuldiger += factor
        i += 1
    return vermenigvuldiger, i

print(vierkantswortel(1342352526252))
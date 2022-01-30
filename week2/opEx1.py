def conta_letras(frase, contar="vogais"):
    vogais = "aeiou"
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    c = 0

    if contar == "vogais":
        for i in frase.lower():
            if i in vogais:
                c += 1
    else:
        for i in frase.lower():
            if i in consoantes:
                c += 1
    return c

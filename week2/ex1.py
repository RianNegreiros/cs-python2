def maiusculas(frase):
    upper = ''
    for char in frase:
        if char.isupper():
            upper += char
    return upper

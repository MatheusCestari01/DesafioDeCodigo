def verificar_anagrama_palindromo(string):
    ocorrencias = {}
    for char in string:
        if char in ocorrencias:
            ocorrencias[char] += 1
        else:
            ocorrencias[char] = 1

    num_impares = 0
    for count in ocorrencias.values():
        if count % 2 != 0:
            num_impares += 1
            if num_impares > 1:
                return False

    return True

string_exemplo = "racecar"
print(verificar_anagrama_palindromo(string_exemplo))
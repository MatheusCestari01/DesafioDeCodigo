def encontrar_substring(string):
    string_modificada = '#'.join('^{}$'.format(string))

    palindromos = [0] * len(string_modificada)

    centro = direita = 0
    for i in range(1, len(string_modificada)-1):
        if i < direita:
            espelho = 2 * centro - i
            palindromos[i] = min(direita - i, palindromos[espelho])

        while string_modificada[i + 1 + palindromos[i]] == string_modificada[i - 1 - palindromos[i]]:
            palindromos[i] += 1

        if i + palindromos[i] > direita:
            centro = i
            direita = i + palindromos[i]

    max_palindromo = max(palindromos)
    centro_palindromo = palindromos.index(max_palindromo)
    inicio = (centro_palindromo - max_palindromo) // 2
    fim = inicio + max_palindromo

    substring_palindroma = string[inicio:fim]
    return substring_palindroma


string_original = "babad"
substring_palindroma = encontrar_substring(string_original)
print(substring_palindroma)

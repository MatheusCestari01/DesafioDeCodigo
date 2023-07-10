def remover_caracteres(string):
    caracteres_unicos = []
    for char in string:
        if char not in caracteres_unicos:
            caracteres_unicos.append(char)
    string_sem_duplicados = ''.join(caracteres_unicos)
    return string_sem_duplicados

# Exemplo de uso:
string_original = "Hello, World"
string_sem_duplicados = remover_caracteres(string_original)
print(string_sem_duplicados)

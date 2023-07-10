def letra_maiuscula(string):
    frases = string.split('. ')
    frases_maiusculas = [frase.capitalize() for frase in frases]
    string_maiuscula = '. '.join(frases_maiusculas)
    return string_maiuscula


string_original = "hello, how are you? i'm fine, thank you"
string_maiuscula = letra_maiuscula(string_original)
print(string_maiuscula)

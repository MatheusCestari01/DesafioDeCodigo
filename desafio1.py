def reverter_ordem(frase):
    palavras = frase.split()
    palavras_revertidas = palavras[::-1]
    frase_revertida = ' '.join(palavras_revertidas)
    return frase_revertida

frase_original = "Hello, World! OpenAi is amazing."
frase_revertida = reverter_ordem(frase_original)
print(frase_revertida)
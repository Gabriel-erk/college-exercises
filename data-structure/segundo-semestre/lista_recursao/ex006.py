def eh_palindromo(texto):
    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return eh_palindromo(texto[1:-1])


print(eh_palindromo("arara"))
print(eh_palindromo("python"))
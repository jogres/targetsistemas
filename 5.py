def inverte_string(s):
    nova_string = ""
    for i in range(len(s) - 1, -1, -1):
        nova_string += s[i]
    return nova_string


string_original = input("Digite uma string: ")


string_invertida = inverte_string(string_original)


print("String original:", string_original)
print("String invertida:", string_invertida)
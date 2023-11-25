#  Verificar conteúdo da String

# Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

import re

text = input("Digite a frase:\n")
rule1 = "[a-z]"
rule2 = "[A-Z]"
rule3 = "[0-9]"

resultado1 = re.findall(rule1, text)
resultado2 = re.findall(rule2, text)
resultado3 = re.findall(rule3, text)

print(f"As letras de a-z são: {resultado1}")
print(f"As letras de A-Z são: {resultado2}")
print(f"Os números de 0-9 são: {resultado3}")

# Correção


def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)


print(check_character("ABCDEFabcdef123450"))
print(check_character("*&%@#!}{"))

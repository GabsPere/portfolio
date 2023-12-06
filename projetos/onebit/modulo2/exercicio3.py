import re
#importando módulo de expressão regular.

#criando input que irá receber a frase
texto=input("Digite sua frase aqui\n> ")

#criando padroes que serao buscados na frase
padrao1="[a-z]"
padrao2="[A-Z]"
padrao3="[0-9]"

#criando as variavris que irao analisar a frase
#padrao1
resultado1=re.findall(padrao1,texto)
print(f'o resultado do primeiro padrão ({padrao1}) é: {resultado1}')

#padrao2
resultado2=re.findall(padrao2,texto)
print(f'o resultado do segundo padrão({padrao2}) é: {resultado2}')

#padrao3
resultado3=re.findall(padrao3,texto)
print(f'o resultado do terceiro padrão ({padrao3}) é: {resultado3}')
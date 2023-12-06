# 43 - Exercício 5
## Conta letras maiúsculas e minúsculas
# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
# def check_char(frase):
#     Dicionário = {"Uppercase":0, "Lowercase":0}
#     for variável in frase:
#         if variável.isupper():
#             Dicionário["Uppercase"]+=1
#         elif variável.islower():
#             Dicionário["Lowercase"]+=1
            
#     print("Texto original:",frase)     
#     print("Número de letras maísculas:",Dicionário["Uppercase"])
#     print("Número de letras mínusculas:",Dicionário["Lowercase"])   
    
# (check_char(input("Digite a frase:")))



# ## Lista números pares e ímpares de uma lista
# Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

def checar_numeros(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
print(checar_numeros([1,2,3,8,9,1,78,2,598,20]))
    

        
            




    
    
    
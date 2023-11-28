## Contagem Regressiva
# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”. 
# for i in range (10,0, -1):
#     if i > 0:
#         print(i)
#     if i == 1:
#         print("Beep")
#correção
# import winsound
# x = 10
# while x >=0:
#     print(x)
#     x-= 1
# winsound.Beep(2500,550)

# ## Tabuada
# Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
# input("Tabuada. Pressione ENTER para continuar")
# valor_inicial = int(input("Digite o valor inicial: "))
# valor_final = int(input("Digite o valor final: "))
# vezes_multiplicado = 0
# while valor_inicial != valor_final:
#     for i in range(valor_inicial, (valor_final+valor_inicial), valor_inicial):
#         vezes_multiplicado += 1
#     print(f"Para chegar no resultado final de {vezes_multiplicado*valor_inicial} foi preciso multplicar {valor_inicial} X {vezes_multiplicado}.\nCaso o valor final não tenha sido igual o digitado é porquê os valores não divisíveis.")
#     break 

## Tabuada correção
number = int(input("Tabuada do: \n"))
begin = int(input("Começa: \n"))
end = int(input("Até: \n"))

x = begin

while x <= end:
    print(f"Tabuada de {number} x {x} = {number*x}")
    x = x + 1
# x = x+1 serve para não cair em loop, ou seja, se você colocar 5 no X, após executar a primeira parte ele irá ler 
# x = 5+1 e inputar esse dado para X, virando 6. Precisa ser no formato de x = x+1, caso contrário da loop.
    
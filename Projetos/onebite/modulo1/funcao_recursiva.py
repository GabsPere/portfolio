#são funções que tem mais de uma chamada dentro delas.
def  fatorial(num):
    if num == 1:
        return 1
    else:
        return (num*fatorial(num - 1))
    #Aqui a função está sendo chamada novamente, fazendo com que fique: fatorial (4) | else return (4 * 3 (4-1)), repetindo até num == 1. 
    # Por isso recursiva.
num = int(input(f"Digite o número para fatorial:\n"))
print(f"O fatorial de {num} é: {fatorial(num)}!")
    
    
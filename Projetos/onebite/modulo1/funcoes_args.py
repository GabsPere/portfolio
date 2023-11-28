#args

# def sum (*num):
#     sum_total = 0
#     for n in num:
#         sum_total += n
#     print(f"A soma total é: {sum_total}!")
# sum(2,3,48,9,58)
     
nome_time = input("Qual o nome do time?\n")
def name(**nomes):
    for key, values in nomes.items():
        print(f" {key} - {values}")
    
        
name(Nome=nome_time, Jogadores = 23, Nacionalidade = "São Paulo")     

 
        
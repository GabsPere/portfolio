#listar valores de 0 a 10 e retornar os menores que 4

# for i in range (10):
#     if i <4:
#         print(i)

# list_numbers = [ i for i in range(10) if i <4]
# print(list_numbers)

game_list = ["Mario","CS GO","Lol", "Dota",
             "Fifa"]
new_list = [x for x in game_list if "B" in x]
print(new_list)

for i in game_list:
    if "a" in i:
        print(i)
#lemos da seguinte forma para I dentro de game_list (para criar I), precisamos que "a" esteja contido em I, ou seja, 
# apenas palavras com A que estão dentro da game_list farão parte de I.

       
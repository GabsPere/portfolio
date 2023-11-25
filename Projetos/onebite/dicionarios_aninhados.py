import pprint
games_dict ={"Resident_Evil_4":{
    "year_launch": 2023,
    "classification": 9.8,
    "genre": ["ação", "aventura"]
},
             "Mario_Odyssey":{
                 "year_launch": 2017,
                 "classification": 10,
                 "genre": ["aventura", "3D"]
             },
             "league_of_legends":{
                 "year_launch": 2011,
                 "classification": 10,
                 "genre": ["moba","strategy"]
             }
             
             }

pp=pprint.PrettyPrinter(depth=4)


pp.pprint(games_dict)

#buscar informações em dicionários aninhados
print(games_dict["league_of_legends"]["genre"])

#adcionar informações
games_dict["league_of_legends"]["players"] = 5 
print(games_dict["league_of_legends"])
#mesmo esquema com o dicionário normal, mas antes precisamos informar qual a chave e depois o valor que buscamos

#deletar dicionário
del games_dict["Resident_Evil_4"]
pp.pprint(games_dict)


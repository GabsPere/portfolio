gameFifa = {
"name": "Fifa 23",
"Year_Launch": 2022,
"Game_Price": 90.50,
"Genre": ["Esporte", "Família"]

}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#recuperar um elemento 
print(gameFifa["Genre"]) # Aqui vai entre [], pois é uma lista
print(gameFifa.get("Game_Price")) #Aqui usamos o get pois está dentro do dicionário, mas a chave precisa estar identico ao do dicionário.

#Podemos recuperar apenas as chaves ou valores. Isso é bom para quando não sabemos como está um valor e queremos usar o comando get.
#O comando items retorna chaves e valores em tupla.
print(gameFifa.keys())
print(gameFifa.values())
print(gameFifa.items())

#conseguimos adicionar itens ao dicionário
gameFifa["Players"] = 2
print(gameFifa)

#Podemos atualizar itens
gameFifa.update({"Players":4})
print(gameFifa) #interessante, pois mesmo realizando a atualização com base no "gamefifa", é necessário tirar print novamente.

#Remover
gameFifa.pop("Players") #Utilizamos a chave
print(gameFifa)


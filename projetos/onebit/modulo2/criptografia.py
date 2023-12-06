import hashlib


#1 verificar algoritmos disponiveis
print(hashlib.algorithms_available)

#2 verificar algoritmos disponiveis no sistema operacional
print(hashlib.algorithms_guaranteed)

#3 usando sha256
algoritmo = hashlib.sha256()
message = "A melhor forma de prever o futuro é criá-lo".encode()
algoritmo.update(message)
print(algoritmo.hexdigest())

#4 utilizando o md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())



import random

# 1 Selecionar valor  aleatorio

list1 = [1, 2, 5, 8, 12, 19, 23]
print(random.choice(list1))

# 2 Gera um valor aleatório dentro de um intervalo
r1 = random.randint(0, 100)
print(r1)

# 3 Retorna caracter aleatorio
name = "Curso Python"
f2 = random.choice(name)
print(f2)

# 4 Retornar mais de um valor -  sintaxe random.sample(sequência, tamanho)
print(random.sample(list1, 5))

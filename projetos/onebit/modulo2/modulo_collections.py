from collections import namedtuple, deque, Counter
from operator import itemgetter


# 1 Contar itens de uma lista (counter)
frutas = ["Uva", "Maçã", "Uva", "Abacaxi", "Mamão", "Pera", "Uva",
          "Abacaxi", "Maçã", "Goiaba"]
print(frutas)
print(Counter(frutas))

# 2 Utilizando tupla nomeada - Tem chave e valores.
game = namedtuple('Jogos', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4", 300.00, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
studants = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)

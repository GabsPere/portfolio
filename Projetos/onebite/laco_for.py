#sistema de média das provas
nome_aluno = input("Informe o nome do aluno:\n")
quantidade_de_notas=int(input("Quantas notas deseja inserir?\n"))

soma_notas = 0

for i in range(quantidade_de_notas):
    notas = float(input("Qual o valor da nota?\n"))
    soma_notas += notas
print(f"A média das do aluno {nome_aluno} é de {soma_notas/notas:.2f}!")

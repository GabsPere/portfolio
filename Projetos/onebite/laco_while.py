#Avaliação de Produtos

nome_produto = input("Digite o nome do produto que gostaria de avaliar:\n")
feedback = 0
notas_avaliacoes = 0
avaliacao = 0
media = 0

while avaliacao != -1:
    avaliacao = float(input("Informe a nota do produto:\n"))
    if avaliacao != -1:
        notas_avaliacoes += avaliacao
        feedback += 1
        media = notas_avaliacoes / feedback
print(f"A média de avaliação do produto {nome_produto} é de {media:.2f}!")
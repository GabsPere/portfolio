"""saudações = "Olá, seja bem vindo!"
nome = input("Primeiro, me diga como quer ser chamado:\n")
idade = int(input("Qual sua idade?\n"))
#Caracteristicas
altura = float(input("Qual sua altura?\n"))
peso = float(input("Qual seu peso?\n"))

identidade =(f"Seu apelido será {nome}, você tem {idade} anos!\nSua altura é: {altura} e você tem {peso} kilos.")
print(identidade)"""

#Listas de livros
livros = [input("Coloque o nome do livro: "), input("Livro 2: ")]
adicionar = input("Deseja adicionar um livro [1] - Sim [2] - Não: \n")
quantidade = len(livros)
if adicionar == "1":
    livro = input("Título do Livro: ")
    coleção = livros.append(livro)
    quantidade = len(livros)
    print(f"Você tem {quantidade} livros, sendo eles: {livros}")
else: 
    print(f"Você tem {quantidade} livros, sendo eles: {livros}")
    













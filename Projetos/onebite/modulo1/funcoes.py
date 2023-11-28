# def sum():
#     return 5 + 4
# print(sum())
# #se usamos o return é obrigatório colocar o print antes de chamar a função.

# def hello_world():
#     print("Hello World")
# hello_world()
#quando usamos apenas a fórmula sem o return, precisamos chamar a fórmula FORA da indentação do print, apenas.

#para usar com paramêtros
# def nome_completo(p_nome, u_nome):
#     print(f"Nome completo: {p_nome} {u_nome}")
# nome_completo(input("Primeiro nome:\n"), input("Último nome:\n"))

#paramêtros default (padrão)
def adress(country="Brasil"):
    print(f"Eu moro em: {country}")
adress()
adress(input("Qual país você mora:\n"))
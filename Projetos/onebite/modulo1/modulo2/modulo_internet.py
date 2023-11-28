
import webbrowser
done = False

while not done:

    print("O que deseja fazer?")
    print("1 - Assisitir Jujutsu.")
    print("2 - Aprender sobre programação")
    print("3 - Aprender sobre Pyhthon")
    print("4 - Sair")

    escolha = input("> ")
    if escolha == "1":
        webbrowser.open(
            "https://www.crunchyroll.com/pt-br/watch/G14U43ZV9/sage?modal=restricted")
    elif escolha == "2":
        webbrowser.open("https://www.youtube.com/@FilipeDeschamps")
    elif escolha == "3":
        webbrowser.open("http://www.python.org")
    elif escolha == "4":
        done = True

num_1 = float(input("Digite o primeiro número:\n"))
num_2 = float(input("Digite o segundo número:\n"))

operation = input("Escolha a operação (+ - / *):\n")

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "/":
    result = num_1 / num_2
elif operation == "*":
    result = num_1 * num_2
else:
    print("Operação inválida.")
    
print(f"O resultado da operação é: {result:.2f}")
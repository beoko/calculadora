#Calculadora
print("Vamos fazer uma calculadora!")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (adicao, subtracao, multiplicacao, divisao): ")

if operacao == "adicao":
  print("A soma é:", num1 + num2)
elif operacao == "subtracao":
  print("A subtração é:", num1 - num2)
elif operacao == "multiplicacao":
  print("A multiplicação é:", num1 * num2)  
elif operacao == "divisao":
  print ("A divisão é:", num1 / num2)
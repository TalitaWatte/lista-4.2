# Peça ao usuário dois números (n1 e n2). O programa deve dizer qual deles é o maior ou se são iguais.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior")
elif num1 < num2:
    print("O segundo número é maior")
elif num1 == num2: 
    print("Os dois números são iguais")
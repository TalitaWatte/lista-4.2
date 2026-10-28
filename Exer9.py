# Crie um script que peça a idade do usuário. 
# Se for 18 ou mais, exiba "Acesso Liberado ao Jogo". Caso contrário, exiba "Acesso Negado".


idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Acesso Liberado ao Jogo")
else: 
    print("Acesso Negado")
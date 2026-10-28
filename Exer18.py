# Crie um menu onde o jogador escolhe entre 1 (Falar), 2 (Atacar) ou 3 (Fugir). 
# Use if/elif/else para exibir uma resposta diferente para cada escolha

print("Menu")
print("1- Falar")
print("2- Atacar")
print("3- Fugir")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print("Jogador, você ganhou o jogo!")
elif opcao == 2:
    print("Jogador, você atacou a pessoa errada!")
elif opcao == 3:
    print("Jogador, você é um covarde!")
else:
    print("Jogador, você é burro? Escolha uma das opções. ")

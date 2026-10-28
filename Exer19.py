#O jogador quer pegar um item de peso 5. Verifique se o peso_atual + 5 ultrapassa o limite_maximo de 50. 
# Se ultrapassar, imprima "Inventário Cheio!".

peso_atual =  int(input("Qual o peso atual do seu inventário, jogador? "))
peso_novo = 5
peso_limite = 50
if peso_atual + 5 >= peso_limite:
    print("Inventário Cheio!")
else:
    print("Item adicionado ao inventário!")





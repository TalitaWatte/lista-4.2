#Escreva um código que peça a vida do jogador. Se for igual a 0, imprima "Game Over".

vida = int(input("Quantas vidas você possui? "))

if vida <= 0:
    print("Game Over")
else:
    print("You Win")    

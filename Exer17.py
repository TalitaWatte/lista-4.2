#Se os pontos do jogador forem maiores que 1000, mude a variável nivel para 2 e dê um bônus de 100 de vida.

pontos = int(input("Quantos pontos você tem? "))
nivel = 1
vida = 100

if pontos >= 1000:
    nivel = 2
    vida = vida + 100

print("Nível:", nivel)
print("Vida:", vida)
#No Godot, queremos evitar que o personagem saia da tela. 
# Se a posicao_x for menor que 0 ou maior que 1024, imprima "Atenção: Saindo da tela!".

posicao = int(input("Qual a sua posição, jogador? "))

if posicao <= 0 or posicao >= 1024 :
    print("Atenção: Saindo da tela!")
else:
    print("Atenção jogador")
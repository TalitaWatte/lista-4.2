#Se o jogador tem um escudo_ativo = True, ele recebe apenas 50% do dano. Se for False, recebe 100%. 
#Escreva a lógica que calcula o dano_final baseado em um dano_base = 20.

dano_base = 20
escudo_ativo = True

if escudo_ativo == True:
    dano_final = 10
else:
    dano_final = 20

print(dano_final)
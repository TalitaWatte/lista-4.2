#Crie uma variável senha_mestra = "python123". 
# Peça ao usuário para digitar uma senha e use um if para verificar se ele acertou.


senha_mestra = "python123"
senha = (input("Digite sua senha: "))

if senha != "python123":
    print("Senha incorreta, tente novamente")
elif senha == "python123":
    print("ACESSO LIBERADO!")


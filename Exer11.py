#Crie um programa que receba a nota de um aluno:
#● Se for 7 ou mais: "Aprovado".
#● Se for entre 5 e 6.9: "Recuperação".
#● Se for menor que 5: "Reprovado".

nota = float(input("Nota: "))

if nota >= 7:
    print("Aprovado")

elif nota >= 5 and nota <= 6.9:
    print("Recuperação")

elif nota <= 5:
    print("Reprovado")


# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
l1=float(input("Digite o comprimento do lado 1: "))
l2=float(input("Digite o comprimento do lado 2: "))
l3=float(input("Digite o comprimento do lado 3: "))
if l1>l2+l3 and l2>l1+l3 and l3>l1+l2:
    print ("Pode formar um triangulo")
else: 
    print ("Não pode formar um triangulo")

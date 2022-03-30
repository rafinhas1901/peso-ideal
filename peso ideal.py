print("Programa de calculo de peso ideal \n")

altura = float(input("Informe sua altura:" ))

sexo = input("Informe seu sexo (masculino: 1 / feminino: 2): " )

if sexo is 1:
    idealmasc = (72.7*altura) - 58 
    print("Seu peso ideal é", idealmasc)

if sexo is 2:
    idealfem = (62.1*altura) - 44.7
    print("Seu peso ideal é:", idealfem)

print("Obrigado po usar esse programa!")
print("Desenvolvedor: Rafael Defanti Azevedo")

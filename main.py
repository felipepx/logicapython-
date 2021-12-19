a = input("Digite a idade da pessoa: ")
idade = int (a)

if idade <=1:
    print ("Recém nascido")
elif idade < 13:
        print ("Criança")
elif idade < 18:
    print ("Adolescente")
elif idade < 60:
    print ("Adulto")
elif idade < 80:
    print ("Idoso")
else:
    print ("Longevo")

print ("Acabou.")

input('')



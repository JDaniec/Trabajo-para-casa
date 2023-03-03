print("--------------------------")
print("-----verificar si un numero es positivo y de cuatro digitos------------")
print("---------------------------")

#intput
a = int(input("Digite el numero: "))

#processing

if a > 0 and a >= 1000 and a <=9999:
    print("El numero tiene cuatro digitos y es positivo")

else:
    print("El numero no es de cuatro digitos o no es positivo")



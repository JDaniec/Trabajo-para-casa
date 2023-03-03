print("-----------------------")
print("Mayor o menor")
print("------------------------")

#intput

a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))


#processing 

a > b 

if a > b: 
    rta = "El numero " + str(a)+ " es mayor que el numero " + str(b)

else:
    rta = "El numero " + str(b)+ " es mayor que el numero " + str(a)

#output
print(str(rta))

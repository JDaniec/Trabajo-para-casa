print("------------------")
print("Cual de los 3 numeros es mayor")
print("-------------------")

#input
a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero "))

#processing

if a > b and a > c:
    rta = "El numero " + str(a) + " es mayor que " + str(b) + " y tambien es mayor que " + str(c)

elif b > a and b > c:
    rta = "El numero " + str(b) + " es mayor que " + str(a) + " y tambien es mayor que " + str(c)   

else:
    rta = "El numero " + str(c) + " es mayor que " + str(a) + " y tambien es mayor que " + str(b)


#output

print(input(rta))

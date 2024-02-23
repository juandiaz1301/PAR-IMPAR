# Programa para verificar si un numero es PAR o IMPAR

# input

x= int(input("Digite el valor de x: "))

# processing

r= x%2

if r==0:
    rta="par"
else:
    rta="impar"

# uotput

print ("El numero " + str(x) + " es " + rta)






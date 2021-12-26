numero= int(input("escriba el valor a descubir si es primo o no "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("este número no es primo" )
else:
  print("Este numero es primo")


"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
con = 0
naturales = []
while con < 100:
      con += 1
      naturales.append(con)
#print(naturales)

"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
con = 0
con1 = ''
acumulado = []
while con < 50:
      con += 1      
      con1 =  con1 + ' ' + str(con)
      acumulado.append(''.join(con1.lstrip())) 
#print(acumulado)

"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""
suma100 = 0
for elemento in naturales: 
    suma100 += elemento
#print(suma100)

"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
tabla100 = ''
con = 0
num = 134
while con < 10:
      con += 1 
      multi = con * num 
      tabla100 = tabla100 + str(multi) + ',' 
tabla100 =  tabla100.rstrip(",")
#print(tabla100)

"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

multiplos3=[]
for i in lista1:
  if i%3 == 0 and i < 300:
    multiplos3.append(i)
  i +=1
cuantos = len(multiplos3)
multiplos3 = int(cuantos)
#print(multiplos3)

"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""
contar = 0
con50 = ''
regresivo50 = []
while contar < 50:
      contar += 1      
      con50 =  str(contar) + ' ' +  con50
      regresivo50.append(''.join(con50.rstrip())) 
regresivo50.reverse()
#print(regresivo50)

"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
invertido = []
for i in range(66,-1,-5):
       invertido.append(i)

#print(invertido)

"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""
cont = 0
primos = []
for i in range(37, 300 + 1):
    primos1 = True
    for j in range(2,11):
        if i == j:
           break
        elif i%j == 0:
           primos1 = False
        else:
           continue
    if primos1 == True:
        primos.append(i)
        cont += 1
print(primos)
        
"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
fibonacci = []
a = 0
b = 1
contando = 0
while contando < 60:
    fibonacci.append(a)
    a, b = b, a+b
    contando += 1    
#print(fibonacci)

"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""

a = 30
def calculaFactorial(n):
  if n>0:
    n = n * calculaFactorial(n - 1)
  else:
    n = 1
  return n
factorial = calculaFactorial(a)
#print (factorial)


"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]

pares=[]
for i, elemento in enumerate(lista3):
  if i%2 ==0 and i<=80:
    pares.append(elemento)
  i +=1
#print(pares)

"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
cubos = []
val = 1

while val <= 100:
 cal = val**3
 cubos.append(cal)
 val +=1
#print(cubos)

"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""

n=1
i=1
serie = '2'
suma_2s = 0
while n <= 10:
  while i < n:
    serie += '2'
    i+=1
  suma_2s += int(serie)
  n +=1
#print(suma_2s)

"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""
 
v11 = '*'
contar = 1
while contar < 10:
  v12 =v11.ljust(contar,'*')
  contar +=1
  print(v12)







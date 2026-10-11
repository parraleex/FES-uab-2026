###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
print("Alex Moraleda Campaña")
print("Sabadell")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
cadena = "12345"
enter = int(cadena)
print(enter)
decimal = float(cadena)
print(decimal)
num = 3.99
num_enter = int(num)
print(num_enter)


print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí
nom = "Alex"
edat = 19
alçada = 1.83

print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alçada} metres.")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

PI = 3.1416
arrodonit = int(round(PI))
divisio = int(arrodonit / 2)
print(divisio)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
temp_c = float(input("Temperatura (en Celsius): "))
fahrenheit = ((temp_c * 9/5) + 32)
print(f"La temperatura en graus Celsius és: {temp_c}. En Fahrenheit és: {fahrenheit}")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
compte = float(input("Total del compte: "))
percentatge = float(input("Percentatge de propina: "))
propina = float((compte * percentatge) / 100)
print(f"El total del compte és de: {compte}€ i el percentatge de propina és del {percentatge} %")
print(f"La propina total a pagar és de {propina} €")


print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
contrasenya = str(input("Contrasenya: "))
if len(contrasenya) < 8:
    print("Contrasenya no vàlida")
else:
    print("Contrasenya vàlida")
###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
comptador = 10
while comptador >= 1:
    print(f"Numero {comptador}")
    comptador -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
comptador = 1
suma = 0
while comptador <= 20:
    if comptador % 2 == 0:
        suma += comptador
    elif comptador == 1:
        suma += comptador
    comptador += 1
print(f"La suma és de: {suma}")



# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
#numero = int(input("Introdueix un numero enter positiu: "))
#factorial = 1
#comptador = 1

#while comptador <= numero:
#    factorial = factorial * comptador # 1 * 1 --> 1 * 2 --> 2 * 3 ---> 6 * 4 --> 24 * 5
#    comptador += 1

#print(f"El factorial de {numero} és {factorial}")

numero = int(input("Numero: "))
comptador = numero - 1

while comptador >= 1:
    numero = numero * comptador
    comptador -= 1
print(f"El factorial es: {numero}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = ""
contrasenya = input("Introdueix una contrasenya: ")

while len(contrasenya) < 8:
    contrasenya = input("Contrasenya no vàlida. Torna a introduir: ")
    if len(contrasenya) > 8:
        print("Contrasenya vàlida")



# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero = int(input("Introdueix un numero: "))
comptador = 1
multiplicacio = 0

while comptador <= 10:
    multiplicacio = numero * comptador
    print(f"{numero} * {comptador} = {multiplicacio}")
    comptador += 1



# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

numero = int(input("Introdueix un numero: "))
comptador = 2

while comptador <= numero:
    es_primer = True
    divisor = 2
    while divisor < comptador:
        if comptador % divisor == 0:
            es_primer = False
            break
        divisor += 1
    if es_primer:
        print(comptador)
    comptador += 1

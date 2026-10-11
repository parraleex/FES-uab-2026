###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic = input("Nom tecnic: ")
nom_xarxa = input("Nom xarxa: ")
print(f"Tècninc: {nom_tecnic}; Xarxa: {nom_xarxa}")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
enllaç = float(input("Longitud (en km): "))
velocitat = float(input("Velocitat (en Gbps): "))
temps = 8.0 /velocitat
print(f"L'enllaç de {enllaç} km triga en transmetre 1 GB {temps} segons")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores = int(input("Hores de feina: "))
preu_hora = float(input("Preu per hora: "))
preu_material = float(input("Preu material: "))
total_hores = hores * preu_hora
total = total_hores + preu_material
print(f"El preu total de la instal·lació és de {total} €")
# -*- coding: utf-8 -*-

import sys
import re
sys.path.append(".")
from random import randint
from Player import Player
from Ship import Ship
from PrintFunctions import printMessage


###################### Validación del nombre ######################

sizeBoard = 0
player_name = ""
Ship_to_be_selected = ""
print("+"*60)
print("¡Bienvenido a Battleship rupestre!")
print("+"*60)

###################### Name Validation ######################

while player_name == "":
    player_name = input("Cual es tu nombre:").capitalize()
    if not bool(re.search(r"^[A-Za-z]{3,}$", player_name)):
        printMessage("\t \t Error: solo acepta más de 3 letras, no acepta algun otro caracter", delimiter = "- " * 40)
        player_name = ""
        
###################### Size board Validation ######################

while sizeBoard < 7 or sizeBoard > 14:
    try:
        printMessage("\t \t Definamos el tamaño del tablero, no puede ser menor a 7 ni mayor a 14", delimiter ="")
        sizeBoard = int(input("Ingrese el valor del tablero: "))
        if sizeBoard < 7 or sizeBoard > 14:
            printMessage("\t \t WARNING! = ¡Revisa las instrucciones!", delimiter="")
    except ValueError:
        printMessage("No se ha ingresado un número, vuelve a intentar")

###################### Assigning Coordinates ######################

printMessage(f"\t \t ¡Perfecto {player_name}! ahora definamos las reglas y las coordenadas donde quieres posicionar tus barcos", delimiter ="")

printMessage("= Reglas","= Puedes agregar los siguientes barcos:"
             ,"= \t \t a. 1 Barco Grande (ocupa 6 espacios)"
             ,"= \t \t b. 1 Barco Mediano (ocupa 4 posiciones)"
             ,"= \t \t c. 3 Barcos Pequeños (Ocupa 2 posiciones)"
             ,"="
             ,"= Deberas seleccionar cual barco quieres crear y en seguida que posiciones ira, solo se permite de manera Horizontal o vertical, no importa el orden en que los elijas "
             ,"="
             ,delimiter = "="*120
             )

#initializing object HumanPlayer and ship
HumanPlayer = Player(player_name,[],sizeBoard) 
AiPlayer = Player("Computadora",[],sizeBoard) 
ship_to_check = Ship()
count_ships = 0
# filling matriz with 0 values in each position
for i in range(sizeBoard):
   HumanPlayer.coordinates.append([0 for j in range(sizeBoard)]) # Creating our board
   AiPlayer.coordinates.append([0 for j in range(sizeBoard)]) # Creating Ai board


#Populating Human ship coordinates

printMessage("Cada valor de 0 es una posicion a la que puedes asignar una parte de cada barco")
printMessage("Tu tablero:")
printMessage(", ".join([chr(i) for i in range(65,65+sizeBoard)])) #Printing our board
printMessage(HumanPlayer.coordinates,delimiter=None,matrix=1)

while count_ships < 3:    
    Ship_to_be_selected = str(input("Cual Barco te gustaría utilizar:")).lower()
    printMessage("las coodenadas tienen que estar separadas con comas")
    printMessage(""*27+"x y")
    if Ship_to_be_selected in [ "a","b","c" ]:
        count_ships = count_ships + 1
        if ship_to_check.is_full(Ship_to_be_selected, HumanPlayer): #Checking if all positions had already been populated
            printMessage("las posiciones para ese barco ya fueron ingredadas, elige otro barco")
        else:
            while not ship_to_check.is_full(Ship_to_be_selected, HumanPlayer):
                HumanPlayer.input_coordinates(Ship_to_be_selected, sizeBoard)

#showing new board
printMessage("Tu tablero quedo de la siguiente manera:")
printMessage(HumanPlayer.coordinates,delimiter=None,matrix=1)
            

#Populating AI ship coordinates
AiPlayer.automatic_generation(sizeBoard)

bs={}
ms={}
ss={}
while True:
    shoot=input("Elige donde quieres dirigir tu misil:  ")
    if bool(re.search(rf"^[A-Za-z],[0-{sizeBoard}]$", shoot)):
        print("entre")
    if HumanPlayer.check_positions_taken(shoot.split(","),HumanPlayer.ship.big_ship):
        print("Big ship hit!!")
        (shoot.split(","),)
        HumanPlayer.ship.big_ship.popitem()
        if HumanPlayer.ship.big_ship=={}:
            print("Big Ship sunk!")
        print(bs)
    elif HumanPlayer.check_positions_taken(shoot.split(","),HumanPlayer.ship.medium_ship):
        print("Medium Ship hit!!")
    elif HumanPlayer.check_positions_taken(shoot.split(","),HumanPlayer.ship.small_ship):
        print("Small Ship hit!!")
    else:
        print("Miss ,Try again.")



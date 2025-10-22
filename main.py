#from core import game (es para arranca la lógica del juego)
from core.tool import clear
from story.menus import intro, mostrar_menu_personajes
from story.quest import prologo
from core.combat import combat
from characters.personajes import *

def main():
    opcion_menu_inicio = intro()

    if opcion_menu_inicio == 1: # 1. continuar
        pass
    elif opcion_menu_inicio == 2: # 2. nueva partida
        opcion_continua = prologo()
        clear()
    elif opcion_menu_inicio == 3: # 3. salir
        pass
    else:
        pass
    
    usuario = mostrar_menu_personajes()

    
    if usuario == 1:
        usuario = Caballero(vida=100, daño=20, nombre="Eldric")
    elif usuario == 2:
        usuario = Arquera()
    elif usuario == 3:
        usuario = Mago()
    

    enemigo = Zombi(vida=60, daño=15, nombre="Zombi Errante")

    combat(usuario, enemigo)

if __name__ == '__main__':
    main()
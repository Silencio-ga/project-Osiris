#from core import game (es para arranca la lógica del juego)
from core.tool import clear
from story.menus import intro, mostrar_menu_personajes
from story.quest import prologo
from core.combat import *
from characters.personajes import *

def main():
    while True:
        opcion_menu_inicio = intro()

        """
        if opcion_menu_inicio == 1: # 1. continuar
            pass
        elif opcion_menu_inicio == 2: # 2. nueva partida
            opcion_continua = prologo()
            clear()
        elif opcion_menu_inicio == 3: # 3. salir
            break
        """
        usuario = mostrar_menu_personajes()


        if usuario == 1:
            usuario = perso_caballero
        elif usuario == 2:
            usuario = perso_arquera
        elif usuario == 3:
            usuario = perso_mago

        combat(usuario, enem_zombi)
    """
    for i in range(2):
        print("Cierrando el progama.")
        print("Cierrando el progama..")
        print("Cierrando el progama...")
    """

if __name__ == '__main__':
    main()
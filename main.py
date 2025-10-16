#from core import game (es para arranca la lógica del juego)
from story.menus import intro
from story.quest import prologo

def main():
    opcion_menu_inicio = intro()

    if opcion_menu_inicio == 1: # 1. continuar
        pass
    elif opcion_menu_inicio == 2: # 2. nueva partida
        prologo()
    elif opcion_menu_inicio == 3: # 3. salir
        pass
    else:
        pass

if __name__ == '__main__':
    main()
#from core import game (es para arranca la lógica del juego)
from core.tool import clear, efect_central_text
from story.menus import intro, mostrar_menu_personajes, menu_universal
from story.quest import prologo, micro_historia
from core.combat import *
from characters.personajes import *
import sys, time


def main():
    while True:
        """
        opcion_menu_inicio = intro()

        
        if opcion_menu_inicio == 1: # 1. continuar
            pass
        elif opcion_menu_inicio == 2: # 2. nueva partida
            prologo()
            clear()
        elif opcion_menu_inicio == 3: # 3. salir
            clear()
            break
        """
        usuario = mostrar_menu_personajes() 

        if usuario == 1:
            usuario = perso_caballero
        elif usuario == 2:
            usuario = perso_arquera
        elif usuario == 3:
            usuario = perso_mago

        opcion_1_1, opcion_2_1, opcion_3_1 , resultado_1, resultado_2, resultado_3 = micro_historia(usuario)

        entrada = menu_universal("Elige un número: ",opcion_1_1, opcion_2_1, opcion_3_1)
        
        if entrada == 1:
            combat(usuario,Zombi(nombre="bandido")) # ivo tiene que hacer una corrección 
            entrada = input(center_text("apriete 'enter' para continuar"))
            clear()
            efect_center_block_gradual(resultado_1)
            entrada = input(center_text("apriete 'enter' para continuar"))
            if entrada == "":
                clear()
        elif entrada == 2:
            efect_center_block_gradual(resultado_2)
            entrada = input(center_text("apriete 'enter' para continuar"))
            if entrada == "":
                clear()
        elif entrada == 3:
            efect_center_block_gradual(resultado_3)
            entrada = input(center_text("apriete 'enter' para continuar"))
            if entrada == "":
                clear()

    for i in range(3):
        for dots in [".   🌑", "..  🌓", "... 🌕"]:
            sys.stdout.write(f"\rCerrando el programa{dots}")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\nListo. 👋")
    time.sleep(0.5)
    clear()



if __name__ == '__main__':
    main()
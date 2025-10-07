import os
import time
import shutil

# funcion para limpia terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# funcion para centra textos en horizontal
def center_text(text):
    cols = shutil.get_terminal_size().columns
    return text.center(cols)


# funcion de menu de inicio
def menu():
    
    tex_menu = [
        "Opciones:\n\n",
        "1. continuar \n",
        "2. nueva partida \n",
        "3. salir \n",
    ]

    max_len = max(len(linea) for linea in tex_menu)

    for linea in tex_menu:
        print(center_text(linea.ljust(max_len)))
    
    menu_opcion = int(input("Elige un numero:"))
    return menu_opcion


# funcion del titulo
def titulo():
    tex_titulo = [
        "░█████╗░░██████╗██╗██████╗░██╗░██████╗",
        "██╔══██╗██╔════╝██║██╔══██╗██║██╔════╝",
        "██║░░██║╚█████╗░██║██████╔╝██║╚█████╗░",
        "██║░░██║░╚═══██╗██║██╔══██╗██║░╚═══██╗",
        "╚█████╔╝██████╔╝██║██║░░██║██║██████╔╝",
        "░╚════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░\n\n",
    ]

    print("\n" * 2)
    for linea in tex_titulo:
        print(center_text(linea))
    



# funcion principal | intro del juego, con titulo y menu
def intro():
    titulo()
    opcion_num = menu()
    return opcion_num

from core.tool import *
import os, shutil, time

# ========================================
#   FUNCIONES DEL MENÚ PRINCIPAL Y TÍTULO
# ========================================

# funcion de menu de inicio
def mostrar_menu_inicio():
    tex_menu = """
Opciones:\n\n
1. continuar \n
2. nueva partida \n
3. salir \n
"""

    efect_center_block_gradual(tex_menu)
    
    while True:
        try:
            opcion_inicio = int(input(center_text("Elige un número: ")))
            if opcion_inicio in (1, 2, 3):
                return opcion_inicio
            print(center_text("Opción inválida. Intenta nuevamente."))
        
        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))


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
    clear()

    print("\n" * 2)
    for linea in tex_titulo:
        print(center_text(linea))
        time.sleep(0.07)
    print("\n" * 2)



# funcion principal | intro del juego, con titulo y menu
def intro():
    titulo()
    opcion = mostrar_menu_inicio()
    return opcion

# =============================================
#   FUNCIONES DEL MENÚ SELECCION DE PERSONAJE
# =============================================

def mostrar_menu_personajes():
    menu_personajes = """
Elige tu destino:\n
[1] Eldric, el Caballero Gris
    ➤ Honor y acero. Vive por su juramento roto.\n
[2] Lyra, la Arquera del Bosque Caído
    ➤ Precisión y sigilo. Sobrevive escuchando a los muertos.\n
[3] Kael, el Mago Desterrado
    ➤ Sabiduría y locura. Manipula la magia prohibida.\n
"""
    
    efect_center_block_gradual(menu_personajes)

    while True:
        try:
            opcion_personaje = int(input(center_text("Elige un número: ")))
            if opcion_personaje in (1, 2, 3):
                return opcion_personaje
            print(center_text("Opción inválida. Intenta nuevamente."))

        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))

# ================================
#   FUNCIONES DEL MENÚ DE COMBATE
# ================================


def mostrar_menu_combate():
    menu_combate = """
Elige una opcion:\n
[1] Atacar\n
[2] Habilidad especial\n
"""

    efect_center_block_gradual(menu_combate)

    while True:
        try:
            opcion_combate = int(input(center_text("Elige un número: ")))
            print(f"~{opcion_combate}~{type(opcion_combate)}")
            if opcion_combate in (1, 2):
                return opcion_combate
            print(center_text("Opción inválida. Intenta nuevamente."))
        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))

if __name__ == "__main__":
    mostrar_menu_combate()
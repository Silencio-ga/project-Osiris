from core.tool import clear, center_text, efect_central_text
import os, shutil, time

# ========================================
#   FUNCIONES DEL MENÚ PRINCIPAL Y TÍTULO
# ========================================

# funcion de menu de inicio
def mostrar_menu_inicio():
    
    tex_menu = [
        "Opciones:\n\n",
        "1. continuar \n",
        "2. nueva partida \n",
        "3. salir \n",
    ]

    max_len = max(len(linea) for linea in tex_menu)

    for linea in tex_menu:
        print(center_text(linea.ljust(max_len)))
    
    while True:
        try:
            opcion = int(input(center_text("Elige un número: ")))
            if opcion in (1, 2, 3):
                return opcion
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

if __name__ == "__main__":
    mostrar_menu_inicio()
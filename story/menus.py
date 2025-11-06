from core.tool import *
import os, shutil, time

# ========================================
#   FUNCIONES DEL MENÚ PRINCIPAL Y TÍTULO
# ========================================

# funcion de menu de inicio
def mostrar_menu_inicio(tmp=0.005):
    tex_menu = """
Opciones:\n\n
1. continuar \n
2. nueva partida \n
3. salir \n
"""

    efect_center_block_gradual(tex_menu,tmp)
    
    while True:
        try:
            opcion_inicio = int(input(center_text("Elige un número: ")))
            if opcion_inicio in (1, 2, 3):
                return opcion_inicio
            print(center_text("Opción inválida. Intenta nuevamente."))
        
        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))


# funcion del titulo
def titulo(tmp=0.07):
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
        time.sleep(tmp)
    print("\n" * 2)



# funcion principal | intro del juego, con titulo y menu
def intro():
    titulo(tmp=0.07)
    opcion = mostrar_menu_inicio()
    return opcion

# =============================================
#   FUNCIONES DEL MENÚ SELECCION DE PERSONAJE
# =============================================

def mostrar_menu_personajes(tmp=0.005):
    menu_personajes = """
Elige tu destino:\n
[1] Eldric, el Caballero Gris
    ➤ Honor y acero. Vive por su juramento roto.\n
"""

    guardado = """ # lo gurado para más adelante 
[2] Lyra, la Arquera del Bosque Caído
    ➤ Precisión y sigilo. Sobrevive escuchando a los muertos.\n
[3] Kael, el Mago Desterrado
    ➤ Sabiduría y locura. Manipula la magia prohibida.\n
"""
    
    efect_center_block_gradual(menu_personajes,tmp)

    while True:
        try:
            opcion_personaje = int(input(center_text("Elige un número: ")))
            if opcion_personaje == 1: # (1, 2, 3) LOS VALORES QUE TENIA
                return opcion_personaje
            print(center_text("Opción inválida. Intenta nuevamente."))

        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))

# ================================
#   FUNCIONES DEL MENÚ DE COMBATE
# ================================


def mostrar_menu_combate(tmp=0.005):
    menu_combate = """
Elige una opcion:\n
[1] Atacar\n
[2] Habilidad especial\n
"""

    efect_center_block_gradual(menu_combate,tmp)

    while True:
        try:
            opcion_combate = int(input(center_text("Elige un número: ")))
            if opcion_combate in (1, 2):
                return opcion_combate
            print(center_text("Opción inválida. Intenta nuevamente."))
        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))

# ================================
#   FUNCIONES DE MENÚ UNIVERSAL
# ================================

# funcion menu universal que mustra un menú centrado (título + opciones) como un bloque con efecto gradual
def menu_universal(titulo_menu, *opciones, tpm=0.005, tex_respuesta="Elige una opción: "):
    # Construir el bloque completo
    lineas = []
    # título en su propia línea(s)
    for t in str(titulo_menu).splitlines():
        lineas.append(t.strip())
    lineas.append("")  # línea en blanco entre título y opciones

    # Añadir opciones numeradas
    for i, opcion in enumerate(opciones, start=1):
        lineas.append(f"[{i}] {opcion}")

    bloque = "\n".join(lineas) + "\n"   # aseguramos salto al final si lo querés

    n = len(opciones)
    while True:
        efect_center_block_gradual(bloque, tpm) # Mostrar el bloque con efecto centrado
        entrada = input(center_text(tex_respuesta))
        clear()
        if entrada.isdigit(): # es para verifica que sea un numero
            num = int(entrada)
            if 1 <= num <= n:
                return num
        print(center_text("Opción inválida. Intenta de nuevo."))

"""
def mostrar_menu_opciones(opcion_1_1, opcion_2_1, opcion_3_1,tmp=0.005):
    menu_opciones = f
Elige una opcion: \n
[1] {opcion_1_1}
[2] {opcion_2_1}
[3] {opcion_3_1}

    efect_center_block_gradual(menu_opciones,tmp)

    while True:
        try:
            opcion = int(input(center_text("Elige un número: ")))
            if opcion_combate in (1, 2, 3):
                return opcion_combate
            print(center_text("Opción inválida. Intenta nuevamente."))
        except ValueError:
            print(center_text("Por favor, ingresa un número válido."))
"""
if __name__ == "__main__":
    mostrar_menu_combate()
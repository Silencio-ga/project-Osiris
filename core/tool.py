import shutil, time, os

# ===============
#   𝗧𝗢𝗢𝗟-𝗧𝗘𝗫𝗧
# ===============

# funcion para limpia terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# funcion para centra textos en horizontal
def center_text(text):
    cols = shutil.get_terminal_size().columns
    return text.center(cols)

# funcion para aparece el texto gradualmente 
def efect_text_gradual(text, tmp):
    for letra in text:
        print(letra, end="", flush=True)
        time.sleep(tmp)

# funcion para hacer lineas decorativas que ocupen toda la terminal
def linea_decorativa(caracter="-", borde="✦"):
    ancho = shutil.get_terminal_size().columns - 2
    return f"{borde}{caracter * ancho}{borde}"

# efecto graducal para aparece texto + center_text
def efect_central_text(text):
    lineas_centradas = [center_text(linea) for linea in text.splitlines()]
    texto_centrado = "\n".join(lineas_centradas)
    efect_text_gradual(texto_centrado, 0.01)

# funcion de bloque de texto centrado con efecto de escritura gradual
def efect_center_block_gradual(text, tmp=0.01):
    # calcula lo ancho de la terminal
    cols = shutil.get_terminal_size().columns
    # separa linea por linea el texto y lo guarda en lista
    lineas = text.splitlines()
    # calcula la linea más larga
    max_len = max(len(linea) for linea in lineas) if lineas else 0
    # calcula 
    margen_izq = max((cols - max_len) // 2, 0)

    # recorremos cada línea y aplicamos el efecto gradual centrado
    for linea in lineas:
        linea_centrada = " " * margen_izq + linea
        for letra in linea_centrada:
            print(letra, end="", flush=True)
            time.sleep(tmp)
        print()
    if text.endswith("\n"):
        print()

# funcion de titulo entre lineas decorativas
def titulo_lineas_decorativa(titulo,lineas="𓂃",tmp=0.01):
    titulo_combat = [linea_decorativa(lineas), center_text(titulo), linea_decorativa(lineas)]

    renglon1 = ""
    renglon2 = ""
    renglon3 = ""

    # imprime el renglon1, 2 y 3 a la vez
    total = len(titulo_combat[0])
    for i in range(total):
        renglon1 += titulo_combat[0][i]
        renglon2 += titulo_combat[1][i]
        renglon3 += titulo_combat[2][i]
        print(f"{renglon1}\n{renglon2}\n{renglon3}")
        time.sleep(tmp)
        if i < total - 1:
            clear()

def menu_univesal(can_opciones,*valores):
    for valores in range(can_opciones):
        menu_opciones = f"{can}"

# --------

# =================
#   𝗧𝗢𝗢𝗟-𝗟𝗢𝗚𝗜𝗖𝗔
# =================

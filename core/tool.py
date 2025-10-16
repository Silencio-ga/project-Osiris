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
def efect_text_gradual(texto, tmp):
    for letra in texto:
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

# --------

# =================
#   𝗧𝗢𝗢𝗟-𝗟𝗢𝗚𝗜𝗖𝗔
# =================

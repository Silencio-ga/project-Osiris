import shutil, time, os

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
def efect_central_text(text, tmp):
    lineas_centradas = [center_text(linea) for linea in text.splitlines()]
    texto_centrado = "\n".join(lineas_centradas)
    efect_text_gradual(texto_centrado, tmp)
    return texto_centrado

# funcion de bloque de texto centrado con efecto de escritura gradual
def efect_center_block_gradual(text, delay=0.01):

    cols = shutil.get_terminal_size().columns
    lineas = text.splitlines()
    max_len = max(len(linea) for linea in lineas) if lineas else 0
    margen_izq = max((cols - max_len) // 2, 0)

    # recorremos cada línea y aplicamos el efecto gradual centrado
    for linea in lineas:
        linea_centrada = " " * margen_izq + linea
        for letra in linea_centrada:
            print(letra, end="", flush=True)
            time.sleep(delay)
        print()
    if text.endswith("\n"):
        print()




# ==========================================

def prologo():
    titulo_prologo = [linea_decorativa("𓂃"), center_text("₊⋆✧ P R O J E C T   O S I R I S ✧⋆⁺"), linea_decorativa("𓂃")]

    renglon1 = ""
    renglon2 = ""
    renglon3 = ""

    # imprime el renglon1, 2 y 3 a la vez
    total = len(titulo_prologo[0])
    for i in range(total):
        renglon1 += titulo_prologo[0][i]
        renglon2 += titulo_prologo[1][i]
        renglon3 += titulo_prologo[2][i]
        print(f"{renglon1}\n{renglon2}\n{renglon3}")
        time.sleep(0.01)
        if i < total - 1:
            clear()

    tex_prologo = f"""
Dicen que el mundo se partió en silencio...\n
Nadie recuerda cuándo ocurrió, solo que el cielo se volvió ciego y el viento comenzó a hablar en lenguas antiguas.
Eldara, el corazón de los hombres, aún respiraba entonces: sus torres rozaban los dioses, y su rey,
ansioso por tocar lo eterno, descendió donde ningún nombre debía ser pronunciado.
Buscó el poder en las entrañas del mundo… y el mundo lo escuchó.\n
No fue fuego ni guerra lo que acabó con Eldara, sino una plegaria contestada.
El rey abrió las puertas de algo que no comprendió —una grieta en la forma misma del alma— y de allí surgió 
la Niebla sin eco, que marchitó la carne, quebró los sueños y dobló los rezos hacia adentro.
Los dioses callaron. Los muertos recordaron.\n
Ahora, las ruinas del reino aún laten, envueltas en un amanecer que nunca llega.
Las campanas tocan solas, las sombras murmuran nombres olvidados, y en las criptas, el aire huele a memoria.
El Abismo no duerme: observa, respira, espera.\n
Algunos aún caminan entre sus cicatrices, arrastrando su cordura, buscando respuestas que nadie pidió.
No son héroes, ni salvadores.\n
Son los ecos de un mundo que intenta olvidarse a sí mismo...
"""
    efect_center_block_gradual(tex_prologo)
    opcion_continua = input(center_text("Aprete 'enter' para continua: "))

prologo()
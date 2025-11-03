from core.tool import *
import time

# ==============
# P R O L O G O
# ==============

# funcion para hacer el prologo
def prologo():
    titulo_lineas_decorativa("₊⋆✧ P R Ó L O G O ✧⋆⁺",tmp=0.005)

    tex_prologo = f"""
Dicen que el mundo se partió en silencio.
Nadie recuerda cuándo ocurrió, solo que el cielo se volvió ciego y el viento comenzó a hablar en lenguas antiguas.
Eldara, el corazón de los hombres, aún respiraba entonces: sus torres rozaban los dioses, y su rey, 
ansioso por tocar lo eterno, descendió donde ningún nombre debía ser pronunciado.
Buscó el poder en las entrañas del mundo… y el mundo lo escuchó.

No fue fuego ni guerra lo que acabó con Eldara, sino una plegaria contestada.
El rey abrió las puertas de algo que no comprendió —una grieta en la forma misma del alma— y de allí surgió 
la Niebla sin eco, que marchitó la carne, quebró los sueños y dobló los rezos hacia adentro.
Los dioses callaron. Los muertos recordaron.

Ahora, las ruinas del reino aún laten, envueltas en un amanecer que nunca llega.
Las campanas tocan solas, las sombras murmuran nombres olvidados, y en las criptas, el aire huele a memoria.
El Abismo no duerme: observa, respira, espera.

Algunos aún caminan entre sus cicatrices, arrastrando su cordura, buscando respuestas que nadie pidió.
No son héroes, ni salvadores.
Son los ecos de un mundo que intenta olvidarse a sí mismo.
"""
    efect_center_block_gradual(tex_prologo,tmp=0.005)
    opcion_continua = input(center_text("Aprete 'enter' para continua: "))


# ================
# MICRO-HISTORIAS
# ================

# Historia 
def micro_historia(historia):
    pass
from story.menus import mostrar_menu_combate
from core.tool import clear, linea_decorativa, center_text
from characters.personajes import *
import random, time

#sistema de combate bien pro

def combat(jugador, enemigo):

    clear()
    titulo_combat = [linea_decorativa("𓂃"), center_text("¡Comienza la batalla!"), linea_decorativa("𓂃")]
    
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
        time.sleep(0.01)
        if i < total - 1:
            clear()

    turno = 1
    
    #empieza el turno del jugador
    while jugador.vida > 0 and enemigo.vida > 0:
        print(center_text(f"--- Turno {turno} ---"))
        print(f"{jugador.nombre} HP: {jugador.vida}")
        print(f"{enemigo.tipo} HP: {enemigo.daño}\n")

        # menu de acciones
        while True:
            opcion_combate = mostrar_menu_combate()
            
            if opcion_combate == 1:
                print(f"\n{jugador.nombre} ataca a {enemigo.nombre} causando {jugador.daño} de daño!")
                enemigo.recibir_daño(jugador.daño, jugador.tipo)
            elif opcion_combate == 2:
                jugador.habilidad_especial(enemigo)
            else:
                print(" Opcion invalida. Inténtalo de nuevo.\n")

        # verificar si el enemigo murió
        if enemigo.vida <= 0:
            efect_center_block_gradual(f"\n{enemigo.nombre} ha sido derrotado.\n¡Has ganado la batalla!")
            break

        # turno del enemigo
        time.sleep(1)
        print(f"\n{enemigo.nombre} contraataca causando {enemigo.daño} de daño.")
        jugador.recibir_daño(enemigo.daño, enemigo.tipo)

        if jugador.vida <= 0:
            efect_center_block_gradual(f"\n{jugador.nombre} ha caído en batalla...\nEl {enemigo.tipo} prevalece.")
            break

        turno += 1

# fin del combate

    if jugador.vida > 0:
        print(f"\n{jugador.nombre} ganó la batalla contra el {enemigo.tipo}!")
        oro_ganado = random.randint(5, 25)
        xp_ganada = random.randint(10, 40)

        print(f"Oro ganado: {oro_ganado} | XP ganada: {xp_ganada}")
        
        return {"oro": oro_ganado, "xp": xp_ganada}
    else:
        print(f"\n{jugador.nombre} cayó en combate...")
        return {"oro": 0, "xp": 0}

# habilidades de los personajes va a ir aca 

def usar_habilidad_especial(jugador, enemigo):
    clase = jugador.__class__.__name__.lower()

#caballero
    if clase == "caballero":
        print(f"\n{jugador.nombre} usa su escudo reduciendo el daño del próximo ataque a la mitad.")

        enemigo.atk //= 2
#arquero
    elif clase == "arquero":
        daño_total = jugador.daño * 3
        print(f"\n {jugador.nombre} lanza una ráfaga de flechas causando {daño_total} de daño.")
        enemigo.hp -= daño_total
        if enemigo.hp <= 0:
            enemigo.muerto = True
            print(f"{enemigo.tipo} ha sido derrotado.")

#mago

    elif clase == "mago":
        daño_magico = jugador.daño * 2 + 5
        print(f"\n{jugador.nombre} lanza una bola de fuego causando {daño_magico} de daño.")
        enemigo.hp -= daño_magico
        if enemigo.hp <= 0:
            enemigo.muerto = True
            print(f"{enemigo.tipo} fue reducido a cenizas.")

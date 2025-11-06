from story.menus import mostrar_menu_combate
from core.tool import clear, center_text, titulo_lineas_decorativa, efect_center_block_gradual
from characters.personajes import *
import random, time

# ==============================
# CARACTERISTICAS DE PERSONAJES
# ==============================

# === aliados ===
perso_caballero = Caballero(vida=100, daño=20, nombre="Eldric")
perso_arquera = Arquera(vida=60,daño=40,nombre="Lyra")
perso_mago = Mago(vida=80,daño=30,nombre="Kael")

# === enemigos ===
enem_zombi = Zombi(vida=80,daño=20)
enem_esqueleto = Esqueleto(vida=60, daño=30)

# ===============================
# SISTEMA DE COMBATE BIEN PRO!!!
# ===============================

# funcion para pelea
def combat(jugador, enemigo):

    clear()
    titulo_lineas_decorativa("C O M B A T E",tmp=0.005)
    turno = 1
    
    while jugador.vida > 0 and enemigo.vida > 0:
        clear()
        print(center_text(f"--- Turno {turno} ---"))
        print(f"{jugador.nombre} HP: {jugador.vida} | {enemigo.nombre} HP: {enemigo.vida}\n")

        opcion = mostrar_menu_combate()
      
      # acción del jugador
        if opcion == 1:
            print(f"\n{jugador.nombre} ataca causando {jugador.daño} de daño!")
            enemigo.recibir_daño(jugador.daño, jugador.nombre)
        elif opcion == 2:
            jugador.habilidad_especial(enemigo)
        else:
            print("Opcion invalida. Se pierde el turno.")
            time.sleep(1)
        
        #turno del enemigo 

        time.sleep(1)
        print(f"\n{enemigo.nombre} contraataca causando {enemigo.daño} de daño.")
        jugador.recibir_daño(enemigo.daño, enemigo.nombre)

        # verificar si el jugador murio
        if jugador.vida <= 0:
            efect_center_block_gradual(f"\n{jugador.nombre} ha caído en batalla...\nEl {enemigo.nombre} prevalece.")
            break

        turno += 1
        time.sleep(1)

# fin del combate

    if jugador.vida > 0:
        print(f"\n{jugador.nombre} ganó la batalla contra el {enemigo.nombre}!")
        oro_ganado = random.randint(5, 25)
        xp_ganada = random.randint(10, 40)

        print(f"Oro ganado: {oro_ganado} | XP ganada: {xp_ganada}")
        
        return {"oro": oro_ganado, "xp": xp_ganada}
    else:
        print(f"\n{jugador.nombre} cayó en combate...")
        return {"oro": 0, "xp": 0} 


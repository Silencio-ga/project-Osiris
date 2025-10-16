import random

#sistema de combate bien pro

def combat(jugador, enemigo): 
    print(f"\n comienza la batalla! te ataca un {enemigo.tipo}\n")
    #empieza el turno del jugador

    turno = 1
    while jugador.vida > 0 and enemigo.hp > 0:
        print(f"--- Turno {turno} ---")
        print(f"{jugador.nombre} HP: {jugador.vida}")
        print(f"{enemigo.tipo} HP: {enemigo.hp}\n")

        # menu de eleccion
        while True:
            print("1️⃣  Atacar")
            print("2️⃣  Habilidad especial\n")
            accion = input("Elige una opción (1 o 2): ")

            if accion == "1":
                daño = jugador.daño  # daño fijo que elija el marcos
                print(f"\n{jugador.nombre} ataca causando {daño} de daño a {enemigo.tipo}.")
                enemigo.hp -= daño
                if enemigo.hp <= 0:
                    enemigo.muerto = True
                    print(f"{enemigo.tipo} ha sido derrotado.")
                break

            elif accion == "2":
                usar_habilidad_especial(jugador, enemigo)
                break

            else:
                print(" Opcion invalida. Inténtalo de nuevo.\n")


        # turno del enemigo
        if not enemigo.muerto:
            daño_enemigo = enemigo.atk
            print(f"\n{enemigo.tipo} ataca infligiendo {daño_enemigo} puntos de daño.")
            jugador.vida -= daño_enemigo

            if jugador.vida <= 0:
                jugador.vida = 0
                jugador.vivo = False
                print(f"{jugador.nombre} fue derrotado por el {enemigo.tipo}.")

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

# NO esta terminado todavia
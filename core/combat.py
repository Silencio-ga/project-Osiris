import random

#sistema de combate bien pro

def combat(player, enemy): 
    print(f"\n comienza la batalla! te ataca un {enemy["nombre"]}\n")
    #empieza el turno del jugador

    while player["hp"] > 0 and enemy["hp"] > 0:
        print(f"HP del Jugador: {player["hp"]} | HP del enemigo: {enemy["hp"]}")
        action = input("Atacar o defenderse? ").lower()

        if action == "atacar":
            damage = random.randint(player["ataque"] - 2, player["attac"] + 2)
            print(f"Atacas y dañas al enemigo por {damage} puntos de daño!")
            enemy["hp"] -= damage 
        elif action == "defenderse": 
            print("Te preparas para defenderte y reduces el daño en un 50%.")
        else:
            print("Esa accion no funciona y pierdes tu turno.")

        if enemy["hp"] <= 0:
            print(f"\n Derrotaste a {enemy["nombre"]}!")
            return "Victoria asegurada!"
        
    #turno del enemigo 

        damage_enemy = random.randint(enemy["ataque"] - 1, enemy["ataque"] + 2)
        if action == "defenderse":
            damage_enemy //= 2
        player["hp"] -= damage_enemy
        print(f"{enemy["nombre"]} te ataca e inflige {damage_enemy} de daño. \n")

    if player["hp"] <=0:
        print("Fuiste derrotado por {enemy["nombre"]}.")
        return "derrota"
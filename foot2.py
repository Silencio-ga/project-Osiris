import os, time, random, shutil

# ==========================================
# ============== TOOL-TEXT =================
# ==========================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def center_text(text):
    cols = shutil.get_terminal_size().columns
    return text.center(cols)

def efect_text_gradual(text, delay=0.01):
    for letra in text:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()

def efect_center_block_gradual(text, delay=0.01):
    """Muestra un bloque centrado con efecto de escritura."""
    cols = shutil.get_terminal_size().columns
    lineas = text.splitlines()
    max_len = max((len(l) for l in lineas), default=0)
    margen = max((cols - max_len) // 2, 0)
    for linea in lineas:
        print(" " * margen, end="")
        for letra in linea:
            print(letra, end="", flush=True)
            time.sleep(delay)
        print()
    if text.endswith("\n"):
        print()

# ==========================================
# ============== PERSONAJES ================
# ==========================================

class Entidad:
    def __init__(self, vida, daño, nombre, tipo=None):
        self.vida = vida
        self.daño = daño
        self.nombre = nombre
        self.tipo = tipo or self.__class__.__name__

    def recibir_daño(self, daño, tipo):
        self.vida -= daño
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"{self.nombre} recibe {daño} puntos de daño. Vida restante: {self.vida}")

# ====== Clases de personajes ======
class Caballero(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Caballero")

    def habilidad_especial(self, enemigo):
        print(f"{self.nombre} levanta su escudo y contraataca con furia sagrada!")
        daño_extra = self.daño + 10
        enemigo.recibir_daño(daño_extra, self.tipo)

class Arquera(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Arquera")

    def habilidad_especial(self, enemigo):
        print(f"{self.nombre} dispara una lluvia de flechas precisas!")
        daño_extra = self.daño + random.randint(5, 15)
        enemigo.recibir_daño(daño_extra, self.tipo)

class Mago(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Mago")

    def habilidad_especial(self, enemigo):
        print(f"{self.nombre} lanza un hechizo devastador!")
        daño_extra = self.daño * 2
        enemigo.recibir_daño(daño_extra, self.tipo)

# ====== Clases de enemigos ======
class Zombi(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Zombi")

class Esqueleto(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Esqueleto")

class Demonio(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Demonio")

# ==========================================
# ============== COMBATE ===================
# ==========================================

def combat(jugador, enemigo):
    clear()
    efect_center_block_gradual(f"¡Comienza la batalla!\nTe enfrentas a un {enemigo.tipo} llamado {enemigo.nombre}.\n")

    turno = 1
    while jugador.vida > 0 and enemigo.vida > 0:
        print(center_text(f"\n--- Turno {turno} ---"))
        print(center_text(f"{jugador.nombre}: {jugador.vida} HP"))
        print(center_text(f"{enemigo.nombre}: {enemigo.vida} HP\n"))

        # Menú de acciones
        print(center_text("[1] Atacar"))
        print(center_text("[2] Habilidad especial"))
        print()
        opcion = input(center_text("Elige una acción: "))

        if opcion == "1":
            print(f"\n{jugador.nombre} ataca a {enemigo.nombre} causando {jugador.daño} de daño!")
            enemigo.recibir_daño(jugador.daño, jugador.tipo)
        elif opcion == "2":
            jugador.habilidad_especial(enemigo)
        else:
            print("Opción inválida. Pierdes el turno.")

        # Verificar si el enemigo murió
        if enemigo.vida <= 0:
            efect_center_block_gradual(f"\n{enemigo.nombre} ha sido derrotado.\n¡Has ganado la batalla!")
            break

        # Turno enemigo
        time.sleep(1)
        print(f"\n{enemigo.nombre} contraataca causando {enemigo.daño} de daño.")
        jugador.recibir_daño(enemigo.daño, enemigo.tipo)

        if jugador.vida <= 0:
            efect_center_block_gradual(f"\n{jugador.nombre} ha caído en batalla...\nEl {enemigo.tipo} prevalece.")
            break

        turno += 1

# ==========================================
# ============== EJECUCIÓN =================
# ==========================================

if __name__ == "__main__":
    jugador = Caballero(vida=100, daño=20, nombre="Eldric")
    enemigo = Zombi(vida=60, daño=15, nombre="Zombi Errante")

    combat(jugador, enemigo)

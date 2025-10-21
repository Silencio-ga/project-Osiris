import shutil, time, os, random


# ===============
#   TOOL-TEXT
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
def efect_center_block_gradual(text, delay=0.01):
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
            time.sleep(delay)
        print()
    if text.endswith("\n"):
        print()

# ==============================================
#   OBJETOS ENTIDAD Y DECLARACION DE PERSONAJES
# ==============================================

# clase madre que tiene todos los personajes
class Entidad:
    def __init__(self,vida:int, nombre:str)->None:
        self.vida = vida
        self.vida_max = vida
        self.vivo= True
        self.nombre = nombre
        self.daño = 0
        self.oro = 0
        self.tipo = self.__class__.__name__ # guarda el tipo de enemigo(zombi,esqueleto)

    # funcion para recibir daño
    def recibir_daño(self, nombre, tipo)->None: #funcion de como reciben daño los personajes
        self.vida -= self.daño
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            print (f"{self.nombre} Murió")
        else:
            print(f"{self.nombre} recibió daño de {Enemigo.tipo}\n Vida restante: {self.vida}")
    
    # funcion para causa daño
    def atacar(self, objetivo):
        daño_infligido = self.daño
        vida -= daño_infligido
        print (f"{self.nombre} ataca a {Enemigo.tipo}")
        print (f"{Enemigo.tipo} recibe {daño_infligido} de daño")

# hija de entidad, objeto caballero
class Caballero(Entidad):
    def __init__(self,vida, daño,)->None:
        super().__init__(vida, daño)
        self.def_escudo = 30
    # funcion del caballero, habilidad curbirse escudo 
    def recibir_daño(self)->None: 
        daño_reducido= max(0, Enemigo.daño - self.def_escudo)
        print(f"{Entidad.nombre} bloquea {self.def_escudo} de daño con su escudo")
        super().recibir_daño(daño_reducido)

# hija de entidad, objeto arquero
class Arquero(Entidad):
    def __init__(self,vida,daño,nombre)->None:
        super().__init__(vida, daño, nombre)

    # funcion de la arquera, habilidad ataque con flechas
    def usar_ráfaga_de_flechas(self): 
        cantidad_de_flechas = random.randint(1,5)
        daño_ráfaga = self.daño * cantidad_de_flechas
        print(f"{self.nombre} dispara {cantidad_de_flechas} flechas a {Enemigo.tipo} causando {daño_ráfaga}")
        Enemigo.recibir_daño(daño_ráfaga)

# hija de entidad, objeto mago
class Mago(Entidad):

    # El mago causa daño expansivo
    def __init__(self,vida,nombre,daño)->None:
        super().__init__(vida,nombre,daño)

    # funcion del mago, habilidad bola de juego
    def bola_de_fuego(self)->None: 
        print(f"Mago lanza una bola de fuego a {Enemigo.tipo}")
        Enemigo.recibir_daño(self.daño*len(Grupo_enemigo))


#===========================
#       Clase Enemgio
#===========================

class Enemigo(Entidad):
    def __init__(self, vida, daño):
        super().__init__(vida, daño)

class Esqueleto(Entidad):
    def __init__(self,vida,daño):
        super().__init__(vida, daño)

class Zombi(Entidad):
    def __init__(self,vida,daño):
        super().__init__(vida, daño)

class Grupo_enemigo: 
    def __init__(self,max_esq=3, max_zb=2):
        self.g1 = self.grupo_aleatorio(max_esq,max_zb)
        self.g2 = self.grupo_aleatorio(max_esq,max_zb)
        self.g3 = self.grupo_aleatorio(max_esq,max_zb)
        self.g4 = self.grupo_aleatorio(max_esq,max_zb)
        self.g5 = self.grupo_aleatorio(max_esq,max_zb)
    
    def grupo_aleatorio(self,max_esq,max_zb): #esta funcion crea grupos de enemigos
        num_esqueletos = random.randint(1, max_esq)
        num_zombis = random.randint(1,max_zb)
        lista_esq = [Esqueleto() for _ in range(num_esqueletos)]
        lista_zb = [Zombi() for _ in range(num_zombis)]
        grupo_en = lista_esq + lista_zb
        random.shuffle(grupo_en)
        return grupo_en
    
    def mostrar_grupo(self,num_grupos): #función que muestra 
        grupo_en = getattr(self,f"g{num_grupos}")
        print (f"\n--- El {num_grupos} esta conformado por {len(grupo_en)} enemigos")
        for i, enemigos in enumerate(grupo_en,1):
            print (f"{i}:{Enemigo.tipo} |HP: {Enemigo.vida} | ATK: {Enemigo.daño}")

# ===================
#   BUCLE DE COMBATE
# ===================

def combat(jugador, enemigo): 
    print(f"\n comienza la batalla! te ataca un {enemigo}\n")
    #empieza el turno del jugador

    turno = 1
    
    jugador.defensa_activa = False
    while jugador.vida > 0 and enemigo.hp > 0:
        print(f"--- Turno {turno} ---")
        print(f"{jugador.nombre} HP: {jugador.vida}")
        print(f"{enemigo.tipo} HP: {enemigo.hp}\n")

        # menu de eleccion
        while True:
            opcion_combate = mostrar_menu_combate()

            if opcion_combate == "1":
                daño = jugador.daño  # daño fijo que elija el marcos
                print(f"\n{jugador.nombre} ataca causando {daño} de daño a {enemigo.tipo}.")
                enemigo.hp -= daño
                if enemigo.hp <= 0:
                    enemigo.muerto = True
                    print(f"{enemigo.tipo} ha sido derrotado.")
                break

            elif opcion_combate == "2":
                usar_habilidad_especial(jugador, enemigo)
                break

            else:
                print(" opcion invalida. Inténtalo de nuevo.\n")


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

combat(Caballero, Zombi)
import  random
from enemy import Enemigo
from enemy import Grupo_enemigo
class Personaje:
    def __init__(self,vida:int, nombre:str)->None:
        self.vida = vida
        self.vida_max = vida
        self.vivo= True
        self.nombre = nombre
        self.daño = 0
    

    def recibir_daño(self)->None: #esto es la funcion de como reciben daño los personajes
        vida -= Enemigo.atk
        if vida <= 0:
            self.vida = 0
            self.vivo = False
            print (f"{self.nombre} Murió")
        else:
            print(f"{self.nombre} recibió daño de {Enemigo.tipo}\n Vida restante: {self.vida}")
        
    def atacar(self):
        daño_infligido = self.daño
        Enemigo.hp -= daño_infligido
        print (f"{self.nombre} ataca a {Enemigo.tipo}")
        print (f"{Enemigo.tipo} recibe {daño_infligido} de daño")

class Fisico(Personaje): #Esta es la clase que divide los personajes con daño magico de los de daño fisico
    def __init__(self,vida, daño, nombre)->None:
        super().__init__(vida, nombre, daño)
        self.daño = daño
            
class Caballero(Fisico):
    def __init__(self,vida, daño,)->None:
        super().__init__(vida, daño)
        self.def_escudo = 30
        
    def recibir_daño(self)->None:
        daño_reducido= max(0, Enemigo.atk - self.def_escudo)
        print(f"{Personaje.nombre} bloquea {self.def_escudo} de daño con su escudo")
        super().recibir_daño(daño_reducido)


class Arquero(Fisico):
    def __init__(self,vida,daño,nombre)->None:
        super().__init__(vida, daño, nombre)

    def usar_ráfaga_de_flechas(self):
        cantidad_de_flechas = random.randint(1,5)
        daño_ráfaga = self.daño * cantidad_de_flechas
        print(f"{self.nombre} dispara {cantidad_de_flechas} flechas a {Enemigo.tipo} causando {daño_ráfaga}")
        Enemigo.recibir_daño_enemigo(daño_ráfaga)

class Mago(Personaje):
    def __init__(self,vida,nombre,daño)->None:
        super().__init__(vida,nombre,daño)
    def bola_de_fuego(self)->None:
        print(f"Mago lanza una bola de fuego a {Enemigo.tipo}")
        Enemigo.recibir_daño_enemigos(self.daño_magico*len(Grupo_enemigo))


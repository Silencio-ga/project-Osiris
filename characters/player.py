import  random
from enemy import enemigos
from enemy import grupo_enemigos
class Personaje:
    def __init__(self,vida:int, nombre:str, clase:str)->None:
        self.vida = vida
        self.vida_max = vida
        self.vivo= True
        self.nombre = nombre
        self.clase = clase
        self.daño = 0
    

    def recibir_daño(self)->None: #esto es la funcion de como reciben daño los personajes
        vida -= enemigos.atk
        if vida <= 0:
            self.vida = 0
            self.vivo = False
            print (f"{self.nombre} Murió")
        else:
            print(f"{self.nombre} recibió daño de {enemigos.tipo}\n Vida restante: {self.vida}")
        
class Fisico(Personaje): #Esta es la clase que divide los personajes con daño magico de los de daño fisico
    def __init__(self,vida:int, daño_fisico:int, nombre:str)->None:
        super().__init__(vida, nombre)
        self.daño = daño_fisico
            
class Caballero(Fisico):
    def __init__(self,clase = "Caballero")->None:
        super().__init__(vida=1000, daño_fisico=120, nombre="Eldric")
        self.def_escudo = 30
        
    def recibir_daño(self)->None:
        daño_reducido= max(0, enemigos.atk - self.def_escudo)
        print(f"{player} bloquea {self.def_escudo} de daño con su escudo")
        super().recibir_daño(daño_reducido)


class Arquero(Fisico):
    def __init__(self,clase="arquera")->None:
        super().__init__(vida=700, daño_fisico=150, nombre="Lyra")

    def usar_ráfaga_de_flechas(self):
        cantidad_de_flechas = random.randint(1,5)
        daño_ráfaga = self.daño_fisico * cantidad_de_flechas
        print(f"{self.nombre} dispara {cantidad_de_flechas} flechas a {enemigos.tipo} causando {daño_ráfaga}")
        enemigos.recibir_daño_enemigos(daño_ráfaga)

class Mago(Personaje):
    def __init__(self,clase= "Mago")->None:
        super().__init__(vida=500,nombre="Kael")
        self.daño_magico= 130
        self.daño = self.daño_magico
        
    def bola_de_fuego(self)->None:
        print(f"Mago lanza una bola de fuego a {enemigos.tipo}")
        enemigos.recibir_daño_enemigos(self.daño_magico*len(grupo_enemigos))


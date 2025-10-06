import  random 
class personajes:
    def __init__(self,vida=int)->None:
        vida= vida

    def recibir_daño(self): #esto es la funcion de como reciben daño los personajes
        vida -= daño_ememigo
        if vida < 0:
            vida = 0
        print(f"{personaje} recibe {daño_enemigo} de {enemigo}")

    def vivo(self, vida):
            return vida > 0
        
class fisicos(personajes): #Esta es la clase que divide los personajes con daño magico de los de daño fisico
    def __init__(self)->None:
        daño_fisico= daño_fisico
            
class caballero(fisicos):
    def __init__(self)->None:
        super().__init__(vida, daño_fisico)
        def_escudo = 30
        daño_fisico = 120
        vida = 1000

    def recibir_daño(self, daño_enemigo):
        daño_reducido= max(0, daño_enemigo, self.def_escudo)
        print(f"{personaje} bloquea {self.def_escudo} de daño con su escudo")
        super().recibir_daño(daño_reducido)

class arquero(fisicos):
    def __init__(self, vida, daño_fisico, daño_rafaga)->None:
        super().__init__(vida, daño_fisico)
        vida = 700
        daño_fisico = 150
        daño_rafaga = daño_fisico * random.randint(1, 4)

    def usar_ráfaga_de_flechas(self,enemigo):
        print(f"Arquero lanza una ráfaga de flechas sobre {enemigo}")
        enemigo.recibir_daño(self.daño_rafaga)

class mago(personajes):
    def __init__(self, vida, daño_magico)->None:
        super().__init__(vida)
        vida = 500
        daño_magico= 130
        
    def bola_de_fuego(self, enemigo)->None:
        print(f"Mago lanza una bola de fuego a {enemigo}")
        enemigo.recibir_daño(daño_magico*num_enemigos)


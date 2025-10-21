import  random

class Entidad:
    def __init__(self,vida:int, nombre:str)->None:
        self.vida = vida
        self.vida_max = vida
        self.vivo= True
        self.nombre = nombre
        self.daño = 0
        self.oro = 0
        self.tipo = self.__class__.__name__ # guarda el tipo de enemigo(zombi,esqueleto)

    def recibir_daño(self, nombre, tipo)->None: #funcion de como reciben daño los personajes
        self.vida -= self.daño
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            print (f"{self.nombre} Murió")
        else:
            print(f"{self.nombre} recibió daño de {Enemigo.tipo}\n Vida restante: {self.vida}")
        
    def atacar(self, objetivo):
        daño_infligido = self.daño
        vida -= daño_infligido
        print (f"{self.nombre} ataca a {Enemigo.tipo}")
        print (f"{Enemigo.tipo} recibe {daño_infligido} de daño")

            
class Caballero(Entidad):
    def __init__(self,vida, daño,)->None:
        super().__init__(vida, daño)
        self.def_escudo = 30
        
    def recibir_daño(self)->None: #función de cubrirse con el escudo del caballero
        daño_reducido= max(0, Enemigo.daño - self.def_escudo)
        print(f"{Entidad.nombre} bloquea {self.def_escudo} de daño con su escudo")
        super().recibir_daño(daño_reducido)


class Arquero(Entidad):
    def __init__(self,vida,daño,nombre)->None:
        super().__init__(vida, daño, nombre)

    def usar_ráfaga_de_flechas(self): #función de habilidad especial del arquero
        cantidad_de_flechas = random.randint(1,5)
        daño_ráfaga = self.daño * cantidad_de_flechas
        print(f"{self.nombre} dispara {cantidad_de_flechas} flechas a {Enemigo.tipo} causando {daño_ráfaga}")
        Enemigo.recibir_daño(daño_ráfaga)

class Mago(Entidad):
    def __init__(self,vida,nombre,daño)->None:
        super().__init__(vida,nombre,daño)
    def bola_de_fuego(self)->None: #función de habilidad especial del mago
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

hordas= Grupo_enemigo()
hordas.mostrar_grupo(2)
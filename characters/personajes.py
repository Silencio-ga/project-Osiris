import  random

class Entidad:
    def __init__(self,vida:int, daño:int, nombre:str, tipo: str = None)->None:
        self.vida = vida
        self.daño = daño
        self.nombre = nombre
        self.tipo = tipo or self.__class__.__name__ # guarda el tipo de enemigo(zombi,esqueleto)

    def recibir_daño(self, nombre, tipo)->None: #funcion de como reciben daño los personajes
        self.vida -= self.daño
        if self.vida <= 0:
            self.vida = 0
            print (f"{self.nombre} Murió")
        else:
            print(f"{self.nombre} recibió daño de {self.tipo}\n Vida restante: {self.vida}")
        
    def atacar(self):
        daño_infligido = self.daño
        vida -= daño_infligido
        print (f"{self.nombre} ataca a {self.tipo}")
        print (f"{self.tipo} recibe {daño_infligido} de daño")

#===========================
#       Clase personajes
#===========================

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


#===========================
#       Clase Enemgios
#===========================

class Zombi(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Zombi")

class Esqueleto(Entidad):
    def __init__(self, vida, daño, nombre):
        super().__init__(vida, daño, nombre, tipo="Esqueleto")

"""
class Grupo_enemigo: 
    def __init__(self,max_esq=3, max_zb=2):
        self.g1 = self.grupo_aleatorio(max_esq,max_zb)
        self.g2 = self.grupo_aleatorio(max_esq,max_zb)
        self.g3 = self.grupo_aleatorio(max_esq,max_zb)
        self.g4 = self.grupo_aleatorio(max_esq,max_zb)
        self.g5 = self.grupo_aleatorio(max_esq,max_zb)
    
    def grupo_aleatorio(self,max_esq,max_zb): #esta funcion crea grupos de enemigos
        grupo_en = []
        num_esqueletos = random.randint(1, max_esq)
        num_zombis = random.randint(0,max_zb)
        for i in range(num_esqueletos):
            grupo_en.append(Esqueleto(f"Esqueleto{i+1}",vida=30, daño=30))
        for i in range(num_zombis):
            grupo_en.append(Zombi(f"Zombi{i+1} ",vida=40, daño=15   ))
        random.shuffle(grupo_en)
        return grupo_en
    
    def mostrar_grupo(self,num_grupos): #función que muestra el grupo de enemigos
        grupo_en = getattr(self,f"g{num_grupos}")
        print (f"\n--- El {num_grupos} esta conformado por {len(grupo_en)} enemigos")
        for i, enemigos in enumerate(grupo_en,1):
            print (f"{i}:{Enemigo.tipo} |VIDA: {Enemigo.vida} | DAÑO: {Enemigo.daño}")

hordas= Grupo_enemigo()
hordas.mostrar_grupo(2)
"""
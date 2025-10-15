import random
from heroes import Personaje
class Enemigo:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
        self.tipo = self.__class__.__name__ #esto guarda el tipo de enemigo(zombi,esqueleto)
        self.muerto = False
    
    def Recibir_daño_enemigo(self,daño,hp):
        hp -= daño
        if hp <= 0:
            self.hp = 0
            self.muerto = True
            print (f"{Personaje.nombre} derrotaste a {Enemigo.tipo}")
        else:
            print (f"{Enemigo.tipo} recibió {Personaje.daño} de {Personaje.nombre}")  

    def ataque_enemigo(self):
        daño_infligido1 = self.atk
        Personaje.vida -= daño_infligido1
        print (f"{Enemigo.tipo} ataca a {Personaje.nombre}")
        print (f"{Personaje.nombre} recibe {daño_infligido1} de daño")      

class Esqueleto(Enemigo):
    def __init__(self,hp,atk):
        super().__init__(hp, atk)

class Zombi(Enemigo):
    def __init__(self,hp,atk):
        super().__init__(hp, atk)

class Grupo_enemigo:
    def __init__(self,max_esq=3, max_zb=2):
        self.g1 = self.grupo_aleatorio(max_esq,max_zb)
        self.g2 = self.grupo_aleatorio(max_esq,max_zb)
        self.g3 = self.grupo_aleatorio(max_esq,max_zb)
        self.g4 = self.grupo_aleatorio(max_esq,max_zb)
        self.g5 = self.grupo_aleatorio(max_esq,max_zb)
    
    def grupo_aleatorio(self,max_esq,max_zb):
        num_esqueletos = random.randint(1, max_esq)
        num_zombis = random.randint(1,max_zb)
        lista_esq = [Esqueleto() for _ in range(num_esqueletos)]
        lista_zb = [Zombi() for _ in range(num_zombis)]
        grupo_en = lista_esq + lista_zb
        random.shuffle(grupo_en)
        return grupo_en
    
    def mostrar_grupo(self,num_grupos):
        grupo_en = getattr(self,f"g{num_grupos}")
        print (f"\n--- El {num_grupos} esta conformado por {len(grupo_en)} enemigos")
        for i, enemigos in enumerate(grupo_en,1):
            print (f"{i}:{Enemigo.tipo} |HP: {Enemigo.hp} | ATK: {Enemigo.atk}")
hordas= Grupo_enemigo()
hordas.mostrar_grupo(2)

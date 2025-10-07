import random

class enemigos:
    def __init__(self,hp, atk):
        self.hp = hp
        self.atk = atk
        self.tipo = self.__class__.__name__ #esto guarda el tipo de enemigo(zombi,esqueleto)

class esqueleto(enemigos):
    def __init__(self):
        super().__init__(hp=250, atk=40)

class zombi(enemigos):
    def __init__(self):
        super().__init__(hp=190, atk=80)

class grupo_enemigos:
    def __init__(self,max_esq=3, max_zb=2):
        self.g1 = self.grupo_aleatorio(max_esq,max_zb)
        self.g2 = self.grupo_aleatorio(max_esq,max_zb)
        self.g3 = self.grupo_aleatorio(max_esq,max_zb)
        self.g4 = self.grupo_aleatorio(max_esq,max_zb)
        self.g5 = self.grupo_aleatorio(max_esq,max_zb)
    
    def grupo_aleatorio(self,max_esq,max_zb):
        num_esqueletos = random.randint(1, max_esq)
        num_zombis = random.randint(1,max_zb)
        lista_esq = [esqueleto() for _ in range(num_esqueletos)]
        lista_zb = [zombi() for _ in range(num_zombis)]
        grupo_en = lista_esq + lista_zb
        random.shuffle(grupo_en)
        return grupo_en
    
    def mostrar_grupo(self,num_grupos):
        grupo_en = getattr(self,f"g{num_grupos}")
        print (f"\n--- El {num_grupos} esta conformado por {len(grupo_en)} enemigos")
        for i, enemigos in enumerate(grupo_en,1):
            print (f"{i}:{enemigos.tipo} |HP: {enemigos.hp} | ATK: {enemigos.atk}")
hordas= grupo_enemigos()
hordas.mostrar_grupo(2)

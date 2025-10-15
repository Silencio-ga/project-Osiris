from heroes import Personaje


class NPC:
    def __init__(self,nombre):
        self.nombre = nombre


class Comerciante(NPC):
    def __init__(self, inventario_comerciante):
        self.nombre = "Roberto"
        self.espadas = {
            "Espada de Acero" :40,
            "Espada de Acero maldito": 60,
            "Espada de Bruxamantino": 90,
            "Espada del Dios del inframundo": 120
        }
        self.arcos = {
            "Arco de Madera dura": 40,
            "Arco de Elfos": 60,
            "Arco Maldito": 90,
            "Arco de Arbol del mundo": 120
        }
        self.bastones = {
            "Baston torcido":40,
            "Baston maldito": 60,
            "Baston oscuro": 90,
            "Baston de almas": 120
        }
        self.pociones = {
            "Poción de Salud": 15,
            "Poción de Fuerza": 20,
        }

        self.inventario_comerciante = {
            "Espadas": self.espadas,
            "Pociones":self.pociones,
            "Arcos": self.arcos,
            "Bastones": self.bastones
        }

    def mostrar_inventario_comerciante(inventario_comerciante):
        print (f"\nHola soy {Comerciante.nombre}. ¿Que estas buscando?")
        while True:
            




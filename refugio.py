from typing import Literal

from animal import Gato, Raton


class Refugio:
    def __init__(self, tipo, calidad: Literal[1, 2, 3, 4, 5]):
        self.tipo = tipo
        self.calidad = calidad  # Por ejemplo, puede ser un valor entre 1 y 10

    def proporcionar_refugio(self, animal: Gato | Raton, calidad=2):
        """El animal se recupera en el refugio."""
        self.calidad -= 1
        animal.refugiarse = 1
        print(f"{animal.nombre} se refugia en un {self.tipo}.")
        animal.recuperarse(calidad)

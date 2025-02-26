from typing import Literal

from animal import Gato, Raton


class Comida:
    def __init__(self, tipo: Literal["pescado", "queso"], cantidad):
        self.tipo = tipo
        self.cantidad = cantidad

    def consumir(self, animal: Gato | Raton, cantidad=2):
        """Permite que el animal consuma la comida y se recupere."""
        if self.cantidad < cantidad:
            cantidad = self.cantidad
            print("Solo quedaba ", cantidad, "de", self.tipo)
        elif self.cantidad >= cantidad:
            self.cantidad -= cantidad
        elif self.cantidad <= 0:
            print("No queda comida")
            return

        if self.tipo == "pescado" and isinstance(animal, Gato):
            animal.recuperarse(self.cantidad)
            print(f"{animal.nombre} consume {self.tipo} y se cura.")
        elif self.tipo == "queso" and isinstance(animal, Raton):
            animal.recuperarse(self.cantidad)
            print(f"{animal.nombre} consume {self.tipo} y se cura.")
        else:
            print(f"{animal.nombre} no puede comer esta comida.")

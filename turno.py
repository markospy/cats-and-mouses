from collections import deque
from random import choice, uniform
from typing import Literal

from animal import Gato, Raton
from comida import Comida
from refugio import Refugio

CANT_ACCIONES = 1


class Turno:

    def __init__(self, gato: Gato, raton: Raton, comida_gato: Comida, comida_raton: Comida, refugio: Refugio):
        self.gato = gato
        self.raton = raton
        self.comida_gato = comida_gato
        self.comida_raton = comida_raton
        self.refugio = refugio
        self.pila_gato = deque()  # Pila de acciones del gato
        self.pila_raton = deque()  # Pila de acciones del ratón
        self._turno = 0  # Numero de turno

    def cambiar_turno(self):
        """Cambia el turno al siguiente jugador."""
        self.jugador = "raton" if self.jugador == "gato" else "gato"

    def compilar_acciones(
        self,
        acciones_gato: Literal["atacar", "esconderser", "alimentarse"],
        acciones_raton: Literal["atacar", "esquivar", "esconderser", "alimentarse"],
    ):
        """
        Compila las acciones de ambos jugadores para el turno.
        Las acciones son listas con 3 movimientos posibles: "recuperarse", "atacar", "esquivar"
        """
        self.pila_gato = deque(acciones_gato)
        self.pila_raton = deque(acciones_raton)

    def resolver_turno(self):
        """
        Resuelve el turno de ambos jugadores según las acciones compiladas.
        Compara y resuelve los 3 pares de acciones.
        """
        self._turno += 1
        for i in range(CANT_ACCIONES):
            # Sacamos las acciones de cada pila
            accion_gato = self.pila_gato.popleft()
            accion_raton = self.pila_raton.popleft()

            print(
                f"Turno {i + 1}:\n (Gato) {self.gato.nombre} realiza '{accion_gato}'\n(Raton) {self.raton.nombre} realiza '{accion_raton}'"
            )

            if accion_gato == "atacar" and accion_raton == "esquivar":
                if not self.raton.esquivar(self.gato):
                    self.gato.atacar(self.raton)

            if accion_gato == "atacar" and accion_raton == "atacar":
                animal = choice(["gato", "raton"])
                if animal == "gato":
                    self.raton.atacar(self.gato, uniform(0.5, 1))
                    self.gato.atacar(self.raton, uniform(0, 0.5))
                else:
                    self.gato.atacar(self.raton, uniform(0.5, 1))
                    self.raton.atacar(self.gato, uniform(0, 0.5))

            elif accion_raton == "esconderser":
                self.refugio.proporcionar_refugio(self.raton)

            elif accion_raton == "alimentarse":
                self.comida_raton.consumir(self.raton)

            elif accion_gato == "esconderser":
                self.refugio.proporcionar_refugio(self.gato)

            elif accion_gato == "alimentarse":
                self.comida_gato.consumir(self.gato)

            if self.raton.vida <= 0:
                print(f"¡El raton {self.raton.nombre} ha muerto! ¡El gato {self.pila_ratongato.nombre} gana!")
                break

            if self.gato.vida <= 0:
                print(f"¡El gato {self.gato.nombre} ha muerto! ¡El ratón {self.raton.nombre} gana!")
                break

        if self.raton.vida > 0 and self.gato.vida > 0:
            print("El turno ha terminado sin que nadie haya muerto.")

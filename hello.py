import time
from random import randint

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import ValidationError, Validator

from animal import Gato, Raton
from comida import Comida
from refugio import Refugio
from turno import Turno

CANT_ACCIONES = 1


class OptionValidator(Validator):
    def validate(self, document):
        text = document.text

        if text not in ["atacar", "esconderser", "alimentarse"]:

            raise ValidationError(
                message="Esta opcion no existe: escoge 'atacar', 'alimentarse', 'esconderse'",
                cursor_position=0,
            )


def main():
    print("Hello from Cats and Mouses!")

    # Crear instancias de Gato y Raton
    gato = Gato(nombre="Tom", vida=100, fuerza=20, defensa=20, agilidad=50)
    raton = Raton(nombre="Jerry", vida=100, fuerza=20, defensa=20, inteligencia=50)

    # Crear instancias de Comida para el gato y el ratón
    comida_gato = Comida(tipo="pescado", cantidad=randint(5, 10))
    comida_raton = Comida(tipo="queso", cantidad=randint(5, 10))

    # Crear instancia de Refugio
    refugio = Refugio(tipo="cueva", calidad=randint(5, 10))

    # Crear instancia de Turno
    turno = Turno(gato=gato, raton=raton, comida_gato=comida_gato, comida_raton=comida_raton, refugio=refugio)

    # Definir las acciones disponibles
    acciones_disponibles = WordCompleter(["atacar", "esconderser", "alimentarse"])

    # Bucle para manejar múltiples turnos
    while gato.vida > 0 and raton.vida > 0:
        print(f"\nTurno {turno._turno + 1}\n")
        print(
            f"\tGato {gato.nombre}:\n\t\tVida: {gato.vida}\n\t\tFuerza: {gato.fuerza}\n\t\tDefensa: {gato.defensa}\n\t\tAgilidad: {gato.agilidad}\n"
        )
        print(
            f"\tRaton {raton.nombre}:\n\t\tVida: {raton.vida}\n\t\tFuerza: {raton.fuerza}\n\t\tDefensa: {raton.defensa}\n\t\tInteligencia: {raton.inteligencia}"
        )

        # Solicitar acciones para el gato
        print(f"\nAcciones para {gato.nombre} (Gato):")
        acciones_gato = []
        for i in range(CANT_ACCIONES):
            accion = prompt(
                f"'atacar', 'esconderser', 'alimentarse'\nAcción {i + 1}: ",
                completer=acciones_disponibles,
                validator=OptionValidator(),
                validate_while_typing=False,
            )
            acciones_gato.append(accion)

        # Solicitar acciones para el ratón
        print(f"\nAcciones para {raton.nombre} (Ratón):")
        acciones_raton = []
        for i in range(CANT_ACCIONES):
            accion = prompt(
                f"'atacar', 'alimentarse', 'esconderse'\nAcción {i + 1}: ",
                completer=acciones_disponibles,
                validator=OptionValidator(),
                validate_while_typing=False,
            )
            acciones_raton.append(accion)

        # Compilar las acciones en el turno
        turno.compilar_acciones(acciones_gato, acciones_raton)

        # Resolver el turno
        turno.resolver_turno()
        time.sleep(20)


if __name__ == "__main__":
    main()

import time
from random import choice, randint

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
    gato = Gato(nombre="Tom", vida=100, fuerza=20, defensa=20, vitalidad=100, agilidad=50)
    raton = Raton(nombre="Jerry", vida=100, fuerza=20, defensa=20, vitalidad=100, inteligencia=50)

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
            f"\t🐱 Gato {gato.nombre}:\n\t\t❤️Vida: {gato.vida}\n\t\t💪Fuerza: {gato.fuerza}\n\t\t🛡️Defensa: {gato.defensa}\n\t\t💨Agilidad: {gato.agilidad}\n\t\t🔋Vitalidad: {gato.vitalidad}\n\t\t🐟Comida: {comida_gato.cantidad}\n\t\t🕳️Refugio: {refugio.calidad}"
        )
        print(
            f"\t🐭 Raton {raton.nombre}:\n\t\t❤️Vida: {raton.vida}\n\t\t💪Fuerza: {raton.fuerza}\n\t\t🛡️Defensa: {raton.defensa}\n\t\t👁️‍🗨️Inteligencia: {raton.inteligencia}\n\t\t🔋Vitalidad: {raton.vitalidad}\n\t\t🧀Comida: {comida_raton.cantidad}\n\t\t🕳️Refugio: {refugio.calidad}"
        )

        animal = choice(["gato", "raton"])
        if animal == "gato":
            # Solicitar acciones para el gato
            print(f"\nAcciones para {gato.nombre} (Gato) 🐱:")
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
            print(f"\nAcciones para {raton.nombre} (Ratón) 🐭:")
            acciones_raton = []
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"'atacar', 'alimentarse', 'esconderse'\nAcción {i + 1}: ",
                    completer=acciones_disponibles,
                    validator=OptionValidator(),
                    validate_while_typing=False,
                )
                acciones_raton.append(accion)

        else:
            # Solicitar acciones para el ratón
            print(f"\nAcciones para {raton.nombre} (Ratón) 🐭:")
            acciones_raton = []
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"'atacar', 'alimentarse', 'esconderse'\nAcción {i + 1}: ",
                    completer=acciones_disponibles,
                    validator=OptionValidator(),
                    validate_while_typing=False,
                )
                acciones_raton.append(accion)

            # Solicitar acciones para el gato
            print(f"\nAcciones para {gato.nombre} (Gato) 🐱:")
            acciones_gato = []
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"'atacar', 'esconderser', 'alimentarse'\nAcción {i + 1}: ",
                    completer=acciones_disponibles,
                    validator=OptionValidator(),
                    validate_while_typing=False,
                )
                acciones_gato.append(accion)

        # Compilar las acciones en el turno
        turno.compilar_acciones(acciones_gato, acciones_raton)

        # Resolver el turno
        turno.resolver_turno()
        time.sleep(10)


if __name__ == "__main__":
    main()

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

        if text not in ["atacar", "esconderse", "alimentarse"]:

            raise ValidationError(
                message="Esta opcion no existe: escoge 'atacar', 'alimentarse', 'esconderse'",
                cursor_position=0,
            )


def main():
    print("Hello from Cats and Mouses!")

    # Crear instancias de Gato y Raton
    gato = Gato(nombre="Tom", vida=100, fuerza=20, defensa=20, vitalidad=100, agilidad=50, alimentarse=0, refugiarse=0)
    raton = Raton(
        nombre="Jerry", vida=100, fuerza=20, defensa=20, vitalidad=100, inteligencia=50, alimentarse=0, refugiarse=0
    )

    # Crear instancias de Comida para el gato y el ratón
    comida_gato = Comida(tipo="pescado", cantidad=randint(1, 5))
    comida_raton = Comida(tipo="queso", cantidad=randint(1, 5))

    # Crear instancia de Refugio
    refugio = Refugio(tipo="cueva", calidad=randint(3, 5))

    # Crear instancia de Turno
    turno = Turno(gato=gato, raton=raton, comida_gato=comida_gato, comida_raton=comida_raton, refugio=refugio)

    # Definir las acciones disponibles
    acciones = ["atacar", "esconderse", "alimentarse"]

    # Bucle para manejar múltiples turnos
    while gato.vida > 0 and raton.vida > 0:
        print(f"\nTurno {turno._turno + 1}\n")
        print(
            f"\t🐱 Gato {gato.nombre}:\n\t\t❤️Vida: {gato.vida}\n\t\t💪Fuerza: {gato.fuerza}\n\t\t🛡️Defensa: {gato.defensa}\n\t\t🔋Vitalidad: {gato.vitalidad}\n\t\t💨Agilidad: {gato.agilidad}\n\t\t🐟Comida: {comida_gato.cantidad} - Puede?: {gato.alimentarse==0}\n\t\t🕳️Refugio: {refugio.calidad} - Puede?: {gato.refugiarse==0}"
        )
        print(
            f"\t🐭 Raton {raton.nombre}:\n\t\t❤️Vida: {raton.vida}\n\t\t💪Fuerza: {raton.fuerza}\n\t\t🛡️Defensa: {raton.defensa}\n\t\t🔋Vitalidad: {raton.vitalidad}\n\t\t👁️‍🗨️Inteligencia: {raton.inteligencia}\n\t\t🧀Comida: {comida_raton.cantidad} - Puede?: {raton.alimentarse==0}\n\t\t🕳️Refugio: {refugio.calidad} - Puede?: {raton.refugiarse==0}"
        )

        animal = choice(["gato", "raton"])
        if animal == "gato":
            # Solicitar acciones para el gato
            print(f"\nAcciones para {gato.nombre} (Gato) 🐱:")
            acciones_gato = []
            acciones_disponibles = acciones.copy()
            if gato.alimentarse != 0 or comida_gato.cantidad <= 0:
                acciones_disponibles.remove("alimentarse")
            if gato.refugiarse != 0 or refugio.calidad <= 0:
                acciones_disponibles.remove("esconderse")
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"{acciones_disponibles} \nAcción {i + 1}: ",
                    completer=WordCompleter(acciones_disponibles),
                    validator=OptionValidator(),
                    validate_while_typing=False,
                )
                acciones_gato.append(accion)

            # Solicitar acciones para el ratón
            print(f"\nAcciones para {raton.nombre} (Ratón) 🐭:")
            acciones_raton = []
            acciones_disponibles = acciones.copy()
            if raton.alimentarse != 0 or comida_raton.cantidad <= 0:
                acciones_disponibles.remove("alimentarse")
            if raton.refugiarse != 0 or refugio.calidad <= 0:
                acciones_disponibles.remove("esconderse")
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"{acciones_disponibles} \nAcción {i + 1}: ",
                    completer=WordCompleter(acciones_disponibles),
                    validator=OptionValidator(),
                    validate_while_typing=False,
                )
                acciones_raton.append(accion)

        else:
            # Solicitar acciones para el ratón
            print(f"\nAcciones para {raton.nombre} (Ratón) 🐭:")
            acciones_raton = []
            acciones_disponibles = acciones.copy()
            if raton.alimentarse != 0 or comida_raton.cantidad <= 0:
                acciones_disponibles.remove("alimentarse")
            if raton.refugiarse != 0 or refugio.calidad <= 0:
                acciones_disponibles.remove("esconderse")
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"{acciones_disponibles} \nAcción {i + 1}: ",
                    completer=WordCompleter(acciones_disponibles),
                    validator=OptionValidator(),
                    validate_while_typing=False,
                )
                acciones_raton.append(accion)

            # Solicitar acciones para el gato
            print(f"\nAcciones para {gato.nombre} (Gato) 🐱:")
            acciones_gato = []
            acciones_disponibles = acciones.copy()
            if gato.alimentarse != 0 or comida_gato.cantidad <= 0:
                acciones_disponibles.remove("alimentarse")
            if gato.refugiarse != 0 or refugio.calidad <= 0:
                acciones_disponibles.remove("esconderse")
            for i in range(CANT_ACCIONES):
                accion = prompt(
                    f"{acciones_disponibles} \nAcción {i + 1}: ",
                    completer=WordCompleter(acciones_disponibles),
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

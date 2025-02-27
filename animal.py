from random import random


class Animal:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa

    def atacar(self, otro_animal):
        """Realiza un ataque a otro animal."""
        danio = self.fuerza - otro_animal.defensa
        if danio > 0:
            otro_animal.vida -= danio
            print(f"🩸 {self.nombre} ataca a {otro_animal.nombre} causando {danio} puntos de daño.")
        else:
            print(f"⚔️ {self.nombre} intenta atacar a {otro_animal.nombre}, pero no hace daño.")

    def defender(self, factor):
        """Defenderse de un ataque, reduce daño."""
        self.defensa += factor * 0.05
        print(f"🛡️ {self.nombre} se defiende, aumentando su defensa.")

    def muerto(self):
        """Verifica si el animal está muerto."""
        if self.vida <= 0:
            return True
        else:
            return False


class Gato(Animal):
    def __init__(self, nombre, vida, fuerza, defensa, agilidad):
        super().__init__(nombre, vida, fuerza, defensa)
        self.agilidad = agilidad

    def atacar(self, raton: "Raton", factor: float):
        """Realiza un ataque a otro animal."""
        if self.muerto():
            return
        danio = (self.fuerza + self.agilidad - raton.defensa) * factor
        if danio > 0:
            raton.vida -= danio
            if raton.defensa > 10:
                raton.defensa -= 5 * factor
            else:
                raton.vida -= 5 * factor
            if raton.fuerza > 10:
                raton.fuerza -= 5 * factor
            else:
                raton.vida -= 5 * factor
            if raton.inteligencia > 10:
                raton.inteligencia -= 5 * factor
            else:
                raton.vida -= 5 * factor
            if self.agilidad < 100:
                self.agilidad += 5 * factor
            if self.fuerza < 100:
                self.fuerza += 5 * factor
            print(f"🩸 {self.nombre} ataca a {raton.nombre} causando {danio} puntos de daño.")
            raton.defender(danio)
        else:
            print(f"⚔️ {self.nombre} intenta atacar a {raton.nombre}, pero no hace daño.")
            self.agilidad -= 1

    def recuperarse(self, factor):
        """Propiedad de recuperacion del animal. Depende de un factor externo: comida o refugio"""
        if self.vida < 100:
            self.vida += factor * 10
        if self.fuerza < 100:
            self.fuerza += factor * 5
        if self.defensa < 100:
            self.defensa += factor * 3
        if self.agilidad > 10:
            self.agilidad -= factor * 1


class Raton(Animal):
    def __init__(self, nombre, vida, fuerza, defensa, inteligencia):
        super().__init__(nombre, vida, fuerza, defensa)
        self.inteligencia = inteligencia

    def atacar(self, gato: Gato, factor: float):
        if self.muerto():
            return
        """Ataque evasivo para el ratón."""
        danio = (self.fuerza + self.inteligencia - gato.defensa) * factor
        if danio > 0:
            gato.vida -= danio
            if gato.agilidad > 10:
                gato.agilidad -= 5 * factor
            else:
                gato.vida -= 5 * factor
            if gato.defensa > 10:
                gato.defensa -= 5 * factor
            else:
                gato.vida -= 5 * factor
            if self.fuerza < 100:
                self.fuerza += 5 * factor
            print(f"🩸 {self.nombre} (Raton) ataca a {gato.nombre} causando {danio} puntos de daño.")
            gato.defender(danio)
        else:
            print(f"⚔️ {self.nombre} (Raton) intenta atacar a {gato.nombre}, pero no hace daño.")

    def esquivar(self, gato: Gato):
        """El ratón puede intentar esquivar un ataque de un gato."""
        esquivar_probabilidad = self.inteligencia * random()  # A mayor inteligencia, mayor posibilidad de esquivar
        if esquivar_probabilidad > gato.agilidad / 100:
            print(f"🪖 {self.nombre} (Raton) esquiva el ataque de {gato.nombre}")
            if self.inteligencia < 100:
                self.inteligencia += 1
            return True
        print(
            f"🩹 {self.nombre} (Raton) intenta esquivar con una probabilidad de {esquivar_probabilidad * 100}%. pero falla"
        )
        return False

    def recuperarse(self, factor):
        """Propiedad de recuperacion del animal. Depende de un factor externo: comida o refugio"""
        if self.vida < 100:
            self.vida += factor * 10
        if self.fuerza < 100:
            self.fuerza += factor * 5
        if self.defensa < 100:
            self.defensa += factor * 3
        if self.inteligencia > 10:
            self.inteligencia -= factor * 3

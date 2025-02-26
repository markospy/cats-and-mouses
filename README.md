# Documentación del Juego: **Cats and Mouses**
# 🐱 ⚔️ 🐭
---

## **Para Jugadores**

### **Descripción del Juego**
"Cats and Mouses" es un juego de estrategia por turnos en el que un gato y un ratón compiten por sobrevivir. El objetivo del gato es cazar al ratón, mientras que el ratón debe esquivar al gato y sobrevivir el mayor tiempo posible. Ambos jugadores pueden realizar acciones como atacar, esconderse, alimentarse o recuperarse para mejorar sus estadísticas y ganar ventaja.

### **Reglas del Juego**
1. **Turnos**: El juego se divide en turnos. En cada turno, tanto el gato como el ratón eligen una acción para realizar.
2. **Acciones Disponibles**:
   - **Atacar**: El gato o el ratón intentan atacar al otro. El daño depende de la fuerza del atacante y la defensa del defenso, así de la inteligencia en el raton y la agilidad en el gato.
   - **Esconderse**: El animal se refugia en un refugio, lo que le permite recuperar vida y otras estadísticas. La calidad del refugio disminuye con cada uso.
   - **Alimentarse**: El animal consume comida para recuperar vida y otras estadísticas. La cantidad de comida disminuye con cada uso.
   - **Recuperarse**: El animal se recupera cuando se esconde o alimenta, aumentando su vida, fuerza, defensa y otras estadísticas y disminuye otras, la inteligencia en el raton y la agilidad en el gato. Así qu eno abuses😌.
3. **Condiciones de Victoria**:
   - El gato gana si reduce la vida del ratón a 0.
   - El ratón gana si reduce la vida del gato a 0.
4. **Recursos Limitados**:
   - **Comida**: La comida es limitada y se consume al alimentarse. Si no hay comida, no se puede realizar esta acción.
   - **Refugio**: El refugio tiene una calidad limitada que disminuye con cada uso. Si la calidad llega a 0, no se puede usar más.
   - La cantida de comida de cada animal y la calidad del refugio es un valor aleatorio de 1 a 10 que se genera al iniciar el juego. La calidad del refugio no es independiente en cada animal. Así que es lo primero que se debería usar antes de que el adversario lo gaste.
5. **Estadísticas**:
   - **Vida**: Si la vida llega a 0, el animal muere.
   - **Fuerza**: Afecta el daño causado al atacar.
   - **Defensa**: Reduce el daño recibido al ser atacado.
   - **Agilidad (Gato)**: Aumenta la probabilidad de esquivar ataques y afecta el daño causado.
   - **Inteligencia (Ratón)**: Aumenta la probabilidad de esquivar ataques y afecta el daño causado.

### **Cómo Jugar**
1. Al inicio del juego, se muestran las estadísticas del gato y el ratón.
2. En cada turno, el jugador elige una acción para el gato y otra para el ratón.
3. Las acciones se resuelven en orden, y los resultados se muestran en pantalla.
4. El juego continúa hasta que uno de los animales muere.

---

## **Para Desarrolladores**

### **Características Técnicas**
1. **Estructura del Proyecto**:
   - **`animal.py`**: Contiene las clases base `Animal`, `Gato` y `Raton`. Define las estadísticas y acciones básicas de los animales.
   - **`comida.py`**: Define la clase `Comida`, que maneja la lógica de consumo de comida y sus efectos en los animales.
   - **`refugio.py`**: Define la clase `Refugio`, que maneja la lógica de recuperación en el refugio.
   - **`turno.py`**: Contiene la clase `Turno`, que gestiona la lógica de los turnos y la resolución de acciones.
   - **`hello.py`**: Es el punto de entrada del juego. Contiene la lógica principal del juego y la interacción con el usuario.

2. **Lógica del Juego**:
   - **Turnos**: El juego se maneja por turnos, donde cada jugador elige una acción para su animal.
   - **Acciones**: Las acciones se resuelven en función de las estadísticas de los animales y las condiciones del juego (calidad del refugio, cantidad de comida, etc.).
   - **Aleatoriedad**: Se utiliza aleatoriedad en ciertas acciones, como el daño causado, la probabilidad de esquivar, la cantidad de comida y calidad del refugio.

3. **Interacción con el Usuario**:
   - Se utiliza la librería `prompt_toolkit` para manejar la entrada de acciones de manera interactiva.
   - Se valida que las acciones ingresadas por el usuario sean válidas.

4. **Extensibilidad**:
   - El código está diseñado para ser fácilmente extensible. Se pueden agregar nuevas acciones, animales o mecánicas de juego sin afectar la estructura existente.

### **Cómo Contribuir**
¡Invitamos a todos los desarrolladores interesados a contribuir al proyecto! Si tienes ideas para mejorar el juego, agregar nuevas características o corregir errores, ¡haz un **Pull Request**! Aquí hay algunas áreas en las que podrías contribuir:
- **Nuevas Acciones**: Agrega nuevas acciones para los animales, como "defender" o "explorar".
- **Nuevas Restricciones**: Dado que el refugio es compartido por ambos animales, se podría impedir que ambos animales lo usaran en el mismo turno. Para ellos había que definir una regla para establecer el orden en que los jugadores puedan definir sus acciones, ya que como esta actualemente implementado el juego el gato es siempre el primero en escojer su acción.
- **Nuevos Animales**: Implementa nuevos animales con habilidades únicas.
- **Mejoras en la Interfaz**: Mejora la interfaz de usuario para hacerla más amigable.
- **Optimización**: Optimiza el código para mejorar el rendimiento.

---

## **Conclusión**
"Cats and Mouses" es un juego simple pero divertido que combina estrategia y aleatoriedad. Tanto jugadores como desarrolladores pueden disfrutar de este proyecto y contribuir a su crecimiento. ¡Únete a nosotros y ayuda a hacer este juego aún mejor!

**¡Haz un Pull Request y sé parte de la comunidad de Cats and Mouses!**

--- 

¡Esperamos que disfrutes del juego y que te unas a nosotros para mejorarlo! 🐱🐭
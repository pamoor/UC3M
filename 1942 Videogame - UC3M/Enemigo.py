
import Constantes
import random
import pyxel


class Enemigo:
    """Esta clase almacena toda la información necesaria referente a los
    enemigos, el tipo de enemigo, su vida, su patrón de movimiento,
    su cadencia de disparo y los pintos que otorga al ser eliminado
    """

    def __init__(self, tipo: str, timer: int, lado: int):
        """Este método crea los enemigos aquí se inicializan el tipo y el
        tiempo, pero dependiendo el enemigo se inicializarán otros
        atributos, como la vida, la posición de inicio la probabilidad de
        disparo y la cadencia, y los puntos que otorga, así como su sprite.
        """
        self.tipo = tipo
        self.timer = timer

        if self.tipo == "Regular":

            self.y = 0
            self.sprite = Constantes.spritesEnemigos[0][0]
            self.vida = 10
            self.ladoSpawn = lado
            self.probDisp = 30
            self.cadencia = 200
            self.ultimoDisp = -200
            self.puntos = 100

            if self.ladoSpawn == 0:
                self.x = random.randint(0, Constantes.ancho // 3)
            if self.ladoSpawn == 1:
                self.x = random. randint(Constantes.ancho * 2 // 3,
                                         Constantes.ancho)

        if self.tipo == "Rojo":

            self.y = 40
            self.vida = 10
            self.ladoSpawn = lado
            self.probDisp = 80
            self.cadencia = 200
            self.ultimoDisp = -200
            self.puntos = 150
            self.timer = timer
            self.loop = 0

            if self.ladoSpawn == 0 or self.ladoSpawn == 2:
                self.x = 0
                self.sprite = Constantes.spritesEnemigos[1][2]

            if self.ladoSpawn == 1 or self.ladoSpawn == 3:
                self.x = Constantes.ancho
                self.sprite = Constantes.spritesEnemigos[1][6]

        if self.tipo == "Bombardero":

            self.y = 20
            self.vida = 50
            self.ladoSpawn = lado
            self.probDisp = 15
            self.cadencia = 10
            self.ultimoDisp = -10
            self.vuelta = False
            self.puntos = 500

            if self.ladoSpawn == 0:
                self.x = 0
                self.sprite = Constantes.spritesEnemigos[2][1]

            if self.ladoSpawn == 1:
                self.x = Constantes.ancho
                self.sprite = Constantes.spritesEnemigos[2][3]

        if self.tipo == "Superbombardero":

            self.y = 30
            self.vida = 200
            self.ladoSpawn = lado
            self.probDisp = 3
            self.cadencia = 30
            self.ultimoDisp = -10
            self.vuelta = False
            self.puntos = 2000

            if self.ladoSpawn == 0:
                self.x = 0
                self.sprite = Constantes.spritesEnemigos[3][1]

            if self.ladoSpawn == 1:
                self.x = Constantes.ancho
                self.sprite = Constantes.spritesEnemigos[3][3]

    def move(self):
        """Este método define el movimiento de los enemigos dependiendo de
        qué tipo sean
        """

        if self.tipo == "Regular":
            """En el caso del movimiento del regular evaluamos su sprite  para 
            ver si el avión ha de ir hacia arriba o hacia abajo, pues cambia 
            justo en la mitad de la pantalla y también el lado de aparición 
            para saber si tenemos que restar o sumar x.
            """

            if self.y >= Constantes.ancho // 2:
                self.sprite = Constantes.spritesEnemigos[0][1]

            if self.sprite == Constantes.spritesEnemigos[0][0]:
                self.y += 2
            else:
                self.y -= 2

            if self.ladoSpawn == 0:
                self.x += 1

            if self.ladoSpawn == 1:
                self.x -= 1

        if self.tipo == "Rojo":
            """En el caso del enemigo rojo tenemos dos movimientos 
            diferentes, que a su vez se diferencian en si el objeto aparece 
            en un lado del tablero o en el otro. En todos el movimiento es 
            controlado dependiendo de la diferencia entre el momento en el 
            que apareció el enemigo (self.timer) y el actual 
            (pyxel.frame_count), que se repetirá en bucle al haberlos ligado a 
            un resto.
            """

            tiempo = pyxel.frame_count - self.timer
            """En el primer caso el avión realizará un zigzag en toda la 
            pantalla para acabar subiendo hacia arriba desde el centro de
            la pantalla. 
            """
            if self.ladoSpawn == 0:
                if tiempo % 102 < 49 and tiempo < 204:
                    self.x += 5
                    self.sprite = Constantes.spritesEnemigos[1][0]
                elif tiempo % 102 < 51 and tiempo < 204:
                    self.y += 5
                    self.sprite = Constantes.spritesEnemigos[1][6]
                elif tiempo % 102 < 100 and tiempo < 204:
                    self.x -= 5
                    self.sprite = Constantes.spritesEnemigos[1][0]
                elif tiempo % 102 <= 102 and tiempo < 204:
                    self.y += 5
                    self.sprite = Constantes.spritesEnemigos[1][6]

                elif tiempo < 228:
                    self.x += 5
                    self.sprite = Constantes.spritesEnemigos[1][0]

                else:
                    self.y -= 8
                    self.sprite = Constantes.spritesEnemigos[1][2]

                if self.ladoSpawn == 1:

                    if tiempo % 102 < 49 and tiempo < 204:
                        self.x -= 5
                        self.sprite = Constantes.spritesEnemigos[1][6]
                    elif tiempo % 102 < 51 and tiempo < 204:
                        self.y += 5
                        self.sprite = Constantes.spritesEnemigos[1][0]
                    elif tiempo % 102 < 100 and tiempo < 204:
                        self.x += 5
                        self.sprite = Constantes.spritesEnemigos[1][6]
                    elif tiempo % 102 <= 102 and tiempo < 204:
                        self.y += 5
                        self.sprite = Constantes.spritesEnemigos[1][0]

                    elif tiempo < 228:
                        self.x -= 5
                        self.sprite = Constantes.spritesEnemigos[1][6]

                    else:
                        self.y -= 8
                        self.sprite = Constantes.spritesEnemigos[1][2]

            """En estos dos siguientes patrones el avión realiza un 
            movimiento en forma de triángulos, desplazándose diagonalmente 
            por la pantalla. Debido a este movimiento decidimos 
            implementarle también sprites orientados diagonalmente.
            """
            if self.ladoSpawn == 2:

                if tiempo % 52 < 22:
                    self.x += 5
                    self.sprite = Constantes.spritesEnemigos[1][0]

                elif tiempo % 52 < 32:
                    self.x -= 4
                    self.y -= 4
                    self.sprite = Constantes.spritesEnemigos[1][3]

                elif tiempo % 52 < 42:
                    self.x -= 4
                    self.y += 4
                    self.sprite = Constantes.spritesEnemigos[1][5]

                elif tiempo % 52 < 52:
                    self.x += 4
                    self.y += 4
                    self.sprite = Constantes.spritesEnemigos[1][7]

            if self.ladoSpawn == 3:

                if tiempo % 52 < 22:
                    self.x -= 5
                    self.sprite = Constantes.spritesEnemigos[1][4]

                elif tiempo % 52 < 32:
                    self.x += 4
                    self.y -= 4
                    self.sprite = Constantes.spritesEnemigos[1][1]

                elif tiempo % 52 < 42:
                    self.x += 4
                    self.y += 4
                    self.sprite = Constantes.spritesEnemigos[1][7]

                elif tiempo % 52 < 52:
                    self.x -= 4
                    self.y += 4
                    self.sprite = Constantes.spritesEnemigos[1][5]

        """Tanto el bombardero como el superbombardero se mueven en base 
        su posición actual, describiendo la forma de un rectángulo y una 
        vez acabada saliendo de la pantalla por la parte opuesta a donde 
        aparecieron. Para ello, en la esquina del rectángulo donde debe 
        girar o no se evalúa el atributo self.vuelta, que únicamente se 
        vuelve True cuando ha completado la mitad del rectángulo.
        """

        if self.tipo == "Bombardero":

            if self.ladoSpawn == 0:

                if self.y == 30 and self.x < Constantes.ancho - 30 - \
                        self.sprite[3]:
                    self.sprite = Constantes.spritesEnemigos[2][1]
                    self.x += 2

                elif self.x >= Constantes.ancho - 30 - self.sprite[3] and \
                        self.y < 100 and not self.vuelta:
                    self.sprite = Constantes.spritesEnemigos[2][0]
                    self.y += 2

                elif self.y >= 100 and self.x > 30:
                    self.sprite = Constantes.spritesEnemigos[2][3]
                    self.x -= 2
                    self.vuelta = True

                elif self.y > 30:
                    self.sprite = Constantes.spritesEnemigos[2][2]
                    self.y -= 2

                else:
                    self.x += 2

            if self.ladoSpawn == 1:

                if self.y == 30 and self.x > 30:
                    self.sprite = Constantes.spritesEnemigos[2][3]
                    self.x -= 2

                elif self.x <= 30 and self.y < 100 and not self.vuelta:
                    self.sprite = Constantes.spritesEnemigos[2][0]
                    self.y += 2

                elif self.y >= 100 and self.x < Constantes.ancho - 30 - \
                        self.sprite[3]:
                    self.sprite = Constantes.spritesEnemigos[2][1]
                    self.x += 2
                    self.vuelta = True

                elif self.y > 30:
                    self.sprite = Constantes.spritesEnemigos[2][2]
                    self.y -= 2

                else:
                    self.x -= 2

        if self.tipo == "Superbombardero":

            if self.ladoSpawn == 0:

                if self.y == 30 and self.x < Constantes.ancho - 30 - \
                        self.sprite[2]:
                    self.sprite = Constantes.spritesEnemigos[3][1]
                    self.x += 1

                elif self.x >= Constantes.ancho - 30 - self.sprite[3] and \
                        self.y < 60 and not self.vuelta:
                    self.sprite = Constantes.spritesEnemigos[3][0]
                    self.y += 1

                elif self.y == 60 and self.x > 30:
                    self.sprite = Constantes.spritesEnemigos[3][3]
                    self.x -= 1
                    self.vuelta = True

                elif self.y > 30:
                    self.sprite = Constantes.spritesEnemigos[3][2]
                    self.y -= 1

                else:
                    self.x += 1

            if self.ladoSpawn == 1:

                if self.y == 30 and self.x > 30:
                    self.sprite = Constantes.spritesEnemigos[3][3]
                    self.x -= 1

                elif self.x <= 30 and self.y < 60 and not self.vuelta:
                    self.sprite = Constantes.spritesEnemigos[3][0]
                    self.y += 1

                elif self.y == 60 and self.x < Constantes.ancho - 30 - \
                        self.sprite[2]:
                    self.sprite = Constantes.spritesEnemigos[3][1]
                    self.x += 1
                    self.vuelta = True

                elif self.y > 30:
                    self.sprite = Constantes.spritesEnemigos[3][2]
                    self.y -= 1

                else:
                    self.x -= 1

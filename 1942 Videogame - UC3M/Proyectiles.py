import Constantes


class Proyectiles:
    """ Esta clase almacena toda la información necesaria para el
    funcionamiento de los proyectiles de nuestro juego."""

    def __init__(self, x: int, y: int, player: bool, misil: bool, bonus: bool):
        """Este método crea los proyectiles

           @param x inicializa la x

           @param y inicializa la y

           @param player inicializa un booleano para saber si el
           proyectil es lanzado por el jugador

           @param misil inicializa un booleano para saber si el que lanza el
           proyectil es el superbombardero

           @param bonus es un parámetro que en caso de acabar con todos los
           enemigos rojos te otorga un disparo cuádruple que hace más daño"""

        """En esta sección se definen los atributos de la clase: la posición del
        proyectil, si este pertenece al jugador y si el tipo de proyectil 
        es "misil", el daño, que depende de si hay bonus o no y el sprite 
        según el tipo proyectil.
        """

        self.x = x
        self.y = y
        self.jugador = player
        self.misil = misil

        if not bonus:
            self.dmg = 10
        else:
            self.dmg = 25

        if self.jugador:
            if not bonus:
                self.sprite = Constantes.spritesProyectiles[2]
            else:
                self.sprite = Constantes.spritesProyectiles[3]
        else:
            if self.misil:
                self.sprite = Constantes.spritesProyectiles[4]
            else:
                self.sprite = Constantes.spritesProyectiles[1]

    def move(self, posicionJugadorx, posicionJugadory):

        """ Aquí se definen los movimientos de los distintos proyectiles,
           se diferencian el del jugador y el de los enemigos, a su vez en
           el de los enemigos se diferencian los misiles, ya que estos se
           dirigen hacia un punto superior al jugador para luego caer en
           vertical, en lugar de caer en vertical directamente.
           """

        if self.jugador:
            self.y -= 15

        else:

            if self.misil:

                if self.y > posicionJugadory - 50:
                    self.y += 5
                else:
                    self.y += 0.03 * (posicionJugadory - 20 - self.y)

                    if 10 < 0.05 * (posicionJugadorx + 12 - self.x):
                        self.x += 10
                    elif -10 > 0.05 * (posicionJugadorx + 12 - self.x):
                        self.x -= 10
                    else:
                        self.x += 0.05 * (posicionJugadorx + 12 - self.x)

            else:
                self.y += 5

import pyxel


class Avion:
    """Esta clase almacena toda la información necesaria para nuestro avión,
     el movimiento, la cadencia de disparo, las vidas y la voltereta"""

    def __init__(self, x: int, y: int):
        """ Este método crea el objeto avión
        @param x la x inicial
        @param y la y inicial
        """

        """ Esta sección define los atributos de la clase: el sprite, 
        la posición en el tablero, la velocidad a la que se mueve, las vidas, 
        la cadencia de disparos, el momento en el que se ha realizado el 
        último disparo, si está haciendo la voltereta, si está invulnerable, 
        el tiempo de invulnerabilidad tras haber sido alcanzado por un 
        enemigo y si nuestro avión se ha quedado sin vidas.
        """
        self.sprite = None
        self.x = x
        self.y = y
        self.velocidad = 5
        self.vidas = 5
        self.loopsDisp = 5
        self.cadencia = 8
        self.ultimoDisp = 0
        self.loop = False
        self.invulnerable = False
        self.tiempoinvul = 50
        self.muerto = False

    def move(self, direccion: str):

        """ Este es el método que dirige el movimiento del aeroplano, recibe
        la dirección ordenada por el jugador.
        """

        if direccion == "derecha":
            self.x += self.velocidad

        if direccion == "izquierda":
            self.x -= self.velocidad

        if direccion == "arriba":
            self.y -= self.velocidad

        if direccion == "abajo":
            self.y += self.velocidad

    def helices(self, frames):

        """Este es un método que define el movimiento de las hélices del
        avión, en función de la paridad del frame en el que nos encontremos
         """

        if frames % 2 == 0 and not self.loop:
            self.sprite = (0, 0, 25, 17)
        elif frames % 2 == 1 and not self.loop:
            self.sprite = (25, 0, 25, 17)

    def voltereta(self, timer: int):

        """ Este es un método que define la voltereta que hace el avión para
        esquivar las balas, cambiando su sprite en función de la diferencia
        entre el momento en el que se ordenó la voltereta y el contador de
        frames de pyxel.
        """

        tiempo = pyxel.frame_count - timer

        lista_sprites = ((30, 20, 26, 11), (59, 24, 24, 6),
                         (114, 23, 24, 7), (212, 0, 26, 15),
                         (0, 0, 25, 17))

        if tiempo < 5:
            self.sprite = lista_sprites[0]

        elif tiempo < 10:
            self.sprite = lista_sprites[1]

        elif tiempo < 15:
            self.sprite = lista_sprites[2]

        elif tiempo < 20:
            self.sprite = lista_sprites[3]

        elif tiempo < 25:
            self.sprite = lista_sprites[4]

        elif tiempo < 30:
            self.loop = False

    def impacto(self, timer: int):

        """Este es un método que define el comportamiento del avión después
        de haber sido alcanzado por un proyectil, se vuelve invulnerable
        durante un periodo de tiempo.
        """

        if pyxel.frame_count - timer < self.tiempoinvul:
            self.invulnerable = True
            if pyxel.frame_count - timer < 10:
                self.sprite = (0, 38, 23, 20)
            else:
                if (pyxel.frame_count - timer) % 2 == 0:
                    self.sprite = (240, 240, 20, 20)
        else:
            self.invulnerable = False

    def muerte(self, timer: int):

        """ Este método se ejecuta cuando el avión se queda sin vidas,
        y en función del tiempo que ha pasado desde el último impacto,
        introducido como parámetro, el sprite del avión cambia.
        """

        listaSprites = ((0, 39, 24, 20), (24, 37, 30, 24), (55, 35, 31, 29),
                        (86, 35, 30, 29), (118, 35, 31, 29), (152, 36, 27, 24))

        tiempo = pyxel.frame_count - timer

        if tiempo < 5:
            self.sprite = listaSprites[0]

        elif tiempo < 10:
            self.sprite = listaSprites[1]

        elif tiempo < 15:
            self.sprite = listaSprites[2]

        elif tiempo < 20:
            self.sprite = listaSprites[3]

        elif tiempo < 25:
            self.sprite = listaSprites[4]

        else:
            self.sprite = listaSprites[5]













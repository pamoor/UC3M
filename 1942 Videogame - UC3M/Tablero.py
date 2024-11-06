from Avión import Avion
from Proyectiles import Proyectiles
import Constantes
import pyxel
from Enemigo import Enemigo
from Fondo import Fondo
from Enemigo_Muerto import Muerto
import random


class Tablero:
    """ Esta clase tiene toda la información necesaria para representar el
    tablero donde el jugador podrá disfrutar del juego"""

    def __init__(self):

        # Estos atributos definen las dimensiones del tablero
        self.ancho = Constantes.ancho
        self.alto = Constantes.alto

        # En este otro grupo se definen diversos atributos de los que se
        # harán uso a lo largo de la clase, así como los booleanos de inicio
        # y final del juego y los marcadores de puntuación
        self.inicio = True
        self.gameOver = False
        self.score = 0
        self.high_score = 0
        self.fondoAvance = False
        self.timerGeneral = 0
        self.timerVoltereta = 0
        self.timerImpacto = 0
        self.puntosBonus = 0
        self.timerBonus = 0
        self.disparoBonus = False
        self.lado_rojo = 0

        # En este grupo se introducen todos los atributos que corresponden a
        # los elementos que se mostrarán en pantalla, introduciendo al
        # inicio del juego el avión del jugador, el portaaviones, el título
        # del juego (que hemos decidido que descienda con el portaaviones) y
        # las olas iniciales.
        self.avion = Avion(self.ancho // 2 - 11, 200)
        self.lista_objetos = [Fondo(self.ancho // 2 -
                                    Constantes.spritesFondo[0][3] // 2, 0,
                                    "Portaaviones"),
                              Fondo(self.ancho // 2 -
                                    Constantes.spritesFondo[3][3] // 2, 0,
                                    "Titulo")]

        self.lista_proyectiles = []
        self.lista_enemigos = []
        self.lista_olas = []
        self.lista_enemigos_muertos = []

        # Este código genera al iniciar el juego olas que ocuparán el fondo
        # en el inicio, siguiendo la misma frecuencia con la que se irán
        # luego generando mientras se juega
        for n in range(self.alto // 5):
            for m in range(self.ancho // 2):
                if random.randint(0, 1) == 0:
                    self.lista_olas.append(Fondo(m * 2, n * 5, "Ola"))

        # Con esta función de pyxel se inicializa el juego
        pyxel.init(self.ancho, self.alto, title="1942")

        """ En esta sección se carga el archivo .pyxres con todos los 
        sprites, así como se cargan en el mismo todas las imágenes de las 
        islas, el portaaviones y el título del juego.
        """

        pyxel.load("Assets/Sprites.pyxres")

        pyxel.image(2).load(0, 0, "Assets/Portaaviones.png")
        pyxel.image(2).load(0, 169, "Assets/huete(1).png")
        pyxel.image(2).load(117, 0, "Assets/Ibiza(2).png")
        pyxel.image(2).load(117, 85, "Assets/Isla_pr.png")
        pyxel.image(1).load(0, 100, "Assets/1942.png")
        pyxel.image(0).load(56, 112, "Assets/Game_over.png")

        # Con esta otra función de pyxel se ejecuta el juego
        pyxel.run(self.update, self.draw)

    def update(self):

        """Esta función se ejecuta cada frame y es donde hemos introducido
        todas las acciones que ocurren a lo largo del juego."""

        # Este breve bloque evalúa si se pulsa la tecla [ESC], que cierra el
        # juego
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        """ Este bloque da resetea todas las listas de elementos (menos las 
        olas) y coloca en pantalla el avión, el portaaviones y el título, 
        para dar comienzo a una nueva partida en el momento en el que se 
        pulse la tecla [SPACE]. También resetea el controlador de tiempo 
        para los enemigos y la puntuación.
        """
        if (self.inicio or self.gameOver) and pyxel.btn(pyxel.KEY_SPACE):
            self.inicio = False
            self.gameOver = False
            self.lista_enemigos.clear()
            self.lista_proyectiles.clear()
            self.lista_enemigos_muertos.clear()
            self.avion = Avion(self.ancho // 2 - 11, 200)
            self.lista_objetos = [Fondo(self.ancho // 2 -
                                        Constantes.spritesFondo[0][3] // 2, 0,
                                        "Portaaviones"),
                                  Fondo(self.ancho // 2 -
                                        Constantes.spritesFondo[3][3] // 2,
                                        0,  "Titulo")]
            self.timerGeneral = 0
            self.score = 0

        # Esto aumenta cada frame el valor del timer que hemos creado nosotros
        self.timerGeneral += 1

        # Esta función anima las hélices del avión controlado por el jugador
        self.avion.helices(pyxel.frame_count)

        # Este bloque actualiza el record de la sesión si es superado por la
        # puntuación de la partida
        if self.score > self.high_score:
            self.high_score = self.score

        # Con este pequeño bloque se consigue que una vez haya explotado el
        # avión del jugador no vuelva a aparecer hasta la siguiente partida.
        if self.gameOver:
            self.avion.sprite = (0, 0, 0, 0)

        """ Aquí comienza el código de lo que ocurre en una partida de 
        nuestro juego, que solo sucederá si no estamos ni en la pantalla del 
        inicio ni en la del final del mismo.
        """
        if not self.inicio and not self.gameOver:

            # ******** MOVIMIENTO *******

            """ Este bloque define el movimiento de la aeronave del jugador, 
            evaluando que no sobrepase ninguno de los bordes establecidos,
            cuando se pulsen las flechas direccionales. 
            """

            if pyxel.btn(pyxel.KEY_RIGHT) and Constantes.ancho - \
                    self.avion.sprite[2] > self.avion.x:
                self.avion.move('derecha')

            if pyxel.btn(pyxel.KEY_LEFT) and self.avion.x > 0:
                self.avion.move('izquierda')

            # Si se pulsa la flecha superior y se llega al límite
            # establecido, hemos implementado que el fondo avance hacia
            # abajo con mayor velocidad.

            if pyxel.btn(pyxel.KEY_UP):
                if self.avion.y > Constantes.alto // 2:
                    self.avion.move('arriba')
                else:
                    self.fondoAvance = True
            else:
                self.fondoAvance = False

            if pyxel.btn(pyxel.KEY_DOWN) and Constantes.alto - \
                    self.avion.sprite[3] - 10 > self.avion.y:
                self.avion.move('abajo')

            """ En estos bloques se ejecutan los métodos de movimiento 
            del resto de objetos en pantalla, así como se evalúa si se deben 
            eliminar al haber sobrepasado uno de los límites de la misma.
            Además, para los elementos del fondo se evalúa si se está 
            avanzando rápido o no.
            """

            for bala in self.lista_proyectiles:
                bala.move(self.avion.x, self.avion.y)
                if bala.y < 0 or bala.y > self.alto:
                    self.lista_proyectiles.remove(bala)

            for elemento in self.lista_objetos:
                if self.fondoAvance:
                    elemento.avance = True
                else:
                    elemento.avance = False
                elemento.move()
                if elemento.y > self.alto:
                    self.lista_objetos.remove(elemento)

            for ola in self.lista_olas:
                if self.fondoAvance:
                    ola.avance = True
                else:
                    ola.avance = False
                ola.move()
                if ola.y > self.alto:
                    self.lista_olas.remove(ola)

            for enemigo in self.lista_enemigos:
                enemigo.move()
                if enemigo.y < 0 or enemigo.x < - enemigo.sprite[
                    2] or enemigo.x > \
                        Constantes.ancho and enemigo in self.lista_enemigos:
                    self.lista_enemigos.remove(enemigo)

            # ******** VOLTERETA DEL AVIÓN ********

            """ En este bloque se evalúa si se pulsa la tecla [X], que en 
            caso de que se dispusiese de consumibles de volteretas, el avión 
            realiza una, cambiando su sprite y volviéndose invulnerable por 
            un tiempo.
            """

            if pyxel.btnp(pyxel.KEY_X) and self.avion.loopsDisp > 0:
                self.avion.loop = True
                self.timerVoltereta = pyxel.frame_count
                self.avion.loopsDisp -= 1

            if self.avion.loop:
                self.avion.voltereta(self.timerVoltereta)

            # ************ SPAWNS ************

            """ En este bloque se añaden tanto a las listas de olas, 
            enemigos y objetos del fondo los elementos necesarios a lo largo 
            del transcurso de la partida.
            """

            # Las islas se generan cada 100 frames, escogiéndose cada vez
            # aleatoriamente una entre las tres disponibles
            if self.timerGeneral % 250 == 0:
                n = random.randint(1, 3)
                if n == 1:
                    self.lista_objetos.append(Fondo(random.randint
                                                    (0, 3 * self.ancho // 4),
                                                    0, "Huete"))

                elif n == 2:
                    self.lista_objetos.append(Fondo(random.randint
                                                    (0, 3 * self.ancho // 4),
                                                    0, "Ibiza"))
                elif n == 3:
                    self.lista_objetos.append(Fondo(random.randint
                                                    (0, 3 * self.ancho // 4),
                                                    0, "PR"))

            # Para generar las olas, la frecuencia de generación variará en
            # función de si se está avanzando rápidamente o no
            if self.fondoAvance:
                frecuenciaolas = 3
            else:
                frecuenciaolas = 6

            if self.timerGeneral % frecuenciaolas == 0:

                # Cada 2 píxeles del ancho del tablero hay 1/2 de
                # probabilidad de que se genere una ola de tamaño 3*2
                for k in range(self.ancho // 2):
                    if random.randint(0, 1) == 0:
                        self.lista_olas.append(Fondo(k * 2, 0, "Ola"))

            """ Los enemigos regulares son los únicos que se generan de 
            manera aleatoria, pues los demás se generan en intervalos de 
            tiempo establecidos.
            """
            if random.randint(0, 30) == 0:
                self.lista_enemigos.append(Enemigo("Regular",
                                                   self.timerGeneral,
                                                   random.randint(0, 1)))

            if self.timerGeneral % 500 - 200 == 0:
                self.lista_enemigos.append(Enemigo("Bombardero",
                                                   pyxel.frame_count,
                                                   random.randint(0, 1)))

            if self.timerGeneral % 2000 == 0:
                self.lista_enemigos.append(Enemigo("Superbombardero",
                                                   pyxel.frame_count,
                                                   random.randint(0, 1)))

            # En el caso de los rojos, se generan en oleadas de 5 enemigos
            # que siguen todos la misma formación
            if self.timerGeneral % 800 == 0 or self.timerGeneral % 800 == \
                    794 or self.timerGeneral % 800 == 788 or \
                    self.timerGeneral % 800 == 782 or self.timerGeneral % 800 \
                    == 776 or self.timerGeneral % 800 == 770:

                if self.timerGeneral % 800 == 770:
                    self.lado_rojo = random.randint(0, 3)

                self.lista_enemigos.append(Enemigo("Rojo", pyxel.frame_count,
                                                   self.lado_rojo))

            # ************* DISPAROS *************

            """ En este bloque se definen las características del disparo que 
            realiza el propio jugador; evalúa si desde el último disparo ha 
            pasado el tiempo establecido (cadencia) y si el avión no se 
            encuentra haciendo la voltereta. Si esto se cumple, se genera un 
            proyectil desde la parte superior y central del avión, pudiendo 
            ser una única bala o 4 dependiendo si el jugador tiene el bonus 
            activo. 
            """

            if pyxel.btn(pyxel.KEY_Z) and pyxel.frame_count - \
                    self.avion.ultimoDisp >= self.avion.cadencia and not \
                    self.avion.loop:
                if not self.disparoBonus:
                    self.lista_proyectiles.append(
                        Proyectiles(self.avion.x + self.avion.sprite[2] // 2,
                                    self.avion.y - self.avion.sprite[3],
                                    True, False, False))
                else:

                    self.lista_proyectiles.append(
                        Proyectiles(self.avion.x + self.avion.sprite[2] // 4,
                                    self.avion.y - self.avion.sprite[3],
                                    True, False, True))

                self.avion.ultimoDisp = pyxel.frame_count

            """ En este otro bloque se definen los disparos de los distintos 
            enemigos. Cada uno dispara en base a unos atributos de la clase:
            probabilidad de disparo, cadencia y último disparo, funcionando 
            de forma muy parecida a los proyectiles del jugador, solo que en 
            este caso se generan de manera aleatoria. Se distinguen los 
            proyectiles de los enemigos regulares (que solo disparan cuando 
            se dirigen al jugador), rojos y bombarderos, de los misiles que 
            crea el superbombardero. Siempre se generan en la parte central 
            e inferior del avión.
            """

            for enemigo in self.lista_enemigos:
                a = random.randint(0, enemigo.probDisp)
                if a == 0 and pyxel.frame_count - enemigo.ultimoDisp >= \
                        enemigo.cadencia:

                    if (not enemigo.sprite == Constantes.spritesEnemigos[0][1]
                        and enemigo.tipo == "Regular") or enemigo.tipo == \
                            "Bombardero" or enemigo.tipo == "Rojo":
                        self.lista_proyectiles.append(
                            Proyectiles(enemigo.x + enemigo.sprite[2] // 2,
                                        enemigo.y + enemigo.sprite[3],
                                        False, False, False))

                    elif enemigo.tipo == "Superbombardero":
                        self.lista_proyectiles.append(
                            Proyectiles(enemigo.x + enemigo.sprite[2] // 2,
                                        enemigo.y + enemigo.sprite[3], False,
                                        True, False))

                    enemigo.ultimoDisp = pyxel.frame_count

            # *************COLISIONES*************

            """ En este sección se definen los impactos de cada proyectil 
            enemigo sobre el jugador. La condición evalúa si la distancia de la
            bala a avión tanto por las coordenadas como por las ordenadas 
            está entre 0 y el tamaño del sprite, si el avión no ha recibido 
            un impacto recientemente (invulnerabilidad) y si no se haya 
            haciendo la voltereta. 
            """
            for bala in self.lista_proyectiles:
                if not bala.jugador:
                    if 0 >= self.avion.x - bala.x >= - self.avion.sprite[2] \
                            and 0 <= self.avion.y - bala.y <= \
                            self.avion.sprite[3] and not \
                            self.avion.invulnerable and \
                            not self.avion.loop:

                        # En caso de que la bala impacte el avión se vuelve
                        # invulnerable, se elimina la bala y se resta una vida;
                        # si esta era la última, se cambia el booleano "muerto"
                        # del avión.

                        self.avion.invulnerable = True
                        self.timerImpacto = pyxel.frame_count
                        self.lista_proyectiles.remove(bala)
                        if self.avion.vidas > 1:
                            self.avion.vidas -= 1
                        else:
                            self.avion.vidas -= 1
                            self.avion.muerto = True

            # En caso de que el avión se quede sin vidas, se ejecuta esta
            # función, que lleva a cabo la animación de una explosión para
            # después acabar la partida
            if self.avion.muerto:
                self.avion.muerte(self.timerImpacto)
                if pyxel.frame_count - self.timerImpacto == 30:
                    self.gameOver = True

            # Aquí se ejecuta la función que indica si el avión es
            # invulnerable después de haber sido alcanzado
            if self.avion.invulnerable and not self.avion.muerto:
                self.avion.impacto(self.timerImpacto)

            """ En este otro bloque, por el contrario, se evalúan los 
            impactos de las balas del jugador sobre los enemigos. En este 
            caso, los enemigos no tienen tiempo de invulnerabilidad y 
            pierden puntos de vida en función al daño de la bala disparada 
            (que depende de si el bonus está activo o no). 
            """

            for bala in self.lista_proyectiles:
                if bala.jugador:
                    for enemigo in self.lista_enemigos:
                        if bala.sprite[2] >= enemigo.x - bala.x >= - \
                                enemigo.sprite[2] and \
                                0 <= enemigo.y - bala.y <= enemigo.sprite[3]:
                            enemigo.vida -= bala.dmg
                            if bala in self.lista_proyectiles:
                                self.lista_proyectiles.remove(bala)

            """ En caso de que el enemigo muera, se añade en su posición un 
            objeto de su tipo a la lista de enemigos muertos (que muestra los 
            puntos que ha otorgado ese enemigo), se suman esos puntos al 
            marcador, si era un enemigo rojo se cuenta ante el posible bonus y 
            se elimina el enemigo de la lista del tablero.
            """
            for enemigo in self.lista_enemigos:
                if enemigo.vida <= 0:
                    self.lista_enemigos_muertos.append(Muerto(enemigo.x,
                                                              enemigo.y,
                                                              enemigo.tipo))
                    self.score += enemigo.puntos
                    if enemigo.tipo == "Rojo":
                        self.puntosBonus += 1
                        self.timerBonus = pyxel.frame_count
                    self.lista_enemigos.remove(enemigo)

            """ En esta sección se da movimiento a las puntuaciones 
            flotantes que dejan los enemigos derrotados, además de 
            eliminarlas cuando superan el tiempo establecido"""

            for abatido in self.lista_enemigos_muertos:
                abatido.action()
                if abatido.tiempo > 50:
                    self.lista_enemigos_muertos.remove(abatido)

            """ En caso de que se hayan derrotado a todos los enemigos rojos de
            esa oleada, se activará el bonus. Se cuenta también con un 
            temporizador que reseteará el contador de rojos muertos de 
            cara a la siguiente oleada y pondrá en False el bonus en caso 
            de que se hubiese obtenido una vez transcurra el tiempo 
            preciso.
            """
            if self.puntosBonus == 6:
                self.disparoBonus = True
            if pyxel.frame_count - self.timerBonus > 300:
                self.disparoBonus = False
                self.puntosBonus = 0

    def draw(self):
        """ Este método representa en pantalla cada frame todo lo que se le
        indique. Es importante incluir un pyxel.cls para que borre todo lo
        dibujado en el frame anterior.
        """

        pyxel.cls(1)

        """ En esta sección se representan todos los objetos que hay en la 
        clase tablero, atendiendo a sus coordenadas y su sprite, 
        incluyendo como color transparente el negro, pues ocupa el fondo 
        de nuestro archivo .pyxres.
        """
        for ola in self.lista_olas:
            pyxel.blt(ola.x, ola.y, *ola.sprite, colkey=0)

        for cosa in self.lista_objetos:
            pyxel.blt(cosa.x, cosa.y, *cosa.sprite, colkey=0)

        for n in self.lista_proyectiles:
            pyxel.blt(n.x, n.y, 1, *n.sprite, colkey=0)

        for n in self.lista_enemigos:
            pyxel.blt(n.x, n.y, 0, *n.sprite, colkey=0)

        for n in self.lista_enemigos_muertos:
            pyxel.blt(n.x, n.y, 0, *n.sprite, colkey=0)

        pyxel.blt(self.avion.x, self.avion.y, 1, *self.avion.sprite, colkey=0)

        """Una vez comenzada la partida se mostrarán al jugador sus vidas, 
        sus loops restantes y su puntuación actual, así como el bonus de 
        forma intermitente si se poseyese.
        """
        if not self.inicio:
            pyxel.text(self.ancho - 40, self.alto - 30, "Vidas: " +
                       str(self.avion.vidas), 7)

            pyxel.text(self.ancho - 40, self.alto - 20, "Loops: " +
                       str(self.avion.loopsDisp), 7)

            pyxel.text(self.ancho - 55, 10, "Puntos: " + str(self.score), 7)

            if self.disparoBonus:
                if pyxel.frame_count % 10 > 4:
                    pyxel.text(self.ancho - 40, self.alto - 50, "**BONUS**",
                               10)
        # Por el contrario, el récord se mostrará también en el inicio
        pyxel.text(10, 10, "Record actual: " + str(self.high_score), 7)

        """ En este bloque se define lo que acompañará al portaaviones y el 
        título en el inicio del juego, solo que estos textos desaparecerán 
        en el momento en que se empiece a jugar.
        """
        if self.inicio:

            pyxel.text(self.ancho - 70, self.alto // 3, "PULSE [SPACE] "
                                                        "\n\nPARA "
                                                        "COMENZAR", 7)
            pyxel.text(10, self.alto // 3, "Desarrollado por \n\nPablo "
                                           "Amor y\n\n"
                                           "Alvaro Carrasco", 7)

        """ En este último bloque se representan una imagen de "GAME OVER" 
        junto a un texto con las instrucciones para empezar una nueva 
        partida, en caso de que al jugador se le agotasen las vidas.
        """
        if self.gameOver:
            pyxel.blt(Constantes.ancho // 2 - Constantes.spritesFondo[4][3]
                      // 2,
                      Constantes.alto // 8, *Constantes.spritesFondo[4],
                      colkey=0)
            pyxel.text(self.ancho // 2 - 58, self.alto // 2,
                       "Pulsa [SPACE] para reintentar", 7)

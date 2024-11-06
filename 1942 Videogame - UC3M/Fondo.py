"""
Created by Pablo Amor in dic 2022
Universidad Carlos III de Madrid
"""
import Constantes


class Fondo:
    """ Esta clase almacena toda la información necesaria de todo lo
    referente a las imágenes que componen el fondo del videojuego """

    def __init__(self, x: int, y: int, tipo: str):

        """Este método crea los objetos que decoran el fondo del videojuego

        @param x establece la x inicial

        @param y establece la y inicial

        @param tipo es un string que indica la imagen que debe ser
        mostrada en el fondo.
        """

        """En esta sección se definen los atributos, el tipo, el avance
        dependiendo de si el avión del jugador llega a un punto del tablero,
        la posición en x, y la posición en y y el sprite del objeto, 
        que dependerán del tipo del mismo.
        """

        self.tipo = tipo
        self.avance = False
        self.x = x

        if self.tipo == "Huete":
            self.sprite = Constantes.spritesFondo[1][0]
        if self.tipo == "Ibiza":
            self.sprite = Constantes.spritesFondo[1][1]
        if self.tipo == "PR":
            self.sprite = Constantes.spritesFondo[1][2]

        if self.tipo != "Portaaviones" and self.tipo != "Ola" \
                and self.tipo != "Titulo":
            self.y = -self.sprite[4]

        if self.tipo == "Portaaviones":
            self.y = Constantes.alto - Constantes.spritesFondo[0][4]
            self.sprite = Constantes.spritesFondo[0]

        if self.tipo == "Titulo":
            self.y = Constantes.alto // 9
            self.sprite = Constantes.spritesFondo[3]

        if self.tipo == "Ola":
            self.sprite = Constantes.spritesFondo[2]
            self.y = y

    def move(self):
        """ Aquí se define el movimiento de las imágenes que conforman el
        fondo, en caso de que avance sea True avanzarán más rápido para dar
        una sensación de velocidad mayor.
        """

        if not self.avance:
            self.y += 1
        else:
            self.y += 2

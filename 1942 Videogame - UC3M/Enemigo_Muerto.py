"""
Created by Pablo Amor in dic 2022
Universidad Carlos III de Madrid
"""


class Muerto:
    """Esta clase almacena toda la información referente a lo que ocurre
    cuando se eliminan los enemigos"""

    def __init__(self, x: int, y: int, tipo: str):

        """Este método define los atributos que tendrán los restos que dejan
        los enemigos tras morir, que se cambiarán por un número que
        representa su puntuación según su tipo, especificado como parámetro.
        """

        # Los atributos que se inicializan aquí son la x y la y que hacen
        # referencia a la posición y el tiempo que controla cuándo desaparecerá
        # el objeto. Por último, se asigna un sprite según el tipo a cada uno.
        self.x = x
        self.y = y
        self.tiempo = 0

        if tipo == "Regular":
            self.sprite = (1, 146, 13, 8)

        if tipo == "Bombardero":
            self.sprite = (1, 161, 29, 15)

        if tipo == "Rojo":
            self.sprite = (17, 145, 15, 8)

        if tipo == "Superbombardero":
            self.sprite = (0, 177, 55, 28)

    def action(self):
        """ Este método define lo que realizará el objeto, se irá moviendo
        hacia arriba y aumentará su tiempo hasta que llegado a cierta
        cantidad el objeto se elimine. """
        self.y -= 1
        self.tiempo += 1

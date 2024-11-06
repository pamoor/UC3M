"""
 Álvaro Carrasco Fuentes y Pablo Amor Molina
 Universidad Carlos III de Madrid
"""
from Tablero import Tablero

import pyxel

pyxel.init(Tablero().ancho, Tablero().alto, title="1942")

pyxel.run(Tablero().update, Tablero().draw)

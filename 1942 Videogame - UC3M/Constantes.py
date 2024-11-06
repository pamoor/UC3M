"""El archivo 'constantes' almacena todas las constantes utilizadas en el
código"""

# Estos son el ancho y el alto del tablero
ancho = 256
alto = 256

""" Estas tuplas representan las coordenadas y dimensiones de los sprites de 
los enemigos en el archivo .pyxres, para que llamarlos a lo largo del 
código resulte mucho más cómodo.
"""

spritesEnemigos = (
                   # Enemigo regular
                   ((132, 64, 15, 15), (148, 65, 13, 14)),

                   # Enemigo rojo
                   ((34, 65, 14, 13), (51, 65, 13, 14), (66, 64, 15, 15),
                    (82, 64, 14, 14), (99, 65, 14, 14), (115, 66, 14, 13),
                    (1, 65, 16, 14), (17, 67, 16, 12)),

                   # Bombardero
                   ((63, 86, 29, 23), (97, 84, 25, 27), (1, 87, 31, 23),
                    (36, 85, 25, 25)),

                   # Superbombardero
                   ((113, 1, 63, 49), (65, 0, 48, 63), (0, 0, 62, 49),
                    (176, 0, 48, 63)))


""" Esta otra tupla de tuplas define las coordenadas y las dimensiones de 
cada uno de los tipos de proyectil en el banco de imágenes del archivo. 
pyxres.
"""
spritesProyectiles = ((4, 79, 4, 4), (52, 79, 4, 4), (32, 73, 2, 9),
                      (70, 71, 15, 12), (59, 66, 8, 29))

""" Estas tuplas representan el banco en el que están cargadas las imágenes 
# del fondo, así como las coordenadas y el tamaño de cada una de estas. 
"""

spritesFondo = (
                # Portaaviones
                (2, 0, 0, 117, 169),
                # Islas
                ((2, 0, 169, 158, 81), (2, 117, 0, 135, 85),
                 (2, 117, 85, 130, 53)),
                # Olas
                (2, 252, 253, 3, 2),
                # 1942
                (1, 0, 100, 182, 46),
                # Game over
                (0, 56, 112, 167, 93))



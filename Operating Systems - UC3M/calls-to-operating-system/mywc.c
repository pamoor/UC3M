//P1-SSOO-23/24

#include <stdio.h>		// Librerría para impresión
#include <unistd.h>		// Librería para el control de ficheros
#include <fcntl.h>      // Librería para importar O_RDONLY
#define BUFSIZE 1


int main(int argc, char *argv[])
{
    //Declaración de variables
    int infile, leidos, leidostot=0, palabras=0, lineas=0, buscando = 1; 
    char buffer[BUFSIZE];

    if(argc < 2) //Error no hay suficientes argumentos
        {printf("Se debe introducir al menos un argumento\n");
         return(-1);}

    if((infile=open(argv[1], O_RDONLY)) == -1) //Error no se puede abrir el fichero
        {printf("No se ha podido abrir el fichero\n");
            return(-1);}

    while ((leidos = read(infile, buffer, BUFSIZE)!= 0)) { //Igualamos en cada iteración del while la salida de la función read a una variable
        if (leidos < 0) { //Si da  error al leer la función devolvera -1
            printf("Error de lectura\n");
            return (-1);
        }
        leidostot += 1; //Variable para controlar los bytes leidos
        if (buffer[0] == ' ' || buffer[0] == '\t') //Si hay un espacio o un \t pondremos buscando a 1
            {buscando = 1;} //Variable para saber cuando empezamos una palabra, cuando la encontremos será 0 y hasta el próximo espacio o salto no volvera a 1
        if (buffer[0] == '\n') //Si hay un salto de línea añadimos una línea y pondremos buscando a 1
            {lineas += 1; buscando = 1;}
        if (buscando == 1 && buffer[0]!= ' ' && buffer[0]!= '\t' && buffer[0] != '\n') //Si buscando es uno y el buffer no está en un espacio o salto de linea 
            {buscando = 0; palabras += 1;}                                             //Sumaremos una palabra y buscando volverá a ser 0
    }
    printf("%d %d %d %s\n", lineas, palabras, leidostot, argv[1]); //Impresión
    
	return(close(infile)); //Cerramos el fichero y devolvemos
}
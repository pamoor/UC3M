//P1-SSOO-23/24

#include <stdio.h>		// Librerría para impresión
#include <unistd.h>		// Librería para el control de ficheros
#include <sys/types.h>	// Librería para definir los tipos de datos
#include <dirent.h>		// Librería para el manejo de directorios
#include <string.h>		// Librería para usar funciones para el manejo de strings


int main(int argc, char *argv[])
{
	/* If less than three arguments (argv[0] -> program, argv[1] -> directory to search, argv[2] -> file to find) print an error y return -1 */

	if(argc < 3) //Error por número de argumentos
	{printf("Se necesitan más argumentos\n");
		return -1;
	}
	
    char *name = argv[1]; //Declaración de variables
    DIR *indir;
    struct dirent *entry;
	int encontrado = 0;

    if ((indir=opendir(name))==NULL) //Error al abrir el directorio
        {printf("Error al abrir el directorio\n");
            return(-1);}
        
    while (((entry=readdir(indir))!= NULL) && (encontrado == 0)) //Comprobamos que el read lea algo además comprobamos que no se haya encontrado el archivo
        {if (strcmp(argv[2], entry->d_name) == 0) //Si el nombre del fichero es igual a el segundo argumento que tenemos hemos encontrado el fichero
			encontrado = 1;}

	if (encontrado == 1) //Si se ha encontrado el archivo hacemos la impresión pedida
		printf("File %s is in directory %s\n", argv[2], argv[1]);
	else //Si no se ha encontrado el archivo hacemos la impresión pedida
		printf("File %s is not in directory %s\n", argv[2], argv[1]);
    
    return(closedir(indir)); //Cerramos y devolvemos

}

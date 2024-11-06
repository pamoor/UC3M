//P1-SSOO-23/24

#include <stdio.h>		// Librerría para impresión
#include <unistd.h>		// Librería para el gtcwd
#include <dirent.h>     // Librería para el manejo de directorios
#include <linux/limits.h> // Librería pra el PATH_MAX


int main(int argc, char *argv[])
{
    char buff[PATH_MAX], *name; //Declaración de variables
    DIR *indir;
    struct dirent *entry;

    if (argc != 1 && argc!= 2) //Error por número de argumentos
        {printf("Número de argumentos incorrecto\n");
            return (-1);}

    if (argc == 1) //Sin argumentos el nombre del directorio será el mismo donde estés 
        name = getcwd(buff, PATH_MAX);

    else
        name = argv[1]; //Con argumentos el nombre será el del argumento

    if ((indir=opendir(name))==NULL) //Error al abrir el directorio
        {printf("Error al abrir el directorio\n");
            return(-1);}
        
    while ((entry=readdir(indir))!= NULL) //Comprobamos que el read lea algo, cuando no lo haga habremos acabado
        printf("%s\n", entry->d_name); //Imprimimos el nombre del fichero seleccionado


    return(closedir(indir)); //Cerramos el directorio y devolvemos
}


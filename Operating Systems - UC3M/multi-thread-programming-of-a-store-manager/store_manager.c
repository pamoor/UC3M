//SSOO-P3 23/24

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stddef.h>
#include <sys/stat.h>
#include <pthread.h>
#include "queue.h"
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <ctype.h>


struct argprod{
    // Estructura para el parámetro de hilo de un Productor
    int i_instrucciones;
    int n_instrucciones;
    struct element *array;
    struct queue *buffer;
};

struct argcon{
    // Estructura para el parámetro de hilo de un Consumidor

    int n_instrucciones;
    struct queue *buffer;
};

struct acum{
    // Estructura para el resultado parcial devuelto por un consumidor
    int profit;
    int stocks[5];
};

int productos[5][3] = { 
    //Matriz de productos en formato {id, precio de compra, precio de venta}
        {1, 2, 3},
        {2, 5, 10},
        {3, 15, 20},
        {4, 25, 40},
        {5, 100, 125}
    };


// Declaración de las variables gestoras de la concurrencia en los hilos
pthread_mutex_t mutex;
pthread_cond_t not_full;
pthread_cond_t not_empty;

void *Productor(void *args) { // Función de los hilos productores
        struct argprod *argumentos = (struct argprod *)args; // Estructura pasada como parámetro

        for(int j=argumentos->i_instrucciones; j < argumentos->i_instrucciones + argumentos->n_instrucciones; j++ ) { 
            // Bucle de rango [indice_inicial, indice_inicial + numero_de_instryucciones]
  
            struct element *dato = &argumentos->array[j]; // Se recoge el dato del almacén

            pthread_mutex_lock(&mutex); // Acceso a la sección crítica

            while (queue_full(argumentos->buffer)) // Si el buffer está lleno se espera a que se vacíe
                pthread_cond_wait(&not_full, &mutex); 

            queue_put(argumentos->buffer, dato); // Una vez se pueda, insertamos elemento en el buffer
            
            // printf("INSERTO EN EL HILO: %d %d %d \n",argumentos->array[j].product_id, argumentos->array[j].op, argumentos->array[j].units);

            pthread_cond_signal(&not_empty); // Enviamos la señal de la condición "not_empty"

            pthread_mutex_unlock(&mutex); // Desbloqueo del mutex
        }
        pthread_exit(0);
    }


void *Consumidor(void *args) { /* codigo del consumidor */
    struct argcon *argumentos = (struct argcon *)args;
    //pthread_t tid = pthread_self();
    struct acum *retorno = calloc(1, sizeof(struct acum)); // Reserva de memoria (a 0) para la estructura a devolver

    for(int j=0; j < argumentos->n_instrucciones; j++ ) {

        pthread_mutex_lock(&mutex); // Acceso a la sección crítica

        while (queue_empty(argumentos->buffer)) // Si el buffer está vacío, se espera a que se introduzca al menos un elemento
            pthread_cond_wait(&not_empty, &mutex); 

        struct element *dato = queue_get(argumentos->buffer); // Se extrae el elemento del buffer
        
        //printf("SACO EN EL HILO %lu: %d %d %d \n", tid, dato->product_id, dato->op, dato->units);

        if (dato->op){ // OPERACIÓN SALE
            retorno->stocks[dato->product_id-1] -= dato->units; // Resto al stock las unidades
            retorno->profit += dato->units*productos[dato->product_id-1][2]; // Sumo al profit unidades * precio_venta
        }
        else { // OPERACIÓN PURCHASE
            retorno->stocks[dato->product_id-1] += dato->units; // Sumo al stock las unidades
            retorno->profit -= dato->units*productos[dato->product_id-1][1]; // Resto al profit unidades * precio_compra
        }

        pthread_cond_signal(&not_full); // Enviamos la señal de la condición "not_full"
        pthread_mutex_unlock(&mutex); // Desbloqueo del mutex
        }
    
    //printf("EL HILO %lu DEVUELVE: PROFIT:%d STOCKS:%d %d %d %d %d \n", tid, retorno->profit, retorno->stocks[0], retorno->stocks[1], retorno->stocks[2], retorno->stocks[3], retorno->stocks[4]);

    pthread_exit((void *)(retorno)); // Termino el hilo y devuelvo
    }

int main (int argc, const char * argv[])
    {
    int profits = 0;
    int product_stock[5]= {0};
    FILE *infile;
    

    if(argc != 5) // Error de número de argumentos incorrecto
        {printf("ERROR: se necesitan 4 argumentos para ejecutar la instrucción\n");
         return(-1);}
  
    if (!isdigit(*argv[2])|| !isdigit(*argv[3]) || !isdigit(*argv[4])) // Comprobación de caracteres numéricos
        {printf("ERROR: La estructura para ejecutar la instrucción es: ./store_manager <file name><num producers><num consumers><buff size>\n");
         return(-1);}

    // Paso de los argumentos en string a entero
    int num_productores = atoi(argv[2]);
    int num_consumidores = atoi(argv[3]);
    int tamano_buffer = atoi(argv[4]);
    if (tamano_buffer < 1) // Control del tamaño de buffer mínimo
        {printf("ERROR: El tamaño del buffer debe ser mayor que 0\n");
         return(-1);}

  
    infile = fopen(argv[1], "r"); // Abrimos el fichero

    if (infile == NULL) {
        perror("Error al abrir el fichero especificado");
        return (-1);}


    int ops; 
    if (fscanf(infile, "%d", &ops) != 1) { // Escaneo y control del número de operaciones a procesar (entero en la primera línea)
        printf("ERROR: La primera línea del archivo no es un entero.\n");
        fclose(infile);
        return (-1);}

    struct element *almacen = malloc(ops * sizeof(struct element)); // Reserva de memoria para el almacén de operaciones del fichero


    char tipo_op[8]; // Para almacenar temporalmente el tipo de operación
    int error_guernika = ops; /* Al ejecutar instrucción en Guernika, la variable ops se perdía en el bucle que hay a continuación,
                                 cuando se escaneaban los datos que componían cada una de las operaciones, por lo que para evitarlo
                                 se crea esta variable auxiliar que preserva el valor de ops y posteriormente se lo volverá a asignar*/

    for (int i = 0; i < error_guernika; i++) { // Bucle para rellenar el almacén con las operaciones del fichero
        
        if (fscanf(infile, "%d %s %d", &almacen[i].product_id, tipo_op, &almacen[i].units) < 3)
            {printf("ERROR: Formato de fichero incorrecto en torno a la línea %d\n", i+2);
            fclose(infile);
            return (-1);}

        if (almacen[i].product_id > 5 || almacen[i].product_id < 1)
            {printf("ERROR: Producto no identificado en la línea %d \n", i+2);
            fclose(infile);
            return(-1);}

        if (strcmp(tipo_op, "PURCHASE")==0) // Paso de manejar el tipo de operación en string a int, como así se especifica en la cabecera de element
            almacen[i].op = 0;

        else if (strcmp(tipo_op, "SALE")==0)
            almacen[i].op = 1;

        else 
            {printf("ERROR: Operación no identificada en la línea %d\n", i+2); // Si no es ni PURCHASE ni SALE
            fclose(infile);
            return (-1);}
        }


    ops = error_guernika; // Restauramos el valor que le corresponde a ops

    // Cálculo de las operaciones a realizar por cada hilo, así como las sobrantes a repartir
    int reparto_prod = ops / num_productores; 
    int resto_prod = ops % num_productores;
    //printf("TAREAS POR PRODUCTOR: %d RESTO: %d\n", reparto_prod, resto_prod);
    int cont_resto_prod = 0; // Contador para gestionar el resto utilizado posteriormente
    

    int reparto_con = ops / num_consumidores;
    int resto_con = ops % num_consumidores;
    //printf("TAREAS POR CONSUMIDOR: %d RESTO: %d\n", reparto_con, resto_con);
    int cont_resto_con = 0;

    // Reserva de memoria para los grupos de hilos
    pthread_t *productores = malloc(num_productores * sizeof(pthread_t)); 
    pthread_t *consumidores = malloc(num_consumidores * sizeof(pthread_t));

    // Reserva de memoria para los argumentos de los grupos de hilos
    struct argprod *total_argumentos_p = malloc(num_productores * sizeof(struct argprod));
    struct argcon *total_argumentos_c = malloc(num_consumidores * sizeof(struct argprod));

    // Se inicializa la cola con el tamaño especificado como argumento
    queue *cola = queue_init(tamano_buffer);
    
    // Se incializan las variables gestoras de la concurrencia
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&not_full, NULL);
    pthread_cond_init(&not_empty, NULL);

    
    

    for (int i=0; i < num_productores; i++){ // Bucle de creación de los Productores

        total_argumentos_p[i].buffer = cola;
        total_argumentos_p[i].array = almacen;

        if (i==0)
            total_argumentos_p[i].i_instrucciones = 0; // Índice inicial a 0
        else
            total_argumentos_p[i].i_instrucciones += (total_argumentos_p[i-1].n_instrucciones + total_argumentos_p[i-1].i_instrucciones); 
            // sumo al índice del elemento el número de elementos procesados en el anterior hilo más el índice en el que comenzó el anterior hilo

        // if (total_argumentos_p[i].i_instrucciones >= ops)
        //     break;

        if (cont_resto_prod < resto_prod){ // Control ejecuciones del "resto"
            cont_resto_prod++;
            total_argumentos_p[i].n_instrucciones = reparto_prod + 1;} // Todavía hay "resto" por compensar
        else
            total_argumentos_p[i].n_instrucciones = reparto_prod; // Caso estándar

        
        pthread_create(&productores[i], NULL, &Productor, (void *)&total_argumentos_p[i]); // Creamos el hilo
        }


    for (int i=0; i < num_consumidores; i++){ // Bucle de creación de los Consumidores

        total_argumentos_c[i].buffer = cola;

        if (cont_resto_con < resto_con){
            cont_resto_con++;
            total_argumentos_c[i].n_instrucciones = reparto_con + 1;}// Todavía hay "resto" por compensar
        else
            total_argumentos_c[i].n_instrucciones = reparto_con;// Caso estándar
        
        pthread_create(&consumidores[i], NULL, &Consumidor, (void *)&total_argumentos_c[i]);// Creamos el hilo
        }

    // Recogemos los hilos Productores
    for (int i=0; i < num_productores; i++){
        pthread_join(productores[i], NULL);}

    // Recogemos los hilos Consumidores
    for (int i=0; i < num_consumidores; i++){
        struct acum *devuelto;
        pthread_join(consumidores[i], (void **)&devuelto);

        // Actualizamos las variables según los datos parciales recogidos en cada hilo
        profits += devuelto->profit;
        for(int j=0; j < 5; j++){
            product_stock[j] += devuelto->stocks[j];
        }
        free(devuelto); // Liberamos la memoria reservada para la estructura que se devuelve en cada Consumidor
        }

    // Destruimos el control de la concurrencia
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&not_full);
    pthread_cond_destroy(&not_empty);



    // Output
    printf("Total: %d euros\n", profits);
    printf("Stock:\n");
    printf("  Product 1: %d\n", product_stock[0]);
    printf("  Product 2: %d\n", product_stock[1]);
    printf("  Product 3: %d\n", product_stock[2]);
    printf("  Product 4: %d\n", product_stock[3]);
    printf("  Product 5: %d\n", product_stock[4]);

    // Resolvemos las reservas de memoria, entre otros
    fclose(infile);
    queue_destroy(cola);
    free(almacen);
    free(productores);
    free(consumidores);
    free(total_argumentos_c);
    free(total_argumentos_p);
    // Termina la ejecución    
    return 0;
}




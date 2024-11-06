//P2-SSOO-23/24

//  MSH main file
// Write your msh source code here

//#include "parser.h"
#include <stddef.h>			/* NULL */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>


#define MAX_COMMANDS 8


// files in case of redirection
char filev[3][64];

//to store the execvp second parameter
char *argv_execvp[8];

void siginthandler(int param)
{
	printf("****  Exiting MSH **** \n");
	//signal(SIGINT, siginthandler);
	exit(0);
}

/* myhistory */

/* myhistory */

struct command
{
  // Store the number of commands in argvv
  int num_commands;
  // Store the number of arguments of each command
  int *args;
  // Store the commands
  char ***argvv;
  // Store the I/O redirection
  char filev[3][64];
  // Store if the command is executed in background or foreground
  int in_background;
};

int history_size = 20;
struct command * history;
int head = 0;
int tail = 0;
int n_elem = 0;

void free_command(struct command *cmd)
{
    if((*cmd).argvv != NULL)
    {
        char **argv;
        for (; (*cmd).argvv && *(*cmd).argvv; (*cmd).argvv++)
        {
            for (argv = *(*cmd).argvv; argv && *argv; argv++)
            {
                if(*argv){
                    free(*argv);
                    *argv = NULL;
                }
            }
        }
    }
    free((*cmd).args);
}

void store_command(char ***argvv, char filev[3][64], int in_background, struct command* cmd)
{
    int num_commands = 0;
    while(argvv[num_commands] != NULL){
        num_commands++;
    }

    for(int f=0;f < 3; f++)
    {
        if(strcmp(filev[f], "0") != 0)
        {
            strcpy((*cmd).filev[f], filev[f]);
        }
        else{
            strcpy((*cmd).filev[f], "0");
        }
    }

    (*cmd).in_background = in_background;
    (*cmd).num_commands = num_commands-1;
    (*cmd).argvv = (char ***) calloc((num_commands) ,sizeof(char **));
    (*cmd).args = (int*) calloc(num_commands , sizeof(int));

    for( int i = 0; i < num_commands; i++)
    {
        int args= 0;
        while( argvv[i][args] != NULL ){
            args++;
        }
        (*cmd).args[i] = args;
        (*cmd).argvv[i] = (char **) calloc((args+1) ,sizeof(char *));
        int j;
        for (j=0; j<args; j++)
        {
            (*cmd).argvv[i][j] = (char *)calloc(strlen(argvv[i][j]),sizeof(char));
            strcpy((*cmd).argvv[i][j], argvv[i][j] );
        }
    }
}


/**
 * Get the command with its parameters for execvp
 * Execute this instruction before run an execvp to obtain the complete command
 * @param argvv
 * @param num_command
 * @return
 */
void getCompleteCommand(char*** argvv, int num_command) {
	//reset first
	for(int j = 0; j < 8; j++)
		argv_execvp[j] = NULL;

	int i = 0;
	for ( i = 0; argvv[num_command][i] != NULL; i++)
		argv_execvp[i] = argvv[num_command][i];
}


/**
 * Main sheell  Loop  
 */
int main(int argc, char* argv[])
{
	/**** Do not delete this code.****/
	int end = 0; 
	int executed_cmd_lines = -1;
	char *cmd_line = NULL;
	char *cmd_lines[10];

	if (!isatty(STDIN_FILENO)) {
		cmd_line = (char*)malloc(100);
		while (scanf(" %[^\n]", cmd_line) != EOF){
			if(strlen(cmd_line) <= 0) return 0;
			cmd_lines[end] = (char*)malloc(strlen(cmd_line)+1);
			strcpy(cmd_lines[end], cmd_line);
			end++;
			fflush (stdin);
			fflush(stdout);
		}
	}

	/*********************************/

	char ***argvv = NULL;
	int num_commands;

	history = (struct command*) malloc(history_size *sizeof(struct command));
	int run_history = 0;

    int Acc = 0;
    char buf[100];
    sprintf(buf, "%d", Acc);
    setenv("Acc", buf, 1);

	while (1) 
	{
		int status = 0;
		int command_counter = 0;
		int in_background = 0;
		signal(SIGINT, siginthandler);

		if (run_history)
    {   
        for (int i=0; argvv[i][0]!=NULL; i++){
            command_counter ++;
        }
        run_history=0;
    }
    else{
        // Prompt 
        write(STDERR_FILENO, "MSH>>", strlen("MSH>>"));

        // Get command
        //********** DO NOT MODIFY THIS PART. IT DISTINGUISH BETWEEN NORMAL/CORRECTION MODE***************
        executed_cmd_lines++;
        if( end != 0 && executed_cmd_lines < end) {
            command_counter = read_command_correction(&argvv, filev, &in_background, cmd_lines[executed_cmd_lines]);
        }
        else if( end != 0 && executed_cmd_lines == end)
            return 0;
        else
            command_counter = read_command(&argvv, filev, &in_background); //NORMAL MODE
    }
		//************************************************************************************************


		/************************ STUDENTS CODE ********************************/
       if (command_counter > 0) {
			if (command_counter > MAX_COMMANDS){
				printf("Error: Maximum number of commands is %d \n", MAX_COMMANDS);
			}
			else {
				// Print command
				//print_command(argvv, filev, in_background);

                int estado;
                int pid;
                int fd[command_counter-1][2];
                
                struct command comando;
                store_command(argvv, filev, in_background, &comando);
                     
                if (n_elem <= history_size ){
                    history[tail] = comando;
                    n_elem ++;
                    tail = (tail + 1) % history_size; // Protegemos el caso del comando #19
                }                    
                else {
                    history[head] = comando;
                    head = (head + 1) % history_size;
                    tail = (tail + 1) % history_size;
                }
                
                
                
                

                // Si tenemos más de un comando, creamos n-1 tuberías
                if (command_counter > 1)
                    {
                    for (int i = 0; i < command_counter - 1; i++) {
                        if (pipe(fd[i]) == -1) {
                            perror("Error al crear la tubería");
                            return -1;}
                    }}

                for (int i = 0; i < command_counter; i++){

                    if (strcmp(argvv[i][0], "mycalc") == 0){
                        mycalc(argvv, i, Acc); //Llamamos a la funcion

                        for( int i= 0; i < 4; i++){ //Limpiamos el argvv manualmente por un bug del parser
                            argvv[0][i]= NULL;
                        }
                        
                    }

                    else if (strcmp(argvv[i][0], "myhistory") == 0){
                        if (argvv[i][1] != NULL && history[atoi(argvv[i][1])].argvv != NULL ){  //Si nos dan un argumento numero entre 0 y 19 y esta lleno
                            if (atoi(argvv[i][1]) >= 0 && atoi(argvv[i][1]) <= 19){             //Cambiamos run_history a 1 para evitar el parser y ejecutar             
                                run_history = 1;                                                //el comando de la linea
                            }                                                    
                        }
                        myhistory(argvv, i);    //Llamamos a la funcion

                    }   
                    else{   

                        // Ejecución estándar de un comando, fork para la ejecución del proceso
                        pid = fork();
                        switch (pid){
                            
                            // Caso de error
                            case -1:
                                perror("Error en el fork");
                                return -1;

                            // Caso del hijo
                            case 0:

                                if (strcmp(filev[2], "0") != 0) {
                                    close(STDERR_FILENO);
                                    if (open(filev[2], O_CREAT | O_TRUNC | O_WRONLY, 0666)==-1){
                                        perror("Error de salida de errores");
                                        return -1;
                                    }}

                                // Si no se trata del primer comando, modificar fichero de entrada
                                if (i!=0) {
                                    // Cerramos fichero estándar
                                    close(STDIN_FILENO);
                                    // Duplicamos el fichero de nuestra pipe (ahora en el "hueco" que ha dejado el estandar)
                                    dup(fd[i-1][0]);
                                    close(fd[i-1][0]);
                                    close(fd[i-1][1]);}
                                // Aprovechamos para actualizar redirección si es necesario el fichero de entrada si es el primer comando
                                else if (strcmp(filev[0], "0") != 0){
                                    close(STDIN_FILENO);
                                    if(open(filev[0], O_RDONLY)==-1){
                                        perror("Error de entrada");

                                        // Es importante cerrar el fichero de error en caso de que el proceso tenga que terminar para evitar problemas de salida
                                        close(STDERR_FILENO);
                                        return -1;
                                    }
                                }
                                
                                // Caso análogo para el fichero de salida
                                if (i!=command_counter-1){
                                    close(STDOUT_FILENO);
                                    dup(fd[i][1]);
                                    close(fd[i][0]);
                                    close(fd[i][1]);}
                                    
                                else if (strcmp(filev[1], "0") != 0) {
                                    close(STDOUT_FILENO);
                                    // Lo truncamos o creamos con read and write
                                    if (open(filev[1], O_CREAT | O_TRUNC | O_WRONLY, 0666)==-1){
                                        perror("Error de salida");
                                        close(STDERR_FILENO);
                                        return -1;
                                    }
                                }
                                
                                // Ejecutamos la instrucción en cuestión
                                if (execvp(argvv[i][0], argvv[i])){
                                    perror("Error al ejecutar la instrucción");
                                    close(STDERR_FILENO);}

                                break;
                                
                           
                            default:
                                // Caso del padre

                                if (i!=0)
                                    // Si no es el primer comando cierro la pipe utilizada
                                    {close(fd[i-1][0]);
                                    close(fd[i-1][1]);}

                                if (in_background == 1 && i == command_counter-1) {
                                    printf("%d\n", pid);} 

                                else if (wait(&estado) == -1) {
                                    perror("Error en el wait");
                                    return -1;}
                                break;

                        }
                    }
                }
                    
            }
        }
    }       
	return 0;
}
int mycalc(char ***argvv, int i, int Acc){
    int operando_1;
    int operando_2;
    // sacamos los numeros a operar del argvv
    operando_1 = atoi(argvv[i][1]);
    operando_2 = atoi(argvv[i][3]);

    //sacamos el operador a usar de argvv                    
    char operador[3];
    strcpy(operador, argvv[i][2]);
    int resultado;

    //Comparamos el operador con add mul o div si no es uno de esos sacamos error            
    if (strcmp(operador, "add") == 0){
        Acc = atoi(getenv("Acc"));  //Parala suma recuperamos la variable de entorno
        resultado = operando_1 + operando_2;    //Operamos
        Acc += resultado;
        char buf[100];
        fprintf(stderr, "[OK] %d + %d = %d; Acc %d\n", operando_1, operando_2, resultado, Acc); //Imprimimos el resultado
        sprintf(buf, "%d", Acc); //Cambiamos la variable a str de nuevo
        setenv("Acc", buf, 1);  //Seteamos la variable de entorno
    }
                            
    else if (strcmp(operador, "mul") == 0){
        resultado = operando_1 * operando_2; //Operamos
        fprintf(stderr, "[OK] %d * %d = %d\n", operando_1, operando_2, resultado); //Imprimimos el resultado
    }
                            
    else if (strcmp(operador, "div") == 0){
        resultado = operando_1 / operando_2; //Operamos
        int resto = operando_1 % operando_2;
        fprintf(stderr, "[OK] %d / %d = %d; Resto %d\n", operando_1, operando_2, resultado, resto); //Imprimimos el resultado
    }

    else {
        printf("[ERROR] La estructura del comando es mycalc <operando_1> <add/mul/div> <operando_2>\n"); //Error de formato
        return -1;
    }
}

int myhistory(char ***argvv, int i) {
    //Miramos si el myhistory tiene algun argumento despues
    if (argvv[i][1]==NULL){ //No tiene argumentos
        for (int i = 0; i < n_elem-1; i++){ //Iteramos en el numero de elementos a imprimir
            fprintf(stderr, "%d ", i); //Imprimimos el numero
            for (int j=0; j < history[i].num_commands; j++){ //Iteramos en el numero de comandos de cada linea                       
                                    
                for (int m=0; m < history[i].args[j]; m++){ //Iteramos en el numero de argumentos de cada comando
                    fprintf(stderr, "%s ", history[i].argvv[j][m]); //Imprimimos todos los comandos con sus argumentos
                }

                if (j == history[i].num_commands - 1) fprintf(stderr, "\n"); //Salto de linea al terminar cada elemento
                else fprintf(stderr, "| "); //Separador si hay varios comandos en cada linea
            }    
        }
    }
                    
    else if ( atoi(argvv[i][1]) >= 0 && atoi(argvv[i][1]) <= 19){ //Tiene argumento numero entre 0 y 19
        if (history[atoi(argvv[i][1])].argvv == NULL){ //Miramos si el numero del argumento tiene algun comando
            printf("ERROR: Comando no encontrado\n"); //Si no hay nada error

            return -1 ;                      
        }
        else{ 
            int num = atoi(argvv[i][1]);  //sacamos el numero que nos pasan cmo argumento
            fprintf(stderr, "Ejecutando el comando %d\n", num); //Imprimimos
                                                                                                   
            argvv[0][0]=NULL; //Limpiamos el argvv
            argvv[0][1]=NULL;
            
            for (int j=0; j < history[num].num_commands; j++){ //Rellenamos el argvv con el comando que tenemos que ejecutar
                for (int m=0; m < history[num].args[j]; m++){ 
                    argvv[j][m]= history[num].argvv[j][m];
                }
            }
        }                      
    }
    else {
        printf("ERROR: Comando no encontrado\n"); //Error si el numero no esta entre 0 y 19
        return -1;
    }
}
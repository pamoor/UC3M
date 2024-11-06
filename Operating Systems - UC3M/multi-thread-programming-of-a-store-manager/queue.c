#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include "queue.h"

// Función para inicializar una cola, con el tamaño como parámetro
queue* queue_init(int size) {
    queue *q = (queue *)malloc(sizeof(queue)); // Reserva de memoria para la cola
    if (q == NULL) {
        printf("Error: No se pudo asignar memoria para la cola.\n");
        exit(-1);
    }
    q->array = (struct element *)malloc(size * sizeof(struct element)); // Reserva de memoria para todas las posiciones del buffer
    if (q->array == NULL) {
        printf("Error: No se pudo asignar memoria para todos los elementos de la cola.\n");
        exit(-1);
    }
    q->size = size;
    q->head = -1; // Cabecera del buffer
    q->tail = -1; // Cola del buffer
    return q;
}

// Función para destruir la cola y liberar la memoria ocupada
int queue_destroy(queue *q) {
    if (q == NULL) {
        printf("Error: La cola no está inicializada.\n");
        return -1;
    }
    free(q->array);
    free(q);
    return 0;
}

// Función para verificar si la cola está vacía
int queue_empty(queue *q) {
    return q->head == -1;
}

// Función para verificar si la cola está llena
int queue_full(queue *q) {
    return (q->tail + 1) % q->size == q->head;
}

// Función para encolar un elemento
int queue_put(queue *q, struct element* elem) {
    if (queue_full(q)) {
        printf("La cola está llena. No se puede encolar.\n");
        return -1;
    }
    if (queue_empty(q))
        q->head = 0;
    q->tail = (q->tail + 1) % q->size;
    q->array[q->tail] = *elem; // El elemento se añade en la cola (FIFO)
    return 0;
}

// Función para desencolar un elemento
struct element* queue_get(queue *q) {
    if (queue_empty(q)) {
        printf("La cola está vacía. No se puede desencolar.\n");
        return NULL;
    }
    struct element *operacion = &(q->array[q->head]);
    if (q->head == q->tail) {
        // La cola tiene solo un elemento
        q->head = -1;
        q->tail = -1;
    } else {
        q->head = (q->head + 1) % q->size; // El elemento se extrae de la cabecera (FIFO)
    }
    return operacion;
}
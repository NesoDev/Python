# importamos las librerias
import random
from pyray import *
from raylib import KEY_ESCAPE, KEY_SPACE

# definimos las dimensiones de la ventana
ancho = 1700
alto = 800

# ingresamos la cantidad de elementos
n = int(input("Cantidad de elementos : "))

# creamos una lista con elementos aleatorios
lista_apoyo = []
lista_aleatoria = []
for i in range(n):
    lista_aleatoria.append(random.randint(100, 800))
    lista_apoyo.append(lista_aleatoria[i])

# definimos variables para la gráfica
ancho_barra = 10
espacio = int((ancho - n*ancho_barra) / (n - 1))

# definimos flags
flag = False
flag_2 = True

# iniciamos una ventana
init_window(ancho, alto, "QUICK SORT")

# definimos una funcion que grafique la lista
def graficar():
    for i in range(len(lista_aleatoria)):
        draw_rectangle(i*(ancho_barra+espacio), alto-lista_aleatoria[i], ancho_barra, lista_aleatoria[i], GREEN)

# definimos una funcion que ordene la lista con bubblesort
def bubbleSort():
    for i in range(n-1):
        clear_background(BLACK)
        if lista_aleatoria[i] > lista_aleatoria[i+1]:
            var_aux = lista_aleatoria[i]
            lista_aleatoria[i] = lista_aleatoria[i+1]
            lista_aleatoria[i+1] = var_aux
        if is_key_pressed(KEY_ESCAPE):
            flag_2 = False
            break

# definimos una funcion que ordene la lista con insertionsort
def insertionSort():
    for i in range(1, len(lista_aleatoria)):
        clear_background(BLACK)
        graficar()
        key = lista_aleatoria[i]
        j = i - 1
        while j >= 0 and key < lista_aleatoria[j]:
            lista_aleatoria[j+1] = lista_aleatoria[j]
            j -= 1
        clear_background(BLACK)
        graficar()
        lista_aleatoria[j+1] = key
        end_drawing()

# definimos una funcion que ordene la lista con quicksort
def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x <= pivot]
        right = [x for x in array[1:] if x > pivot]
        return quickSort(left) + [pivot] + quickSort(right)

# mantenemos abierta la ventana iniciada
while not window_should_close():
    clear_background(BLACK)
    if is_key_pressed(KEY_SPACE) or flag: 
        flag = True
        insertionSort()
    graficar()
    end_drawing()

# finalizamos la ventana
close_window()

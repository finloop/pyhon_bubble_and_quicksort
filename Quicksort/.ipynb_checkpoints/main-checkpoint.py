# Zwraca indeks taki że, po lewej stronie są wartości mniejsze od niego, a po prawej większe.
def partition(tab, low, high):
    # Wybieram indeks high jako wartość względem której będę porównywał elementy i nazwę ją pivot.
    pivot = tab[high]
    # mid to indeks pivot, za którym będą znajdować się wartości większe od pivot.,
    #na początek ustawiam go na pierwszą wartość.
    mid = low
    # Dla każdego elementu w zakresie low-high
    for i in range(low, high):
        # Jeżeli wartość w tablicy jest mniejsza od pivot
        if tab[i] < pivot:
            # Zamieniam miejscami w tablicy obecną wartość z mid
            tab[i], tab[mid] = tab[mid], tab[i]
            # zwiększam mid o 1
            mid+=1
    tab[mid], tab[high] = tab[high], tab[mid]
    return mid
            
    
def quicksort(tab, low, high):
    if low < high:
        mid = partition(tab,low,high)
        quicksort(tab,low,mid-1)
        quicksort(tab,mid+1,high)
        
        
import random
tab = [random.randrange(1,10) for i in range(0,10)]
print(tab)
z = tab
q = quicksort(tab, 0, len(tab) - 1)
print(z)
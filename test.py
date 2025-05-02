import random
import time
from merge import mergeSort
from select import selectSort

def createList(size):
    numbers = [0] * size
    for i in range(size):
        numbers[i] = random.random() * 10
    return numbers

def getTimeMerge(arr):
    start = time.perf_counter()
    mergeSort(arr, 0, len(arr) - 1)
    finish = time.perf_counter()
    return finish - start

def getTimeSelect(arr):
    start = time.perf_counter()
    selectSort(arr)
    finish = time.perf_counter()
    return finish - start

for i in range(0, 7):
    print(f'Тест на {pow(2, i)*500} элементов')
    print('Время работы сортировки слиянием: ' + str(getTimeMerge(createList(pow(2, i)*500))))
    print('Время работы сортировки выборкой: ' + str(getTimeSelect(createList(pow(2, i)*500))))
def merge(arr, left, mid, right):
    # вычисляем длину левого и правого списков (контейнеров)
    n1 = mid - left + 1
    n2 = right - mid
    
    # создаем левые и правые списки (контейнеры)
    L = [0] * n1
    R = [0] * n2
    
    # переносим элементы 
    for i in range (n1):
        L[i] = arr[left + i]
    for j in range (n2):
        R[j] = arr[mid + 1 + j]
    
    # инициализируем итераторы для левого, правого и конечного списков 
    it1 = 0
    it2 = 0
    itres = left
    
    # возвращаем элементы в массив, предварительно сравнив их
    while it1 < n1 and it2 < n2:
        if L[it1] <= R[it2]:
            arr[itres] = L[it1]
            it1 += 1
        else:
            arr[itres] = R[it2]
            it2 += 1
        itres += 1
    
    # добавляем оставшиеся элементы левого списка
    # если такие есть
    while it1 < n1:
        arr[itres] = L[it1]
        it1 += 1
        itres += 1
        
    # добавляем оставшиеся элементы правого списка
    # если такие есть
    while it2 < n2:
        arr[itres] = R[it2]
        it2 += 1
        itres += 1
        
# Рекурсивный алгоритм сортировки слиянием
# Функция сортирует подотрезок массива с индексами в полуинтервале [left:right)
def mergeSort(arr, left, right):
    if left < right:
        # Вычисляем индекс элемента посередине 
        mid = (left + right) // 2
        
        # Рекурсивный вызов себя же
        mergeSort(arr, left, mid)
        mergeSort(arr, mid +1, right)
        # Слияние констейнеров
        merge(arr, left, mid, right)
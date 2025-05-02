from merge import mergeSort

# Функция, выводящая элементы списка
# Аргумент 'arr' - список
def print_list(arr):
    for i in arr:
        print(i, end = ' ')
    print()

# Тестовая функция
def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print_list(arr)
    
    mergeSort(arr, 0, len(arr) - 1)
    
    print("Sorted array is")
    print_list(arr)
    
if __name__ == "__main__":
    main()
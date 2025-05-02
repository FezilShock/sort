from select import selectSort

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
    
    selectSort(arr)
    
    print("Sorted array is")
    print_list(arr)
    
if __name__ == "__main__":
    main()
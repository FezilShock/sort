def selectSort(x):
    for ind1 in range(len(x) - 1):                  # Берем индекс первого элемента
        for ind2 in range(ind1 + 1, len(x)):        # Индекс второго элемента
            if x[ind1] > x[ind2]:                   # Если значение, индекс которого больше, оказывается меньше
                x[ind1], x[ind2] = x[ind2], x[ind1] # То меняем значени местами


def inputArray(length, message):
    array = []
    for i in range(length):
        array.append(input(message))
    return array

def returnOnlyShortElements(array):
    i = 0
    j = 0
    new_array = []
    while i < len(array):
        if len(array[i]) <= 3:
            new_array.insert(j, array[i])
            j += 1
        i += 1
    print(new_array)

array_length = int(input("Введите длину массива: "))
array = inputArray(array_length, "Введите элемент массива: ")
returnOnlyShortElements(array)
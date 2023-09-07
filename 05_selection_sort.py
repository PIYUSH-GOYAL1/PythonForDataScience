def selection_sort(array):
    n = len(array)
    for i in range (n-1):
        min_index = i
        for j in range (i+1, n):
            if array[j] < array[min_index]:
                min_index = j
            array[i] , array[min_index] = array[min_index] , array[i]

string_1 = input("Enter the list of numbers separated by spaces: ")

numbers = [int(num) for num in string_1.split(" ")]

selection_sort(numbers)
print(numbers)
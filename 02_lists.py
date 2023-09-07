list_1 = list()
list_2 = list()

length_1 = int(input("Enter length of list 1 : "))

for i in range (length_1):
    list_1.append(int(input("Enter element: ")))

length_2 = int(input("Enter length of list 1 : "))

for j in range(length_2):
    list_2.append(int(input("Enter the element: ")))

list_1 += list_2

print(list_1)
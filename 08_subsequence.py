string_1 = input("Enter a sentence: ")

vowels = ['a','e','i','o','u']
result = [letter for letter in string_1 if letter.lower() not in vowels]
result = ''.join(result)
print(result)

list_1 = list(result.split(" "))
list_3 = list()


for i in range(len(list_1)):
    list_2 = list(list_1[i])
    list_3.append(len(list_2))

ind = 0
max_element = list_3[0]
 
for i in range (1,len(list_3)):
  if list_3[i] > max_element:
    max_element = list_3[i]
    ind = i
print("Index of the maximum element in the list is: ",ind)


print(ind)
print("Longest Common Subsequence:")
print(list_1[ind])


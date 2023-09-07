string_1 = input("Enter a sentence: \n")
sentence = string_1.split(" ")
for i in sentence:
    print(i.capitalize(), end=" ")
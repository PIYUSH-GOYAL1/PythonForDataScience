number = int(input("Enter a number: "))

# Recursion Method To Find The Binary Equivalent Of The Given Decimal Number

def convert(number):
        if number >= 1:
            convert(number // 2)
            print (number % 2 , end=' ')

convert(number)

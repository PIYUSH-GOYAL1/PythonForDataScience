subject_1 = int(input("Enter marks of subject 1 : "))
subject_2 = int(input("Enter marks of subject 2 : "))
subject_3 = int(input("Enter marks of subject 3 : "))

average = (subject_1 + subject_2 + subject_3)/3

if (average <= 40):
    print("FAIL")
else:
    print("PASS")

input1=input("Enter the first string :")
input2=input("Enter the second string :")

for i in range(len(input1)):
    if input1[i] in input2:
        print(input1[i])
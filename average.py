total=0
count=0
average=0
print("Average of numbers")
print("To stop the loop type 0")
#i=int(input("Enter the i :"))
#n=int(input("Enter the number limit :"))

while True:
    i=int(input("Enter the number :"))
    count+=1
    total=total+i
    average=total/count
    if i==0:
        break
    i+=1

print("Total is :",total)    
print("Average is :",average)
print("Count is :",count)
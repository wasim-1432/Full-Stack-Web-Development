x=int(input("Enter any number\n"))
count=0
y=str(x)
z="0123456789"
for i in y:
    for j in z:
        if i==j:
            count+=1
print("Total Digits in a given number=",count)
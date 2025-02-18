x=int(input("Enter any number\n"))
sum=0
while x:
    sum=sum+x%10
    x=x//10
print("Sum of digits=",sum)
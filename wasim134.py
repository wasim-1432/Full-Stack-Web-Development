print("Enter the year")
x=int(input())
if x%100==0:
    if x%400==0:
        print("Leap Year")
else:
    if x%4==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
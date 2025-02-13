x=int(input("Enter an number\n"))
match x:
    case x if 99<x<1000:
        print("Three Digit Number")
    case x:
        print("Not Three Digit Number")
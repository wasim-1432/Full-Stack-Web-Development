x=int(input("Enter any number\n"))
match x:
    case x if x>0:
        print("Positive Number")
    case x if x<0:
        print("Negative Number")
    case x if x==0:
        print("Zero")
    case _:
        print("Default Value")
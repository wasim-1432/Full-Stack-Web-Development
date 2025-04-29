s=input("Enter any string\n")
for i in s:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        pass
    else:
        print("String has some other characters other than alphabets")
        break
else:
    print("String has only alpabhets characters")
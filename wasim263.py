s=input("Enter any string\n")
ch=input("Enter any character\n")
for i in s:
    if ch==i:
        print("Present")
        break
else:
    print("Not Present")
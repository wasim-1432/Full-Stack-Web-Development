x=input("Enter any string\n")
l1=[]
for e in x:
    if not e.isalpha() and e!=' ':
        l1.append(e)
print(l1)
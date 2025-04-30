x=input("Enter any string\n")
l1=[e for e in x.split(' ') if e!=0]
length=[len(i) for i in l1]
print(l1[length.index(max(length))])
l1=[int(e) for e in input("Enter the numbers with comma\n").split(',')]
s1=set()
s2=set()
for i in l1:
    if i%2==0:
        s1.add(i)
    else:
        s2.add(i)
print(s1)
print(s2)
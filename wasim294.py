x=["Mumbai","Lucknow","Bharatpur","Bazara"]
temp=[]
mylist=[]
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x.sort()
for i in range(0,26):
    temp.clear()
    for j in x:
        if j.startswith(alpha[i]):
            temp.append(j)
    if len(temp)>0:
        mylist.append(tuple(temp))
print(mylist)
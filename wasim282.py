x=input("Enter any string\n")
l1=[e for e in x]
l2=[]
i=0
j=0
while i<=len(l1)-1:
    if l1[i] not in l2:
        j=0
        count=0
        while j<=len(l1)-1:
            if l1[i]==l1[j]:
                count+=1
            j+=1
        print(l1[i],count)
        l2.append(l1[i])
    i+=1

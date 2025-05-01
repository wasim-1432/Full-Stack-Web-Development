x=['Noida','Siddharthnagar','Mumbai','Siddharthnagar']
l1=[e for e in x]
i=0
while i<=len(l1)-1:
    count=0
    j=0
    while j<=len(l1)-1:
        if x[i]==l1[j]:
            count+=1
            if count==2:
                break
        j+=1
    if count==2:
        break
    i+=1
if count==2:
    print("Repeated string=",l1[i])
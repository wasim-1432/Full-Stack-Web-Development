x=['AB','BC','BC']
i=0
for e in x:
    if x.index(e)!=i:
        print("First repeated string=",x[i])
        break
    i+=1

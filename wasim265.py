x=input("Enter any string\n")
count=0
for i in x:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        count+=1
print("Total words in a given string is=",count)
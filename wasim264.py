x=input("Enter any string\n")
vowels="aeiouAEIOU"
count=0
for i in x:
    if i in vowels:
        count+=1
print("Total Vowels is=",count)
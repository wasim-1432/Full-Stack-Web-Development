x=input("Enter any string\n")
y="AEIOUaeiou"
print("Vowels in a given string")
for i in x:
    for j in y:
        if i==j:
            print(i,end='')
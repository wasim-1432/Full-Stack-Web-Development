def Count_Words_In_A_Given_String(s):
    count=1
    for i in s:
        if i==' ':
            count+=1
    return count
print("Enter any string")
s=input()
print("Total words in a given string=",Count_Words_In_A_Given_String(s))
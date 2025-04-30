s1=input("Enter any string\n")
print(' '.join([e for e in s1.split(' ') if e!=' '][::-1]))
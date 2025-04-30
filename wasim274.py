s1=input("Enter any text\n")
print([eval(x) for x in [e for e in s1.split(' ') if e!=' '] if x.isdigit() or not x.isalpha() and type[eval(x)==float]])
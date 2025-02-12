print("Enter the value of a,b & c")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("Two real Contant")
elif d==0:
    print("Two distinct real root")
else:
    print("Imaginary Roots")
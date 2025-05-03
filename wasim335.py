def Check_Leap_Year(year):
    if year%4==0:
        return True
    elif year%400==0:
        return True
    else:
        return False
year=int(input("Enter any number\n"))
print("Required answer=",Check_Leap_Year(year))
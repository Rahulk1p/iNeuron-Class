'''1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between
2000 and 3200 (both included). The numbers obtained should be printed  in a comma-separated sequence on a single
line.'''
lst = []
for x in range(2000,3201):
    print(x)
    if x % 7 == 0 :
        if x % 5 != 0:
            lst.append(x)
print(str(lst).lstrip('[').rstrip(']'))

'''2.Write a Python program to accept the user's first and last name and then getting them printed 
in the the reverse order with a space between first name and last name. '''

first_name = input("Enter First Name = ")
last_name = input("Enter Last Name = ")
name = first_name +" "+last_name
print(name[::-1])

'''3. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3 '''
def volume(diameter):
    pi = 3.1415926535897931
    radius = diameter /2
    return (4/3)*pi*(radius ** 3 )
print(volume(12))

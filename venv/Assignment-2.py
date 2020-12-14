"""
1. Create the below pattern using nested for loop in Python.
*
**
***
****
*****
****
***
**
*
"""
control = 0
pattern = ""
for i in range(5*2):
    pattern = ""
    if (i > 5):
        control = control - 1
    else:
        control = control + 1

    for j in range(control - 1):
        pattern = pattern + "*"
    print(pattern)


#Write a Python program to reverse a word after accepting the input from the user.

#Input word: ineuron
#Output: norueni
word = input("Enter the Word =")
print(word[::-1])



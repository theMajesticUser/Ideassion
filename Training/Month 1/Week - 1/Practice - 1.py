#Q - Declare an array with series of random numbers then choose an number. Check if the adddition of two numbers is equal to the chosen number.

# inputs
a = [1,2,3,4,5,6,7,8]
b = 6

# function [sumfind] to find sum of two numbers x,y in a[] which results in b and x is not equal to y to avoid repetition of same numbers
# position of combinations using array.index() are stored in postiton[]

def sumfind(a, b):
    position =[]
    resultant=[]#excess
    for x in a:
        for y in a :
            if x!=y :
             if x + y == b:
                position.append((a.index(x), a.index(y)))
                resultant.append((x,y))#excess
    print("Results  : ",resultant)#excess
    print("Position : ",position)
# call function
sumfind(a, b)

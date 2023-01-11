#Q - Enter an input number and find all prime numbers less than the input number.

def prime(a):
    for num in range(2, a+1):
        # all prime numbers are greater than 1
        for i in range(2, num):
          # if divided by itself gives 0 as remainder not an prime number
            if (num % i) == 0:
                break
        else:
            print(num)
# Taking an input number from the user
a = int(input("Enter an number : "))
# Calling function
prime(a)
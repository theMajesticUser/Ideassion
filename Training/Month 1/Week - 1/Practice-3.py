#Q- Get an number and reverse it wihhout using libraries.

#get number
Original_Number = int(input("Enter Number: "))
#Declare reverse to store the reversed number
Reverse_Number = 0
#create an loop to run until original number is greater than 0.
while(Original_Number > 0):
#Using % to separate the last number from the combined number, Any number divided by 10 gives remainder of last number unless its 0
 Remainder = Original_Number %10
 #To store the reverse number 
 Reverse_Number = (Reverse_Number *10) + Remainder
 #To remove last digit from original number
 Original_Number = Original_Number //10
 #Display
print("Reverse : " ,Reverse_Number)

#Checking the valid input
while True:
    num = input("Please enter a number ")
    try:
        val = int(num)
        print("Input is an integer number.")
        print("Input number is: ", val)
        break;
    except ValueError:
        print("enter the valid number")


#Changing long integer in to list to perform operation
res = list(map(int, str(val)))
##print ("The list from number is " + str(res))
sumof = sum(res)
print("The sum of the integer  is " , sumof)
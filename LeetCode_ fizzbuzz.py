
n = 5
rangeOfList = range(1,n+1)
list1 = list(rangeOfList)
print(list1)


condition1 = "FizzBuzz"
condition2 = "Fizz"
condition3 = "Buzz"

for i in range(len(list1)):
    if list1[i] % 3 == 0 and list1[i] % 5 == 0:
        list1[i] = condition1

    elif list1[i] % 3 == 0:
        list1[i] =condition2

    elif list1[i] % 5 == 0:
        list1[i] =condition3

print(list1)
myList = list(map(str,list1))
print(myList)
print(myList.__repr__().replace("'",'"')) 
#loops repeat a block of code multiple times
#while loops repeats a block of code as long as a condition is true 
#for loops repeats a block of code a specific number of times
list1 = range(1, 1001)
# print(list1)
for number in list1:
    if number % 2 == 0:
        print(f'number is even {number}')
else:
    print("this number is not even")
#sum
print(f'the sum of the list is {sum(list1)}')
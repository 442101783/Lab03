numbers_list = []
i = 0
j = 10
for i in range(10):
    print("enter 10 numbers")
    numbers_list.append(input())
numbers_list.sort()
print("the largest number in the list is ",numbers_list.pop())    
    
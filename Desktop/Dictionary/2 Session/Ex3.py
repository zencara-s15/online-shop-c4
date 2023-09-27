# Ex3 - Array number
# arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]

#1 - Reverse array
arr = [10, 3, 4, 8, 9, 4, 5, 3, 5]
LastIndex = len(arr) -1
result = 0
arr1 = []
for i in range(len(arr)):
    result += arr[LastIndex-i]
arr1.append(result)
print(arr1)





#2 - Remove duplicate value
#3 - replace numebr > 3 with 0
#4 - Find average of odd number
#6 - remove number 8, 9, 10
# ----------
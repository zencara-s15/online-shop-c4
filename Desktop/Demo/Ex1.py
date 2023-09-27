number = "68 10 1 2 30"
sum = 0
res = ""
for i in range(len(number)):
    if number[i] == " " or i == len(number) -1:
        if i == len(number) -1:
            res += number[i]
        sum += int(res)
        res = ""
    else:
        res += number[i]
print(sum)
text = "apple is the best"
res = ""
isFound = False
for i in range(len(text)):
    if i == 0:
        res += text[i].upper()
    elif text[i] == " ":
        isFound = True
        res += text[i].upper()
    elif isFound:
        res += text[i].upper()
        isFound = False
    else:
        res += text[i]
print(res)

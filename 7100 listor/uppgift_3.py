word = input("Skriv ett ord")

result = ""
for i in word:
    if i not in "aeiouåäö":
        result += i + "o" + i
    else:
        result += i

print("Översatt till rövarspråket", result)

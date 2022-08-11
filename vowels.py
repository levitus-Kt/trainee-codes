import libs
text = input("Ломаем хейт \n")
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for i in range(0, len(vowels)):
    text = text.replace(vowels[i], '')
print(text)
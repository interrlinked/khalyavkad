string1 = input("Введіть перший рядок символів: ")
string2 = input("Введіть другий рядок символів: ")

common_chars = set(string1) & set(string2)

print("Спільні символи:", end=" ")
for char in common_chars:
    print(char, end=" ")

string = input("Введіть рядок слів, розділених пробілами: ")

words = string.split()
longest_word = max(words, key=len)
word_length = len(longest_word)

print("Найдовше слово:", longest_word)
print("Довжина найдовшого слова:", word_length)

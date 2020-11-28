letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  count = []
  for letter in word:
    if letter not in count:
      count.append(letter)
  return len(count)
# Uncomment these function calls to test your function:
# print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
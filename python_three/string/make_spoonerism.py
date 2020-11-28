# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  first_letter_word1 = word1[0]
  first_letter_word2 = word2[0]
  # print(first_letter_word1, first_letter_word2)
  first = word1.replace(word1[0], first_letter_word2)
  second = word2.replace(word2[0], first_letter_word1)
  # print(first, second)
  spoonerism = first + ' ' + second
  return spoonerism

print(make_spoonerism("Belly", "Jeans"))
# print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
# print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
# print(make_spoonerism("a", "b"))
# should print b a
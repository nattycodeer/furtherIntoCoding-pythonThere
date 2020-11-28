# Write your every_other_letter function here:
def every_other_letter(word):
  other_letters_in_word = ''
  for i in range(0, len(word), 2):
    word_skip = word[i]
    other_letters_in_word += word_skip
  return other_letters_in_word

# print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
# print(every_other_letter(""))
# should print

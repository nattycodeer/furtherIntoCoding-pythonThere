# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word) < 20:
    word_exclamation = word + '!' * len(word)
    return word_exclamation
  return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
# print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
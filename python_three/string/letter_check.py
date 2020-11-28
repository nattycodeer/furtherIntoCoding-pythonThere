def letter_check(word, letter):
  for item in word:
    if item == letter: #a == y
      return True
  return False
print(letter_check('cake', 'y'))
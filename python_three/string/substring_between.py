# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_char = word.find(start)
  end_char = word.find(end)

  if start and end in word:
    return word[start_char+1:end_char]
  else:
    return word

# Uncomment these function calls to test your function:
# print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
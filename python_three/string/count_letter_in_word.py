# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for letter in word:
    if x == letter:
      count += 1
  return count
# Uncomment these function count_char_xcalls to test your tip function:
print(count_char_x("mississippi", "s"))
# print(count_char_x("mississippi", "i"))
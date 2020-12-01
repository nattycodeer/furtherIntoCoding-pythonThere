letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = letter_to_points.pop(" ", 0)
# print(letter_to_points)

def score_word(word):
  point_total = 0
  # print(letter_to_points.keys())
  for i in word:
    if i not in letter_to_points.keys():
      # print(letter_to_points[" "])
      point_total += letter_to_points[" "]
    else:
       point_total += letter_to_points[i]
  return point_total

# print(score_word("$NATTY"))
brownie_points = score_word("BROWNIE")
print(brownie_points)
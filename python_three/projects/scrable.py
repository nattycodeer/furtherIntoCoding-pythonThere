letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = letter_to_points.pop(" ", 0)
print(letter_to_points)

# Fucntion adds words to a list the player played for
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
# brownie_points = score_word("BROWNIE")
# print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "worldNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Function 
def play_word(player, word):
  player_to_words = {}
  player_to_words[player] = word
  return player_to_words

# play_word('Player1', ['Minecraft' , 'Mario', 'Pokemon'])
# player_to_points = {}
# for player, words in player_to_words.items():
#   player_points = 0
#   for word in words:
#     player_points += score_word(word)
#   player_to_points[player] = player_points
# print(player_to_points)


# Fucniton Update total ponits
def update_point_totals():
  player_to_points = {}
  player_to_words = play_word('Player3', ['$Kirby', 'Pokemon'])
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      word = word.upper()
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points
  
print(update_point_totals())

# players = input('Enter player name: ')
# words_played = input('Enter words: ')


# Output
# {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}
# {'Player3': 32}

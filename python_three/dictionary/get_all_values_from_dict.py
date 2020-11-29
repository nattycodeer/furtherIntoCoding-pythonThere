num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for exercise in list(num_exercises.values()):
  total_exercises += exercise
print(total_exercises)
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  pop_student = all_students.pop()
  students_in_poetry.append(pop_student)
print(students_in_poetry)
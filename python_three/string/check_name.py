# Write your check_for_name function here:
def check_for_name(sentence, name):
  lst = sentence.split(' ')
  for word in lst:
    if name.lower() == word.lower():
      return True
  return False


# print(check_for_name("My name is Jamie", "Jamie"))
# should print True
# print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
#Write your function here
def add_greetings(names):
  greetings = []
  for name in names:
    name = 'Hello, ' + name #  'Hello, ' + "Owen" = 'Hello, Owen'
    greetings.append(name)
  return greetings
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


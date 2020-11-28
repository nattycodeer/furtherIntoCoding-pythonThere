def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4] # LenRupr
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
    return username

  return username
print(username_generator('Ho', 'Hup'))
# print(username_generator('Lerina', 'Chetee'))
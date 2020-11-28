def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4] # LenRupr
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
    return username

  return username
# print(username_generator('Ho', 'Hup'))
print('Username: ', username_generator('Abe', 'Simpson'))

# Password Generator Machine:
def password_generator(username):
  password = ''
  for i in range(0, len(username)):
      password += username[i - 1]
  return password

uname = username_generator('Abe', 'Simpson')
print('Password: ', password_generator(uname))

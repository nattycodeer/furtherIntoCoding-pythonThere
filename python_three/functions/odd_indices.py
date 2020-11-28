#Write your function here
def odd_indices(lst):
  new_lst = []
  for idx in range(len(lst)):
    if idx % 2 != 0:
      new_lst.append(lst[idx])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

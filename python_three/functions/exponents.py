#Write your function here
def exponents(bases, powers):
  exp_lst = []
  for base in bases:
    for power in powers:
      item = base ** power
      exp_lst.append(item)

  return exp_lst

# comprehension list solution
# exp_lst = [base ** power for base in bases for power in powers]
# return exp_lst
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

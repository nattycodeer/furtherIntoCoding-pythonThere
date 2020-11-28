#Write your function here
def over_nine_thousand(lst):
  lst_sum = 0
  for num in lst:
    lst_sum += num
    if lst_sum > 9000:
      break
  return lst_sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
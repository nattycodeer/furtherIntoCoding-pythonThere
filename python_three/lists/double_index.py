#Write your function here
def double_index(lst, index):
    new_list = lst[:index]
    new_list.append(int(lst[index] * 2))
    new_list = new_list + lst[index:]
    return new_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
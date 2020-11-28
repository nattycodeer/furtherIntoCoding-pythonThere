#Write your function here
def middle_element(lst):
    if len(lst) % 2 == 0:
        index_num = int(len(lst) / 2)
        middle_nums_sum = lst[index_num] + lst[index_num-1]
        average = middle_nums_sum / 2
        return average
    else:
        index_num = int(len(lst) // 2)
        return lst[index_num]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
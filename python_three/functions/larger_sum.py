# Write your function here
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num1 in lst1:
        sum1 += num1

    for num2 in lst2:
        sum2 += num2

    if sum1 > sum2:
        return lst1
    elif sum2 > sum1:
        return lst2
    elif sum2 == sum1:
        return lst1


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
def delete_starting_evens(lst):
    empty_lst = []

    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            return lst[i:]

# #Uncomment the lines below when your function is done
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


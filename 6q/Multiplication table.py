def multiplication_table(size):
    new_list = []
    for i in range(1, size + 1):
        first_list =[]
        for j in range(1, size + 1):
            first_list.append(i * j)
        new_list.append(first_list)


    return new_list



print(multiplication_table(1)) #, [[1]])
print(multiplication_table(2)) #, [[1, 2], [2, 4]])
# print(multiplication_table(3)) #, [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
# print(multiplication_table(4)) #, [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
# print(multiplication_table(5)) #, [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]])


# 1 2 3
# 2 4 6
# 3 6 9

# [[1,2,3],[2,4,6],[3,6,9]]
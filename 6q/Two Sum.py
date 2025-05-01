def two_sum(numbers, target):
    for i, num in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if num + numbers[j] == target:
                return i, j





print(two_sum([1 ,2, 3],            4)) #,)) #  ((0,2), (2,0))),
print(two_sum([1234,5678,9012], 14690)) #,  ((1,2), (2,1))),
print(two_sum([2, 2, 3],            4)) #,  ((0,1), (1,0))),

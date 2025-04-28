from itertools import count
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    set_nums = set()
    for num in nums:
        if num in set_nums:
            return True
        set_nums.add(num)
    return False




print(containsDuplicate([1,2,3,1])) # True
print(containsDuplicate([1, 2, 3, 4])) # False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True


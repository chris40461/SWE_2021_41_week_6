from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range (len(nums)):
        for j in range (i):
            if (nums[i]+nums[j]== target):
                print([j,i])
    return []

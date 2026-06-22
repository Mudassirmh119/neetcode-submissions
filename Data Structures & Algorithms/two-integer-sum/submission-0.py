class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for index, num in enumerate(nums):
            if num in difference:
                return [difference[num], index]
            difference[target - num] = index
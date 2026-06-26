from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        counter = Counter(nums)
        
        longest = 0
        for num in nums:
            if (num - 1) not in counter:
                length = 0
                while (num + length) in counter:
                    length += 1
                longest = max(length, longest)
        return longest
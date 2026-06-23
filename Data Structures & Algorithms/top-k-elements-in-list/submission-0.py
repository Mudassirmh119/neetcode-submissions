from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        
        li = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(li[i][0])
        return res
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        
        return [item[1] for item in heap]

        # li = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        # res = []
        # for i in range(k):
        #     res.append(li[i][0])
        # return res
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]
        
        for num, count in counter.items():
            bucket[count].append(num)
        
        result = []
        print(bucket)
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                result.append(n)
            if len(result) >= k:
                return result

        # counter = Counter(nums)
        # heap = []
   
        # for num, freq in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (freq, num))
        #     else:
        #         heapq.heappushpop(heap, (freq, num))
        
        # return [item[1] for item in heap]
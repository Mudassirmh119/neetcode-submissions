from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        post = [1] * len(nums)
        pref_prod = 1
        post_prod = 1
        
        for i, num in enumerate(nums):
            pref_prod *= num
            pref[i] = pref_prod

        for i in range(len(nums), 0, -1):        
            post_prod *= nums[i-1]
            post[i - 1] = post_prod
        
        li = []
        for index, num in enumerate(nums):
            print("idx",index + 1)
            if index == 0:
                li.append(post[index + 1])
            elif index == len(nums) - 1:
                li.append(pref[index - 1])
            else:
                li.append(pref[index - 1] * post[index + 1])        
        return li
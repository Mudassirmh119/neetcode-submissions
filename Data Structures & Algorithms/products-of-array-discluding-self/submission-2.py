class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        post = [1] * len(nums)        
        
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):        
            
            post[i] = post[i + 1] * nums[i + 1]
        
        li = []

        for i in range(len(nums)):
            li.append(pref[i] * post[i])
        return li
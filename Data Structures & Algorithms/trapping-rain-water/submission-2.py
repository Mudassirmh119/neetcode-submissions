class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]

        res = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        return res


        # max_left = [0] * len(height)
        # max_right = [0] * len(height)
        # current_max = 0

        # for i in range(len(height)):
        #     if i == 0:
        #         max_left[i] = 0
        #     else:
        #         current_max = max(height[i - 1], current_max)
        #         max_left[i] = current_max
        
        # current_max = 0
        # for i in range(len(height) - 1, -1, -1):
        #     if i == len(height) - 1:
        #         max_right[i] = 0
        #     else:
        #         current_max = max(height[i + 1], current_max)
        #         max_right[i] = current_max
        
        # result = 0
        # for i in range(len(height)):
        #     result += max(min(max_left[i], max_right[i]) - height[i], 0)
        
        # return result
        
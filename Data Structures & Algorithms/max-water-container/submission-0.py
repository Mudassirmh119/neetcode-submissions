class Solution:
    def maxArea(self, heights: List[int]) -> int:
        _max = 0

        left, right = 0, len(heights) - 1

        while left < right:
            _max = max(min(heights[left], heights[right]) * (right - left), _max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1 

        return _max
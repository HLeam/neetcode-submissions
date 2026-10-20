class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we want to know the are between two walls
        left, right = 0, len(heights) - 1
        curr_max = float('-inf')

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left 
            area = height * width

            curr_max = max(curr_max, area)

            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1

        return curr_max


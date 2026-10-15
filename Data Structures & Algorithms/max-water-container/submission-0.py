class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        curr_max = 0
        while left < right:
            # how we have to calculate how much water it can hold (w * h)
            height = min(heights[left], heights[right])
            width = right - left 
            area = height * width

            curr_max = max(curr_max, area)

            #figure out which wall is shorter then move to higher wall
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return curr_max

            
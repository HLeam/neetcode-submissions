class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        counter = 0
        # Probably gas for edge cases

        for i in nums:
            if i == 1:
                counter += 1
            else:
                counter = 0
            max_ = max(max_, counter)

        return max_
        
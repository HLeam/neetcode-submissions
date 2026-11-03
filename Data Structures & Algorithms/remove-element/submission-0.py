class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextNonVal = 0
        # 0,1,2,2,3,0,4,2
        for end in range(len(nums)):  
            if nums[end] != val:
                nums[nextNonVal] = nums[end]
                nextNonVal += 1
        return nextNonVal 

        
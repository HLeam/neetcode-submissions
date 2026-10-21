class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We can sort the nums array so we can iterate through two pointers to find where i + left + right  = 0

        nums.sort()
        res = []

        #since we are planning on left being i + 1 and right being len(nums) - 1
        #left and right area laready decided sof for loop from 0 -> len(nums) -2

        for i in range(len(nums) - 2):
            # there's also a case where i is going to be a number we've done before aleady
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # what we should do when total is > 0, < 0, and == 0
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # when there's a match now, there's cases where the value maybe [-1-1-1,0,2,2]
                    # we don't want left to iterate to just be -1 again and say that's a match for i + nums[l + 1] + nums[r] == 0 that could cause a duplicat

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        #this would get last dupcliate number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res
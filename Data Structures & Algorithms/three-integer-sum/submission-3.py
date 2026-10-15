class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #goal is for all three index to add to 0

        # there's a chase where we can have same consecutive numbers so we'll need to move pointers past the duplciats
        nums.sort()
        res = []
        # [-1,-1,-1,0,1,2]
        for i in range(len(nums) - 2):
            # we also have a case what if i is going to num we been thoguth 

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    #now we need to move the left and right pointers so the next one isn't duplicats
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return res



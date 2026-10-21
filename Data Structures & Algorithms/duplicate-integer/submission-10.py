class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set_nums = set(nums)

        # return len(set_nums) != len(nums)

        hm = defaultdict(int)

        for i in nums:
            if i in hm:
                return True
            else:
                hm[i] += 1

        return False
        
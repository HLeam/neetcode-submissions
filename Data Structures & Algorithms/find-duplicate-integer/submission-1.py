class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     check = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if check == nums[j]:
        #             return check
        state = defaultdict(int)
        for i in range(len(nums)):
            state[nums[i]] += 1

        for key, value in state.items():
            if value > 1:
                return key
            
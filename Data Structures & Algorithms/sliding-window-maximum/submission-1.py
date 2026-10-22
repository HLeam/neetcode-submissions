class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for end in range(len(nums)):
            # Remove indexes outside the window.
            while q and q[0] == end - k:
                q.popleft()

            # Smaller values cannot beat this newer value.
            while q and nums[q[-1]] <= nums[end]:
                q.pop()

            q.append(end)

            if end >= k - 1:
                res.append(nums[q[0]])

        return res
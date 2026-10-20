class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we want to know when a char that is added to the state contains a duplicate in our current state

        state = defaultdict(int)
        curr_max = 0
        start = 0

        for end in range(len(s)):
            state[s[end]] += 1

            while state[s[end]] > 1:
                state[s[start]] -= 1
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1
                
            curr_max = max(curr_max, end - start + 1)

        return curr_max
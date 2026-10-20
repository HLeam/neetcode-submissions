class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = defaultdict(int)
        start = 0
        max_ = 0

        #AAABABB
        for end in range(len(s)):
            state[s[end]] += 1

            # we want figure out what is the minmun we need to replace to get a higher number
            #end - start + 1 gets the current window we wan to - from max now 
            while end - start + 1 - max(state.values()) > k:
                state[s[start]] -= 1
                start += 1
            max_ = max(max_, end - start + 1)

        return max_
        
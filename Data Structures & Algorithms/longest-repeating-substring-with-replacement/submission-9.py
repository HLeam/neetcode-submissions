class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = defaultdict(int)
        max_ = 0
        start = 0

        for end in range(len(s)):
            state[s[end]] += 1

            while (end - start + 1) - max(state.values()) > k:
                state[s[start]] -= 1
                start += 1
            
            max_ = max(max_, end - start + 1)

        return max_
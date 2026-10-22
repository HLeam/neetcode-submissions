class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = defaultdict(int)
        start = 0
        max_ = 0
        most_freq = 0

        for end in range(len(s)):
            #Build the window
            state[s[end]] += 1

            # we need to see if the least commom char < k
            most_freq = max(most_freq, state[s[end]])
            #most_freq can also be max(state.values())
            while (end - start + 1) - most_freq > k:
                state[s[start]] -= 1
                start += 1
            max_ = max(max_, end - start + 1)

        return max_
                
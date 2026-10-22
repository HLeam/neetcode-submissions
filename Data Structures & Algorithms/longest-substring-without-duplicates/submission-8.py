class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need to keep track of char:occurance
        state = defaultdict(int)
        max_ = 0
        start = 0
        
        for end in range(len(s)):
            state[s[end]] += 1

            #if the character we added now has a value of 2 that means we should shrink the window until it's valid again 
            while state[s[end]] > 1:
                state[s[start]] -= 1
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1

            max_ = max(max_, len(state))
        return max_
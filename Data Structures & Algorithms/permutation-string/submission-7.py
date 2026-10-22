class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        state = defaultdict(int)
        s1_array = list(s1)
        res = False
        start = 0

        for end in range(len(s2)):
            state[s2[end]] += 1

            if end - start + 1 == len(s1):
                target = Counter(s1)
                if state == target:
                    return True
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1
        
        return res

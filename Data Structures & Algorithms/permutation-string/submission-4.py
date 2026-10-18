class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        res = False


        for end in range(len(s2)):
            state = list(s1)

            if s2[end] in state:

                for c in range(len(s1)):
                    if end + c < len(s2) and s2[end + c] in state:
                        state.remove(s2[end + c])
                    else:
                        break

                if len(state) == 0:
                    return True

                    
        return False
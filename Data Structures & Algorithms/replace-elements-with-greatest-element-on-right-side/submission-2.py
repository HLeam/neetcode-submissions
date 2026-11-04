class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1
        res = [0] * len(arr)

        for i in reversed(range(len(arr))):
            res[i] = max_
            max_ = max(max_, arr[i])
        return res
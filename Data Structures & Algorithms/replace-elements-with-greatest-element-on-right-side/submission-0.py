class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        left = 0 
        max_ = -1

        for end in range(len(arr)):
            # we now want to figure out the max of to the right 
            for j in range(end + 1, len(arr)):
                max_ = max(max_, arr[j])
            print(arr[end], max_)
            arr[end] = max_
            max_ = -1

        return arr

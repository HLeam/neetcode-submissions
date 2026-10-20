class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        count = 0
        state = []

        for end in range(len(arr)):
            state.append(arr[end])

            if end - start + 1 == k:
                avg_value = int(sum(state) / k)

                if avg_value >= threshold:
                    count += 1

                state.pop(0)
                start += 1
        return count
        
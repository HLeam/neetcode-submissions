class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for i in operations:
            if i == "+":
                stack.append(int(stack[-1] + stack[-2]))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(int(stack[-1] * 2))
            else:
                stack.append(int(i))
        return sum(stack)
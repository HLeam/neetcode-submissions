class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        res = 0
        for o in operations:
            if o == "+":
                total = int(s[-2]) + int(s[-1])
                s.append(int(total))
            elif o == "C":
                s.pop()
            elif o == "D":
                total = 2 * int(s[-1])
                s.append(int(total))
            else:
                s.append(int(o))
        return sum(s)

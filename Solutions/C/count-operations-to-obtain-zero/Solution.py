# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ret = 0
        if num1 > num2:
            num1, num2 = num2, num1

        while num1:
            ret += num2 // num1
            num1, num2 = num2 % num1, num1
        return ret

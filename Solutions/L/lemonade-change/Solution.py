# https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for x in bills:
            if x == 5:
                five += 1
            elif x == 10:
                if not five:
                    return False
                five, ten = five - 1, ten + 1
            elif five and ten:
                five, ten = five - 1, ten - 1
            elif five > 2:
                five -= 3
            else:
                return False
        return True

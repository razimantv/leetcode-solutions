# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, bottles: int, exchange: int) -> int:
        ret, empty = 0, 0
        while bottles:
            ret += bottles
            empty += bottles
            bottles = empty // exchange
            empty -= empty // exchange * exchange
        return ret

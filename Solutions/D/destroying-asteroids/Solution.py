# https://leetcode.com/problems/destroying-asteroids/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for x in sorted(asteroids):
            if x > mass: 
                return False
            mass += x
        return True

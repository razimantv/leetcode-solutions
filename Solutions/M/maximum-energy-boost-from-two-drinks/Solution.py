# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution:
    def maxEnergyBoost(
        self, energyDrinkA: List[int], energyDrinkB: List[int]
    ) -> int:
        A1, A2, B1, B2 = 0, 0, 0, 0
        for A, B in zip(energyDrinkA, energyDrinkB):
            A1, A2, B1, B2 = max(A1, B2) + A, A1, max(A2, B1) + B, B1
        return max(A1, B1)

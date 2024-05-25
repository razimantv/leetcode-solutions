# Taking maximum energy from the mystic dungeon

[Problem link](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Array reuse](/README.md#Dynamic_programming-Array_reuse)
* [Array scanning](/README.md#Array_scanning) > [Right to left](/README.md#Array_scanning-Right_to_left)

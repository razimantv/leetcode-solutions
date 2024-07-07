# Generate binary strings without adjacent zeros

[Problem link](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        prev = self.validStrings(n - 1)
        return [s + "1" for s in prev] + [
            s + "0" for s in prev if s[-1] == '1'
        ]
```
## Tags

* [Brute force enumeration](/README.md#Brute_force_enumeration) > [Elementwise processing using a vector](/README.md#Brute_force_enumeration-Elementwise_processing_using_a_vector)

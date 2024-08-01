# Plus one

[Problem link](https://leetcode.com/problems/plus-one)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/plus-one

class Solution {
 public:
  vector<int> plusOne(vector<int>& digits) {
    for (int pos = digits.size() - 1;; --pos) {
      if (pos < 0) {
        digits.insert(digits.begin(), 1);
        break;
      }

      if (++digits[pos] < 10) break;
      digits[pos] = 0;
    }
    return digits;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
* [Integer operations on strings](/Collections/integer-operations-on-strings.md#integer-operations-on-strings)

# Count symmetric integers

[Problem link](https://leetcode.com/problems/count-symmetric-integers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
 public:
  int countSymmetricIntegers(int low, int high) {
    int ret{};
    while (low <= high) {
      string s = to_string(low++);
      int L = s.size();
      if (L & 1) continue;
      if (accumulate(s.begin(), s.begin() + L / 2, 0) ==
          accumulate(s.begin() + L / 2, s.end(), 0))
        ret++;
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)

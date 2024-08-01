# Consecutive characters

[Problem link](https://leetcode.com/problems/consecutive-characters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/consecutive-characters

class Solution {
 public:
  int maxPower(string s) {
    int best = 1, cur = 1, N = s.size();
    for (int i = 1; i < N; ++i) {
      if (s[i] == s[i - 1])
        ++cur;
      else
        cur = 1;
      best = max(best, cur);
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)

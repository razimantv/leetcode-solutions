# Maximum enemy forts that can be captured

[Problem link](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution {
 public:
  int captureForts(vector<int>& forts) {
    int last1{-1}, last2{-1}, best{};
    for (int i{}, n = forts.size(); i < n; ++i) {
      int x = forts[i];
      if (!x) continue;
      if (x == 1) {
        if (last1 < last2) best = max(best, i - last2 - 1);
        last1 = i;
      } else {
        if (last2 < last1) best = max(best, i - last1 - 1);
        last2 = i;
      }
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)

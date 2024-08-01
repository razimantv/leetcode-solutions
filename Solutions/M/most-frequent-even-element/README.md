# Most frequent even element

[Problem link](https://leetcode.com/problems/most-frequent-even-element/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/most-frequent-even-element/

class Solution {
 public:
  int mostFrequentEven(vector<int>& nums) {
    int best = -1, bestcnt = 0;
    unordered_map<int, int> cnt;
    for (int x : nums) {
      if (x & 1) continue;
      ++cnt[x];
      if (cnt[x] > bestcnt or (cnt[x] == bestcnt and x < best))
        best = x, bestcnt = cnt[x];
    }
    return best;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)

# Minimum penalty for a shop

[Problem link](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution {
 public:
  int bestClosingTime(string s) {
    int ytot{}, n = s.size();
    for (char c : s)
      if (c == 'Y') ++ytot;
    int ret = 0, best = ytot;
    for (int i = 0, cur = ytot; i < n; ++i) {
      if (s[i] == 'N')
        ++cur;
      else
        --cur;
      if (cur < best) ret = i + 1, best = cur;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)

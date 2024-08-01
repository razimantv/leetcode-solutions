# Determine the minimum sum of a k avoiding array

[Problem link](https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution {
 public:
  int minimumSum(int n, int k) {
    int ret{};
    unordered_set<int> used;
    for (int i = 1; n; ++i)
      if (!used.count(k - i)) {
        ret += i;
        used.insert(i);
        --n;
      }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)

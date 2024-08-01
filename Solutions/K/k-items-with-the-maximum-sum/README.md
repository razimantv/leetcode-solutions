# K items with the maximum sum

[Problem link](https://leetcode.com/problems/k-items-with-the-maximum-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution {
 public:
  int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    vector<int> all{numOnes, numZeros, numNegOnes};
    int ret{};
    for (int i = 0; i < 3; ++i) {
      int cur = min(k, all[i]);
      ret += cur * (1 - i);
      k -= cur;
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)

# Max sum of a pair with equal sum of digits

[Problem link](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

class Solution {
 public:
  int digsum(int x) {
    int ret{};
    while (x) ret += x % 10, x /= 10;
    return ret;
  }
  int maximumSum(vector<int>& nums) {
    unordered_map<int, multiset<int>> work;
    int best = -1;
    for (int x : nums) {
      int y = digsum(x);
      if (work.count(y)) best = max(best, x + *work[y].rbegin());
      work[y].insert(x);
      if (work[y].size() == 3) work[y].erase(work[y].begin());
    }
    return best;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)

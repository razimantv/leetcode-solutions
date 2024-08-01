# Construct target array with multiple sums

[Problem link](https://leetcode.com/problems/construct-target-array-with-multiple-sums)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/construct-target-array-with-multiple-sums

class Solution {
 public:
  bool isPossible(vector<int>& target) {
    if (target.size() == 1) return target[0] == 1;

    multiset<int, greater<int>> cur(target.begin(), target.end());
    int n = target.size();
    long long tot = accumulate(target.begin(), target.end(), 0ll);

    while (*cur.begin() > 1) {
      int x = *cur.begin();
      cur.erase(cur.begin());

      long long rest = tot - x, prev = x % rest;
      if (!prev) prev = rest;
      if (prev == x) return false;
      tot -= x - prev;
      cur.insert(prev);
    }
    return true;
  }
};
```
## Tags

* [Time reversed simulation](/Collections/time-reversed-simulation.md#time-reversed-simulation)

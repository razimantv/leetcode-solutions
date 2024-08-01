# Beautiful arrangement

[Problem link](https://leetcode.com/problems/beautiful-arrangement)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/beautiful-arrangement

class Solution {
 public:
  unordered_set<int> seen;
  int countArrangement(int n, int start = 1) {
    if (start == n + 1) return 1;
    int ret = 0;
    for (int i = 1; i <= n; ++i) {
      if ((i % start and start % i) or seen.count(i)) continue;
      seen.insert(i);
      ret += countArrangement(n, start + 1);
      seen.erase(i);
    }
    return ret;
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)

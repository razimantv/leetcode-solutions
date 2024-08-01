# Number of dice rolls with target sum

[Problem link](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
  unordered_map<int, int> cache;

 public:
  int numRollsToTarget(int n, int k, int target) {
    if (n == 0 or target == 0) return n == target;
    int conv = (n << 10) | target;
    if (cache.count(conv)) return cache[conv];
    int& ret = cache[conv];

    const int MOD = 1'000'000'007;
    for (int i = 1; i <= k and i <= target; ++i) {
      ret += numRollsToTarget(n - 1, k, target - i);
      if (ret >= MOD) ret -= MOD;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)

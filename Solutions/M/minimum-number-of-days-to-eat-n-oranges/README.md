# Minimum number of days to eat n oranges

[Problem link](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges

class Solution {
 public:
  static unordered_map<int, int> cache;
  int minDays(int n) {
    if (n < 3)
      return n;
    else if (cache.count(n))
      return cache[n];
    else
      return cache[n] = 1 + min(n % 2 + minDays(n / 2), n % 3 + minDays(n / 3));
  }
};

unordered_map<int, int> Solution::cache = {};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)

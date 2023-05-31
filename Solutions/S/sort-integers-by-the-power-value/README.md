# Sort integers by the power value

[Problem link](https://leetcode.com/problems/sort-integers-by-the-power-value)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-integers-by-the-power-value

class Solution {
 public:
  unordered_map<int, int> cache;

  int collatz(int n) {
    if (cache.count(n))
      return cache[n];
    else
      return cache[n] = 1 + collatz((n & 1) ? (3 * n + 1) : n / 2);
  }

  int getKth(int lo, int hi, int k) {
    cache[1] = 0;
    vector<pair<int, int>> vec;
    for (int i = lo; i <= hi; ++i) vec.push_back({collatz(i), i});
    sort(vec.begin(), vec.end());
    return vec[k - 1].second;
  }
};
```
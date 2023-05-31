# Richest customer wealth

[Problem link](https://leetcode.com/problems/richest-customer-wealth)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/richest-customer-wealth

class Solution {
 public:
  int maximumWealth(vector<vector<int>>& accounts) {
    int ret = 0;
    for (const auto& a : accounts)
      ret = max(ret, accumulate(a.begin(), a.end(), 0));
    return ret;
  }
};
```
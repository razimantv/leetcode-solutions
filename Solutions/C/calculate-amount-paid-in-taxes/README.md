# Calculate amount paid in taxes

[Problem link](https://leetcode.com/problems/calculate-amount-paid-in-taxes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/calculate-amount-paid-in-taxes

class Solution {
 public:
  double calculateTax(vector<vector<int>>& brackets, int income) {
    int prev = 0;
    double ret = 0;
    for (const auto& v : brackets) {
      if (income <= v[0]) {
        ret += (income - prev) * v[1] / 100.;
        break;
      }
      ret += (v[0] - prev) * v[1] / 100.;
      prev = v[0];
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)

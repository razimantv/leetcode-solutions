# Sequential digits

[Problem link](https://leetcode.com/problems/sequential-digits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sequential-digits

class Solution {
 public:
  vector<int> sequentialDigits(int low, int high) {
    vector<int> ans;
    for (int i = 1; i < 10; ++i) {
      for (int dig = i, cur = dig; dig < 10 and cur <= high;
           cur = cur * 10 + (++dig)) {
        if (cur >= low) ans.push_back(cur);
      }
    }
    sort(ans.begin(), ans.end());
    return ans;
  }
};
```
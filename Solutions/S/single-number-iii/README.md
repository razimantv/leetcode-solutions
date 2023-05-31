# Single number iii

[Problem link](https://leetcode.com/problems/single-number-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/single-number-iii

class Solution {
 public:
  vector<int> singleNumber(vector<int>& nums) {
    unordered_set<int> s;
    for (int n : nums) {
      if (s.count(n))
        s.erase(n);
      else
        s.insert(n);
    }
    vector<int> ret;
    for (int n : s) ret.push_back(n);
    return ret;
  }
};
```
# Set mismatch

[Problem link](https://leetcode.com/problems/set-mismatch)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/set-mismatch

class Solution {
 public:
  vector<int> findErrorNums(vector<int>& nums) {
    int n = nums.size();
    vector<bool> seen(n + 1, false);
    vector<int> ret;
    for (int x : nums) {
      if (seen[x])
        ret.push_back(x);
      else
        seen[x] = true;
    }

    for (int i = 1; i <= n; ++i)
      if (!seen[i]) ret.push_back(i);
    return ret;
  }
};
```
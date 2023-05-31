# Teemo attacking

[Problem link](https://leetcode.com/problems/teemo-attacking)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/teemo-attacking

class Solution {
 public:
  int findPoisonedDuration(vector<int>& t, int d) {
    int ans = 0;
    for (int i = 0; i < t.size(); ++i) {
      ans += min(d, (i + 1) < t.size() ? (t[i + 1] - t[i]) : d);
    }
    return ans;
  }
};
```
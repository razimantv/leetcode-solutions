# Movement of robots

[Problem link](https://leetcode.com/problems/movement-of-robots/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/movement-of-robots/

class Solution {
 public:
  int sumDistance(vector<int>& nums, string s, int d) {
    int n = s.size();
    vector<long long> pos(n);
    for (int i = 0; i < n; ++i) pos[i] = nums[i] + (s[i] == 'L' ? -1 : 1) * d;
    sort(pos.begin(), pos.end());
    long long ret{}, psum{}, MOD = 1'000'000'007;
    for (int i = 0; i < n; ++i) {
      ret = (ret + i * pos[i] - psum) % MOD;
      psum += pos[i];
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)

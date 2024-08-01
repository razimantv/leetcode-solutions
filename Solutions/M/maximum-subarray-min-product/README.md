# Maximum subarray min product

[Problem link](https://leetcode.com/problems/maximum-subarray-min-product)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-subarray-min-product

class Solution {
 public:
  int maxSumMinProduct(vector<int>& nums) {
    vector<tuple<int, int, long long>> s;
    nums.push_back(-1);
    int n = nums.size();
    long long best = 0, cur = 0;
    for (int i = 0; i < n; ++i) {
      cur += nums[i];
      if (s.empty() or get<0>(s.back()) < nums[i])
        s.push_back({nums[i], i, cur});
      else {
        while (!s.empty() and get<0>(s.back()) >= nums[i]) {
          auto [v, p, prev] = s.back();
          s.pop_back();
          best =
              max(best, (cur - nums[i] - (s.empty() ? 0 : get<2>(s.back()))) *
                            (long long)v);
        }
        s.push_back({nums[i], i, cur});
      }
    }
    return best % 1'000'000'007;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)

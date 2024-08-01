# Count number of bad pairs

[Problem link](https://leetcode.com/problems/count-number-of-bad-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-number-of-bad-pairs

class Solution {
 public:
  long long countBadPairs(vector<int>& nums) {
    unordered_map<int, int> m;
    int n = nums.size();
    long long ret = (n * (long long)(n - 1)) / 2;

    for (int i = 0; i < n; ++i) m[i - nums[i]]++;
    for (auto [k, v] : m) ret -= (v * (long long)(v - 1)) / 2;
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Hashmap](/Collections/hashmap.md#hashmap)

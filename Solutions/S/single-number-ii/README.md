# Single number ii

[Problem link](https://leetcode.com/problems/single-number-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/single-number-ii

class Solution {
 public:
  int singleNumber(vector<int>& nums) {
    unordered_map<int, int> cnt;
    for (auto n : nums) cnt[n]++;
    for (auto m : cnt)
      if (m.second == 1) return m.first;
    return 0;
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N0, N1, N2 = ~0, 0, 0
        for x in nums:
            N0, N1, N2 = (N0 & ~x) | (N2 & x), (N1 & ~x) | (N0 & x), (N2 & ~x) | (N1 & x)
        return N1
```
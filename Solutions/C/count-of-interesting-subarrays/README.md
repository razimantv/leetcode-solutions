# Count of interesting subarrays

[Problem link](https://leetcode.com/problems/count-of-interesting-subarrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-of-interesting-subarrays/

class Solution {
 public:
  long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
    unordered_map<int, int> cnt;
    cnt[0] = 1;
    int pref{};
    long long ret{};
    for (int x : nums) {
      pref = (pref + (x % modulo == k)) % modulo;
      ret += cnt[(pref + modulo - k) % modulo];
      ++cnt[pref];
    }
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)

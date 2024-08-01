# Bitwise xor of all pairings

[Problem link](https://leetcode.com/problems/bitwise-xor-of-all-pairings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
 public:
  int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
    int ret = 0;
    if (nums1.size() & 1)
      ret ^= accumulate(nums2.begin(), nums2.end(), 0, bit_xor<int>());
    if (nums2.size() & 1)
      ret ^= accumulate(nums1.begin(), nums1.end(), 0, bit_xor<int>());
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Composition of operations](/Collections/mathematics.md#composition-of-operations)

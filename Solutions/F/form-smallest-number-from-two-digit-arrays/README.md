# Form smallest number from two digit arrays

[Problem link](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution {
 public:
  int minNumber(vector<int>& nums1, vector<int>& nums2) {
    vector<int> mask(10);
    for (int x : nums1) mask[x] = 1;
    for (int x : nums2) mask[x] |= 2;
    int x = 0;
    for (int i = 1, m = 0; i < 10; ++i) {
      if (mask[i] == 3)
        return i;
      else if (mask[i] and !(mask[i] & m)) {
        x = x * 10 + i;
        m |= mask[i];
      }
    }
    return x;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)

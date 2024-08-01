# Add to array form of integer

[Problem link](https://leetcode.com/problems/add-to-array-form-of-integer/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution {
 public:
  vector<int> addToArrayForm(vector<int>& num, int k) {
    reverse(num.begin(), num.end());
    for (int i = 0, carry = 0; k or carry; ++i) {
      if (i == num.size()) num.push_back(0);
      num[i] += carry + k % 10;
      carry = num[i] / 10;
      k /= 10;
      num[i] %= 10;
    }
    reverse(num.begin(), num.end());
    return num;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)

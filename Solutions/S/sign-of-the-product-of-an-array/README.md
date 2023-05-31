# Sign of the product of an array

[Problem link](https://leetcode.com/problems/sign-of-the-product-of-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution {
 public:
  int arraySign(vector<int>& nums) {
    int sgn = 1;
    for (int n : nums) {
      if (n == 0)
        return 0;
      else if (n < 0)
        sgn = -sgn;
    }

    return sgn;
  }
};
```
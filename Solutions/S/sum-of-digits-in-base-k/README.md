# Sum of digits in base k

[Problem link](https://leetcode.com/problems/sum-of-digits-in-base-k)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-digits-in-base-k

class Solution {
 public:
  int sumBase(int n, int k) {
    int ret = 0;
    while (n) {
      ret += n % k;
      n /= k;
    }
    return ret;
  }
};
```
# The kth factor of n

[Problem link](https://leetcode.com/problems/the-kth-factor-of-n)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-kth-factor-of-n

class Solution {
 public:
  int kthFactor(int n, int k) {
    for (int i = 1; i <= n; ++i)
      if (n % i == 0 and --k == 0) return i;
    return -1;
  }
};
```
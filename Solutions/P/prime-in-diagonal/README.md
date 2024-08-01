# Prime in diagonal

[Problem link](https://leetcode.com/problems/prime-in-diagonal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/prime-in-diagonal/

class Solution {
 public:
  bool prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i)
      if (n % i == 0) return false;
    return true;
  }
  int diagonalPrime(vector<vector<int>>& nums) {
    int ret{};
    for (int i = 0, n = nums.size(); i < n; ++i) {
      for (int j : {i, n - 1 - i}) {
        int x = nums[i][j];
        if (prime(x)) ret = max(ret, x);
      }
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)

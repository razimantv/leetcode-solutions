# N th tribonacci number

[Problem link](https://leetcode.com/problems/n-th-tribonacci-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
 public:
  int tribonacci(int n) {
    if (n < 2) return n;

    int a = 0, b = 1, c = 1;
    for (int i = 2; i < n; ++i) {
      a += b + c;
      swap(a, c);
      swap(a, b);
    }
    return c;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)

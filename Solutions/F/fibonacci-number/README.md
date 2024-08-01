# Fibonacci number

[Problem link](https://leetcode.com/problems/fibonacci-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/fibonacci-number

class Solution {
 public:
  int fib(int n) {
    int prev = 1, cur = 0;
    for (int i = 0; i < n; ++i) {
      prev += cur;
      swap(prev, cur);
    }
    return cur;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)

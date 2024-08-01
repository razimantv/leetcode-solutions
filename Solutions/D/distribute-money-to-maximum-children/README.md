# Distribute money to maximum children

[Problem link](https://leetcode.com/problems/distribute-money-to-maximum-children/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution {
 public:
  int distMoney(int money, int children) {
    if (money < children)
      return -1;
    else if (money == children * 8 - 4)
      return children - 2;
    else if (money == children * 8)
      return children;
    else
      return min((money - children) / 7, children - 1);
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)

# Ugly number ii

[Problem link](https://leetcode.com/problems/ugly-number-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/ugly-number-ii

class Solution {
 public:
  int nthUglyNumber(int n) {
    vector<int> ugly = {1};
    int l2 = 0, l3 = 0, l5 = 0;
    for (int i = 1; i < n; ++i) {
      if (ugly[l2] * 2 == ugly.back()) ++l2;
      int n2 = ugly[l2] * 2;
      if (ugly[l3] * 3 == ugly.back()) ++l3;
      int n3 = ugly[l3] * 3;
      if (ugly[l5] * 5 == ugly.back()) ++l5;
      int n5 = ugly[l5] * 5;
      if (n2 <= n3 and n2 <= n5) {
        ugly.push_back(n2);
        ++l2;
      } else if (n3 <= n5) {
        ugly.push_back(n3);
        ++l3;
      } else {
        ugly.push_back(n5);
        ++l5;
      }
    }
    return ugly.back();
  }
};
```
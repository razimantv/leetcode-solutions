# Valid square

[Problem link](https://leetcode.com/problems/valid-square)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-square

class Solution {
 public:
  bool test(const vector<int>& a, const vector<int>& b, const vector<int>& c,
            const vector<int>& d) {
    if (a[0] + b[0] != c[0] + d[0]) return false;
    if (a[1] + b[1] != c[1] + d[1]) return false;
    vector<int> d1{a[0] - b[0], a[1] - b[1]}, d2{c[0] - d[0], c[1] - d[1]};
    return (d1[0] * d2[0] + d1[1] * d2[1] == 0) and
           (d1[0] * d1[0] + d1[1] * d1[1] != 0) and
           (d1[0] * d1[0] + d1[1] * d1[1] == d2[0] * d2[0] + d2[1] * d2[1]);
  }
  bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3,
                   vector<int>& p4) {
    return test(p1, p2, p3, p4) or test(p1, p3, p2, p4) or test(p1, p4, p2, p3);
  }
};
```
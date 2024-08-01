# Numbers at most n given digit set

[Problem link](https://leetcode.com/problems/numbers-at-most-n-given-digit-set)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set

class Solution {
 public:
  int atMostNGivenDigitSet(vector<string>& digits, int n) {
    string ns = to_string(++n);
    int D = digits.size(), N = ns.size();
    vector<int> p(ns.size(), 1);
    sort(digits.begin(), digits.end());
    int ret = 0;
    for (int i = 1; i < p.size(); ++i) ret += (p[i] = p[i - 1] * D);
    for (int i = 0; i < N; ++i) {
      bool flag = false;
      int dcnt = 0;
      for (string d : digits) {
        if (d[0] < ns[i])
          ++dcnt;
        else if (d[0] == ns[i])
          flag = true;
        else
          break;
      }
      ret += dcnt * p[N - 1 - i];
      if (!flag) break;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)

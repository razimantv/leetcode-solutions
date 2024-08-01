# Count special integers

[Problem link](https://leetcode.com/problems/count-special-integers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-special-integers

class Solution {
 public:
  int factorial(int n) { return (n < 2) ? 1 : (n * factorial(n - 1)); }
  int countSpecialNumbers(int n) {
    auto str = to_string(++n);
    int ret = 0, L = str.size();
    for (int i = 1; i < L; ++i) ret += 9 * factorial(9) / factorial(10 - i);
    // cout << "start:" << ret << "\n";
    for (int i = 0; i < L; ++i) {
      for (char c = '0' + (i == 0); c < str[i]; ++c) {
        // cout << i << " " << c;
        bool flag = false;
        for (int j = 0; j < i; ++j)
          if (str[j] == c) {
            flag = true;
            break;
          }
        if (!flag) {
          ret += factorial(10 - i - 1) / factorial(10 - L);
          // cout << " " << ret;
        }
        // cout<< "\n";
      }
      bool flag = false;
      for (int j = 0; j < i; ++j)
        if (str[j] == str[i]) {
          flag = true;
          break;
        }
      if (flag) break;
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)

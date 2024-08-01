# Count of integers

[Problem link](https://leetcode.com/problems/count-of-integers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-of-integers/

class Solution {
 public:
  vector<vector<int>> cnt;
  const int MOD = 1'000'000'007;
  void inc(int& x, int y) {
    x += y;
    if (x >= MOD) x -= MOD;
  }
  void dec(int& x, int y) { inc(x, MOD - y); }
  int count(const string& num, int target) {
    int ret{}, L = num.size();
    for (int i = 0; target >= 0 and i < L; ++i) {
      int x = num[i] - '0';
      for (int y = 0; y < x and target >= 0; ++y, --target)
        inc(ret, cnt[L - i - 1][target]);
      if (!target) return ++ret;
    }
    return ret;
  }
  int count(string num1, string num2, int s1, int s2) {
    int L = num2.size();
    cnt = vector<vector<int>>(L + 1, vector<int>(s2 + 1, 0));
    cnt[0][0] = 1;
    for (int i = 0; i < L; ++i)
      for (int j = 0; j <= s2; ++j)
        for (int k = j; k <= s2 and k < j + 10; ++k)
          inc(cnt[i + 1][k], cnt[i][j]);

    int ret{};
    for (int i = s1; i <= s2; ++i) {
      inc(ret, count(num2, i));
      dec(ret, count(num1, i));
    }

    int dsum1{};
    for (char c : num1) dsum1 += c - '0';
    if (dsum1 >= s1 and dsum1 <= s2) inc(ret, 1);

    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)

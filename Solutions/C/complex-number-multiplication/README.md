# Complex number multiplication

[Problem link](https://leetcode.com/problems/complex-number-multiplication)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/complex-number-multiplication

class Solution {
 public:
  pair<int, int> cmp(const string& s) {
    bool flag{false};
    int p = 0;
    if (s[0] == '-') flag = true, ++p;
    int f = 0;
    while (s[p] != '+') f = f * 10 + s[p++] - '0';
    if (flag) f = -f;

    flag = false;
    if (s[++p] == '-') flag = true, ++p;
    int g = 0;
    while (s[p] != 'i') g = g * 10 + s[p++] - '0';
    if (flag) g = -g;

    return {f, g};
  }
  string complexNumberMultiply(string num1, string num2) {
    auto [f1, g1] = cmp(num1);
    auto [f2, g2] = cmp(num2);

    int f = f1 * f2 - g1 * g2, g = f1 * g2 + f2 * g1;
    return to_string(f) + "+" + to_string(g) + "i";
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Integer operations on strings](/Collections/integer-operations-on-strings.md#integer-operations-on-strings)

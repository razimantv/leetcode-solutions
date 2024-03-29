# Fraction to recurring decimal

[Problem link](https://leetcode.com/problems/fraction-to-recurring-decimal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/fraction-to-recurring-decimal

class Solution {
 public:
  string fractionToDecimal(long long num, long long den) {
    if (den < 0) num = -num, den = -den;
    if (!num) return "0";
    string ret;
    if (num < 0) ret = "-", num = -num;
    ret += to_string(num / den);
    num %= den;
    if (!num) return ret;
    ret += ".";
    string decimal;
    map<int, int> pos;
    for (int i = 0;; ++i) {
      if (!num) return ret += decimal;
      if (pos.count(num))
        return ret += decimal.substr(0, pos[num]) + "(" +
                      decimal.substr(pos[num]) + ")";
      pos[num] = i;
      num *= 10;
      decimal += to_string(num / den);
      num %= den;
    }
  }
};
```
## Tags

* [Hashmap](/README.md#Hashmap) > [Update using insert and delete](/README.md#Hashmap-Update_using_insert_and_delete)
* [Mathematics](/README.md#Mathematics) > [Basic](/README.md#Mathematics-Basic)

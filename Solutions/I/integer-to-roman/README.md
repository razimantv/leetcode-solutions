# Integer to roman

[Problem link](https://leetcode.com/problems/integer-to-roman)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/integer-to-roman

class Solution {
 public:
  string intToRoman(int num) {
    vector<int> nums{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> conv{"M",  "CM", "D",  "CD", "C",  "XC", "L",
                        "XL", "X",  "IX", "V",  "IV", "I"};

    string ret = "";
    for (int i = 0; num;) {
      if (num >= nums[i]) {
        num -= nums[i];
        ret += conv[i];
      } else
        ++i;
    }
    return ret;
  }
};
```
## Tags

* [Formatted output](/Collections/formatted-output.md#formatted-output)

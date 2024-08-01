# Integer to english words

[Problem link](https://leetcode.com/problems/integer-to-english-words)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/integer-to-english-words

class Solution {
  const string digits[10] = {"Zero", "One", "Two",   "Three", "Four",
                             "Five", "Six", "Seven", "Eight", "Nine"};
  const string teens[10] = {"Ten",      "Eleven",  "Twelve",  "Thirteen",
                            "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                            "Eighteen", "Nineteen"};
  const string tens[10] = {"",      "",      "Twenty",  "Thirty", "Forty",
                           "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
  const string multipliers[4] = {"", " Thousand", " Million", " Billion"};

  string threedigit(int n) {
    string ret;
    if (!n) return ret;

    if (n >= 100) ret += digits[n / 100] + " Hundred";
    n %= 100;
    if (!n) return ret;

    if (!ret.empty()) ret += " ";
    if (n < 10)
      return ret + digits[n];
    else if (n < 20)
      return ret + teens[n - 10];

    ret += tens[n / 10];
    n %= 10;
    if (!n) return ret;

    if (!ret.empty()) ret += " ";
    return ret + digits[n];
  }

 public:
  string numberToWords(int num) {
    if (!num) return "Zero";

    string ret;
    for (int i = 3, m = 1'000'000'000; i >= 0; --i, m /= 1000) {
      if (num < m) continue;
      if (!ret.empty()) ret += " ";
      ret += threedigit(num / m) + multipliers[i];
      num %= m;
    }

    return ret;
  }
};
```
## Tags

* [Formatted output](/Collections/formatted-output.md#formatted-output)

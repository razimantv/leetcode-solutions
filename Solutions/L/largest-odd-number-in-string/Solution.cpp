// https://leetcode.com/problems/largest-odd-number-in-string

class Solution {
 public:
  string largestOddNumber(string num) {
    for (int i = num.size() - 1; i >= 0; --i)
      if (num[i] & 1) return num.substr(0, i + 1);
    return "";
  }
};

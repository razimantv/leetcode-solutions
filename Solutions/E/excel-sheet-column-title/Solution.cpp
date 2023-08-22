// https://leetcode.com/problems/excel-sheet-column-title/

class Solution {
 public:
  string convertToTitle(int n) {
    string s;
    while (n) {
      s += ('A' + (--n) % 26);
      n /= 26;
    }
    reverse(s.begin(), s.end());
    return s;
  }
};

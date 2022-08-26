// https://leetcode.com/problems/plus-one

class Solution {
 public:
  vector<int> plusOne(vector<int>& digits) {
    for (int pos = digits.size() - 1;; --pos) {
      if (pos < 0) {
        digits.insert(digits.begin(), 1);
        break;
      }

      if (++digits[pos] < 10) break;
      digits[pos] = 0;
    }
    return digits;
  }
};

// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution {
 public:
  int findNumbers(vector<int>& nums) {
    int cnt = 0;
    for (int n : nums) cnt += (to_string(n).size() % 2 == 0);
    return cnt;
  }
};

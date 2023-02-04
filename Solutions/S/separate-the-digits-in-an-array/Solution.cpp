// https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution {
 public:
  vector<int> separateDigits(vector<int>& nums) {
    vector<int> ret;
    for (int x : nums)
      for (char c : to_string(x)) ret.push_back(c - '0');
    return ret;
  }
};

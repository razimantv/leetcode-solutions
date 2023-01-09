// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution {
 public:
  int maximumCount(vector<int>& nums) {
    int p{}, n{};
    for (int x : nums)
      if (x > 0)
        ++p;
      else if (x < 0)
        ++n;
    return max(n, p);
  }
};

// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible

class Solution {
 public:
  int minOperations(vector<int>& nums, vector<int>& numsDivide) {
    sort(nums.begin(), nums.end());
    int x = accumulate(numsDivide.begin(), numsDivide.end(), numsDivide[0],
                       [](int a, int b) { return __gcd(a, b); });
    for (int i = 0, n = nums.size(); i < n; ++i)
      if (x % nums[i] == 0) return i;
    return -1;
  }
};

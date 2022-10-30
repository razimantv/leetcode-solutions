// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution {
 public:
  int averageValue(vector<int>& nums) {
    int tot = 0, cnt = 0;
    for (int x : nums)
      if (x % 6 == 0) tot += x, cnt++;
    if (cnt)
      return tot / cnt;
    else
      return 0;
  }
};

// https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution {
 public:
  int numberOfPoints(vector<vector<int>>& nums) {
    vector<int> hascar(101);
    for (auto car : nums)
      for (int i = car[0]; i <= car[1]; ++i) hascar[i] = 1;
    return accumulate(hascar.begin(), hascar.end(), 0);
  }
};

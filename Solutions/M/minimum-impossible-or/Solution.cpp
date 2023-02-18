// https://leetcode.com/problems/minimum-impossible-or/

class Solution {
 public:
  int minImpossibleOR(vector<int>& nums) {
    unordered_set<int> s;
    for (int x : nums) s.insert(x);
    for (int x = 1;; x <<= 1)
      if (!s.count(x)) return x;
    return -1;
  }
};

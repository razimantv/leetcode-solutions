// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution {
 public:
  vector<int> findDisappearedNumbers(vector<int>& nums) {
    unordered_set<int> s;
    for (int x : nums) s.insert(x);

    vector<int> ret;
    for (int i = 1, n = nums.size(); i <= n; ++i)
      if (!s.count(i)) ret.push_back(i);
    return ret;
  }
};

// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution {
 public:
  vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    vector<int> ret;
    vector<short> cnt(1001);
    for (int x : nums1) ++cnt[x];
    for (int x : nums2)
      if (cnt[x]-- > 0) ret.push_back(x);
    return ret;
  }
};

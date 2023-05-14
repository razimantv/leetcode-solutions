// https://leetcode.com/problems/maximum-or/

class Solution {
 public:
  long long maximumOr(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> lpref(n), rpref(n);
    for (int i = 1, j = n - 2; i < n; ++i, --j) {
      lpref[i] = lpref[i - 1] | nums[i - 1];
      rpref[j] = rpref[j + 1] | nums[j + 1];
    }

    long long ret{};
    for (int i = 0; i < n; ++i)
      ret = max(ret, lpref[i] | rpref[i] | ((nums[i] * 1ll) << k));
    return ret;
  }
};

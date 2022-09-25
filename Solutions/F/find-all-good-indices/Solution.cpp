// https://leetcode.com/problems/find-all-good-indices/

class Solution {
 public:
  vector<int> goodIndices(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> left(n, 1), right(n, 1), answer;
    for (int i = 1; i < n; ++i)
      if (nums[i] <= nums[i - 1]) left[i] = left[i - 1] + 1;
    for (int i = n - 2; i >= 0; --i)
      if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
    for (int i = k; i < n - k; ++i)
      if (left[i - 1] >= k and right[i + 1] >= k) answer.push_back(i);
    return answer;
  }
};

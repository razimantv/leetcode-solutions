// https://leetcode.com/problems/range-sum-query-immutable

class NumArray {
 public:
  vector<int> psum;

  NumArray(vector<int>& nums) {
    psum = {0};
    int tot = 0;
    for (int x : nums) psum.push_back(tot += x);
  }

  int sumRange(int left, int right) { return psum[right + 1] - psum[left]; }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */

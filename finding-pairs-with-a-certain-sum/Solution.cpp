// https://leetcode.com/problems/finding-pairs-with-a-certain-sum

class FindSumPairs {
 public:
  vector<int> nums1, nums2;
  unordered_map<int, int> cnt;
  FindSumPairs(vector<int>& n1, vector<int>& nums2) : nums1(n1), nums2(nums2) {
    sort(nums1.begin(), nums1.end());
    for (int x : nums2) ++cnt[x];
  }

  void add(int i, int v) {
    --cnt[nums2[i]];
    ++cnt[nums2[i] += v];
  }

  int count(int tot) {
    int ret = 0;
    for (int x : nums1) {
      if (x >= tot) break;
      ret += cnt[tot - x];
    }
    return ret;
  }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */

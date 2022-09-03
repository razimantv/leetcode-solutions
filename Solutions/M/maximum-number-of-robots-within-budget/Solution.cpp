// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

class Solution {
 public:
  bool work(int n, int k, vector<int>& ct, vector<int>& rc, long long b) {
    long long tot = 0;
    deque<pair<int, int>> dq;
    for (int i = 0; i < n; ++i) {
      tot += rc[i];
      while (!dq.empty() and dq.back().first <= ct[i]) dq.pop_back();
      dq.push_back({ct[i], i});
      if (i >= k - 1) {
        while (dq.front().second <= i - k) dq.pop_front();
        long long cur = k * tot + dq.front().first;
        if (cur <= b) return true;
        tot -= rc[i - k + 1];
      }
    }
    return false;
  }
  int maximumRobots(vector<int>& ct, vector<int>& rc, long long b) {
    int n = ct.size();
    int start = 0, end = n + 1;
    while (end - start > 1) {
      int mid = (start + end) >> 1;
      if (work(n, mid, ct, rc, b))
        start = mid;
      else
        end = mid;
    }
    return start;
  }
};

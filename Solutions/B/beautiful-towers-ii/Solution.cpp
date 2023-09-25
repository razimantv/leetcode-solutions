// https://leetcode.com/problems/beautiful-towers-ii/

class Solution {
 public:
  long long maximumSumOfHeights(vector<int>& h) {
    int n = h.size();
    vector<long long> lsum(n), rsum(n);
    vector<int> stack{0};

    for (long long i = 1; i < n; ++i) {
      while (!stack.empty() and h[stack.back()] > h[i]) stack.pop_back();
      if (stack.empty())
        lsum[i] = i * h[i];
      else
        lsum[i] = h[i] * (i - stack.back() - 1) + h[stack.back()] +
                  lsum[stack.back()];
      stack.push_back(i);
    }

    stack = {n - 1};
    for (long long i = n - 2; i >= 0; --i) {
      while (!stack.empty() and h[stack.back()] > h[i]) stack.pop_back();
      if (stack.empty())
        rsum[i] = (n - 1 - i) * h[i];
      else
        rsum[i] = h[i] * (stack.back() - i - 1) + h[stack.back()] +
                  rsum[stack.back()];
      stack.push_back(i);
    }

    long long ret{};
    for (int i = 0; i < n; ++i) ret = max(ret, lsum[i] + h[i] + rsum[i]);
    return ret;
  }
};

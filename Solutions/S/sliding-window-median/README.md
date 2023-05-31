# Sliding window median

[Problem link](https://leetcode.com/problems/sliding-window-median)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sliding-window-median

class Solution {
 public:
  multiset<int, greater<int>> left;
  multiset<int> right;
  int lx, ly;

  void balance() {
    if (left.size() > lx) {
      right.insert(*left.begin());
      left.erase(left.begin());
    } else if (right.size() > ly) {
      left.insert(*right.begin());
      right.erase(right.begin());
    }
  }

  void add(int x) {
    left.insert(x);
    balance();
  }

  void remove(int x) {
    if (left.count(x))
      left.erase(left.find(x));
    else
      right.erase(right.find(x));
    balance();
  }

  double median() {
    double ret = *right.begin();
    if (left.size() == right.size()) ret = (ret + *left.begin()) / 2;
    return ret;
  }

  vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    int n = nums.size();
    lx = k >> 1, ly = k - lx;
    for (int i = 0; i < k; ++i) add(nums[i]);
    vector<double> ret{median()};
    for (int i = 0, j = k; j < n; ++i, ++j) {
      add(nums[j]);
      remove(nums[i]);
      ret.push_back(median());
    }
    return ret;
  }
};
```
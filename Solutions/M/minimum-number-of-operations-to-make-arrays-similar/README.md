# Minimum number of operations to make arrays similar

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution {
 public:
  pair<vector<int>, vector<int>> oddeven(const vector<int>& v) {
    vector<int> odd, even;
    for (int x : v) ((x & 1) ? odd : even).push_back(x);
    sort(odd.begin(), odd.end());
    sort(even.begin(), even.end());
    return {odd, even};
  }

  long long work(const vector<int>& v1, const vector<int>& v2) {
    int n = v1.size();
    long long ret{};
    for (int i = 0; i < n; ++i) {
      if (v1[i] < v2[i]) ret += v2[i] - v1[i];
    }
    return ret / 2;
  }

  long long makeSimilar(vector<int>& nums, vector<int>& target) {
    auto [odd1, even1] = oddeven(nums);
    auto [odd2, even2] = oddeven(target);
    return work(odd1, odd2) + work(even1, even2);
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution:
    def oddeven(self, nums):
        odd = sorted(filter(lambda x: x % 2 == 1, nums))
        even = sorted(filter(lambda x: x % 2 == 0, nums))
        return odd, even

    def work(self, v1, v2):
        n = len(v1)
        return sum([v1[i]-v2[i] for i in range(n) if v1[i] > v2[i]]) // 2

    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        odd1, even1 = self.oddeven(nums)
        odd2, even2 = self.oddeven(target)
        return self.work(odd1, odd2) + self.work(even1, even2)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Greedy](/Collections/greedy.md#greedy)

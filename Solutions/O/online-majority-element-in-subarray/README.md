# Online majority element in subarray

[Problem link](https://leetcode.com/problems/online-majority-element-in-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/online-majority-element-in-subarray

class MajorityChecker {
 public:
  vector<int> arr;
  const int L = 800;
  unordered_map<int, vector<int>> pos;
  map<int, vector<int>> cntmap;
  MajorityChecker(vector<int>& arr) : arr(arr) {
    int N = arr.size();
    for (int i = 0; i < N; ++i) pos[arr[i]].push_back(i);
    for (auto& [v, vec] : pos) cntmap[vec.size()].push_back(v);
  }

  int query(int left, int right, int threshold) {
    if (threshold < L) {
      unordered_map<int, int> cur;
      for (int i = left; i <= right; ++i)
        if (++cur[arr[i]] == threshold) return arr[i];
      return -1;
    }

    for (auto mit = cntmap.lower_bound(threshold); mit != cntmap.end(); ++mit) {
      for (int v : mit->second) {
        auto& vec = pos[v];
        if (upper_bound(vec.begin(), vec.end(), right) -
                lower_bound(vec.begin(), vec.end(), left) >=
            threshold)
          return v;
      }
    }
    return -1;
  }
};

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker* obj = new MajorityChecker(arr);
 * int param_1 = obj->query(left,right,threshold);
 */
```
## Tags

* [Design data structure](/README.md#Design_data_structure)
* [Binary search](/README.md#Binary_search) > [C++ set](/README.md#Binary_search-C___set)

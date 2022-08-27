// https://leetcode.com/problems/find-k-closest-elements

class Solution {
 public:
  vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    nth_element(arr.begin(), arr.begin() + k, arr.end(), [&](int a, int b) {
      if (abs(a - x) != abs(b - x)) return abs(a - x) < abs(b - x);
      return a < b;
    });
    arr.erase(arr.begin() + k, arr.end());
    sort(arr.begin(), arr.end());
    return arr;
  }
};

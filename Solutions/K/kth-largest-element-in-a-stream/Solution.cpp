// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest {
 public:
  multiset<int> heap;
  int k;
  KthLargest(int k, vector<int>& nums) : k(k) {
    for (int x : nums) add(x);
  }

  int add(int val) {
    heap.insert(val);
    if (heap.size() > k) heap.erase(heap.begin());
    return *heap.begin();
  }
};


# Clone graph

[Problem link](https://leetcode.com/problems/clone-graph)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/clone-graph


class Solution {
  unordered_map<int, Node*> cache;

 public:
  Node* cloneGraph(Node* node) {
    if (node == NULL) return NULL;
    Node* ret = new Node(node->val);
    cache[node->val] = ret;
    for (auto next : node->neighbors) {
      if (!cache.count(next->val))
        next = cloneGraph(next);
      else
        next = cache[next->val];
      ret->neighbors.push_back(next);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Pointers](/Collections/pointers.md#pointers)

# Shortest path to get all keys

[Problem link](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution {
public:
  const vector<pair<int,  int>> neigh{{0,1},{1,0},{0,-1},{-1,0}};
  int shortestPathAllKeys(vector<string>& grid) {
    int K{1}, m=grid.  size (), n=grid[0].  size(), starti, startj;
    for(int i=0;i<m;++i) for(int j=0;j<n;++j) {
      char c=grid[i][j];
      if(c>='a') K= max(K, c-'a'+1);
      if(c=='@') starti=i, startj=j;
    }
    int KM {(1<<K)-1};
    
    auto getmask=[&](int i, int j, int keymask) {
      return (i<<(5+K)) | (j<<K) | keymask;
    };
    auto unmask=[&](int m) {
      int keymask=m&KM; m>>=K;
      int j=m&31; m>>=5;
      return make_tuple(m, j, keymask);
    };
    
    queue<int> bfsq;
    int startmask{getmask(starti, startj, 0)};
    bfsq.  push(startmask);
    unordered_map<int, int> dist{{startmask,0}};
    while(!  bfsq.  empty()){
      auto[i,j,keymask]= unmask(bfsq. front());
      int d=dist [bfsq.  front()];
      bfsq.  pop();
      if(keymask==KM) return d;
      for(auto[di,dj]: neigh) {
        int ii=i+di, jj=j+dj, mmask=keymask;
        if(ii<0 or ii>=m or jj<0 or jj>=n or grid[ii][jj]=='#') continue;
        char c=grid[ii][jj];
        if(isalpha(c)) {
          int key = (c&7)-1;
          if(c<'a') {
            if(!(keymask& (1<<key))) continue;
          } else mmask |=(1<<key);
        }
        int newmask=getmask(ii,jj, mmask);
        if(! dist .  count(newmask)) {
          dist[newmask ]=d+1;
          bfsq.  push(newmask);
        }
      }
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Addition of auxiliary vertices](/Collections/graph-theory.md#addition-of-auxiliary-vertices)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)

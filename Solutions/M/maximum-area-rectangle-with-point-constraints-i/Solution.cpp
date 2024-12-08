// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

// Converted by ChatGPT
class QuadNode {
 public:
  int cnt;
  QuadNode* child[2][2];

  QuadNode() : cnt(0) {
    for (int i = 0; i < 2; ++i) {
      for (int j = 0; j < 2; ++j) {
        child[i][j] = nullptr;
      }
    }
  }
};

class Solution {
 public:
  int maxRectangleArea(vector<vector<int>>& points) {
    vector<int> xCoord, yCoord;
    for (auto& coord : points) {
      xCoord.push_back(coord[0]);
      yCoord.push_back(coord[1]);
    }
    QuadNode* quad = new QuadNode();
    int xmin = *min_element(xCoord.begin(), xCoord.end());
    int xmax = *max_element(xCoord.begin(), xCoord.end());
    int ymin = *min_element(yCoord.begin(), yCoord.end());
    int ymax = *max_element(yCoord.begin(), yCoord.end());

    auto insert = [&](auto&& insert, QuadNode* node, int xl, int xr, int yl,
                      int yr, int x, int y) -> void {
      node->cnt++;
      if (xl == xr && yl == yr) return;
      int xm = (xl + xr) / 2;
      int ym = (yl + yr) / 2;
      int i = (x > xm) ? 1 : 0;
      int j = (y > ym) ? 1 : 0;
      int cxl = (i == 0) ? xl : xm + 1;
      int cxr = (i == 0) ? xm : xr;
      int cyl = (j == 0) ? yl : ym + 1;
      int cyr = (j == 0) ? ym : yr;

      if (node->child[i][j] == nullptr) {
        node->child[i][j] = new QuadNode();
      }
      insert(insert, node->child[i][j], cxl, cxr, cyl, cyr, x, y);
    };

    auto count = [&](auto&& count, QuadNode* node, int xl, int xr, int yl,
                     int yr, int xL, int xR, int yL, int yR, int cur) -> int {
      if (cur > 4) return 5;
      if (xL <= xl && xr <= xR && yL <= yl && yr <= yR) {
        return cur + node->cnt;
      }
      int xm = (xl + xr) / 2;
      int ym = (yl + yr) / 2;
      if (xm >= xL && ym >= yL) {
        if (node->child[0][0] != nullptr) {
          cur = count(count, node->child[0][0], xl, xm, yl, ym, xL, min(xm, xR),
                      yL, min(ym, yR), cur);
          if (cur > 4) return 5;
        }
      }
      if (xm >= xL && ym < yR) {
        if (node->child[0][1] != nullptr) {
          cur = count(count, node->child[0][1], xl, xm, ym + 1, yr, xL,
                      min(xm, xR), max(ym + 1, yL), yR, cur);
          if (cur > 4) return 5;
        }
      }
      if (xm < xR && ym >= yL) {
        if (node->child[1][0] != nullptr) {
          cur = count(count, node->child[1][0], xm + 1, xr, yl, ym,
                      max(xm + 1, xL), xR, yL, min(ym, yR), cur);
          if (cur > 4) return 5;
        }
      }
      if (xm < xR && ym < yR) {
        if (node->child[1][1] != nullptr) {
          cur = count(count, node->child[1][1], xm + 1, xr, ym + 1, yr,
                      max(xm + 1, xL), xR, max(ym + 1, yL), yR, cur);
          if (cur > 4) return 5;
        }
      }
      return cur;
    };

    unordered_map<int, vector<int>> rows, cols;
    unordered_set<pair<int, int>, pair_hash> seen;

    for (size_t i = 0; i < xCoord.size(); ++i) {
      int x = xCoord[i], y = yCoord[i];
      insert(insert, quad, xmin, xmax, ymin, ymax, x, y);
      seen.insert({x, y});
      rows[x].push_back(y);
      cols[y].push_back(x);
    }

    unordered_map<pair<int, int>, int, pair_hash> rownext, colnext;

    for (auto& [x, row] : rows) {
      sort(row.begin(), row.end());
      for (size_t i = 0; i + 1 < row.size(); ++i) {
        rownext[{x, row[i]}] = row[i + 1];
      }
    }

    for (auto& [y, col] : cols) {
      sort(col.begin(), col.end());
      for (size_t i = 0; i + 1 < col.size(); ++i) {
        colnext[{col[i], y}] = col[i + 1];
      }
    }

    int ret = -1;
    for (auto& [x, y] : seen) {
      if (rownext.find({x, y}) == rownext.end() ||
          colnext.find({x, y}) == colnext.end())
        continue;

      int y2 = rownext[{x, y}];
      int x2 = colnext[{x, y}];
      if (seen.find({x2, y2}) != seen.end() &&
          count(count, quad, xmin, xmax, ymin, ymax, x, x2, y, y2, 0) == 4) {
        ret = max(ret, (y2 - y) * (x2 - x));
      }
    }

    return ret;
  }

 private:
  struct pair_hash {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const {
      auto hash1 = hash<T1>{}(p.first);
      auto hash2 = hash<T2>{}(p.second);
      return hash1 ^ hash2;
    }
  };
};

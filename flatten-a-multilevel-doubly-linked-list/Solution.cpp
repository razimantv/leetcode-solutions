// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
 public:
  Node *flatten(Node *head, int start = 1) {
    if (head == NULL) return NULL;
    Node *right = head->next;

    Node *child = head;
    if (head->child != NULL) {
      child = flatten(head->child, 0);
      head->next = head->child;
      head->child->prev = head;
      head->child = NULL;

      if (right != NULL) {
        right->prev = child;
        child->next = right;
      }
    }

    Node *end = child;
    if (right != NULL) {
      end = flatten(right, 0);
    }

    return start ? head : end;
  }
};

// https://leetcode.com/problems/reverse-linked-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
 public:
  ListNode* reverseList(ListNode* head, ListNode* prev = nullptr) {
    if (!head) return head;
    ListNode* temp = head->next;
    head->next = prev;
    return temp ? reverseList(temp, head) : head;
  }
};

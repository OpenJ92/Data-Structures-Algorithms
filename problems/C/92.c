/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (head == NULL || right == left) {
        return head;
    }
    
    struct ListNode struct_sentinel_one = { .val = 0, .next = head };
    struct ListNode* sentinel_one = &struct_sentinel_one;
    struct ListNode* curr = head;

    while (left > 1) {
        curr = curr->next;
        sentinel_one = sentinel_one->next;
        right = right - 1;
        left = left - 1;
    }

    struct ListNode struct_sentinel_two = { .val = 0, .next = curr };
    struct ListNode* sentinel_two = &struct_sentinel_two;
    struct ListNode* temp = NULL;

    while (right > 0) {
        temp = curr->next;
        curr->next = sentinel_two;
        sentinel_two = curr;
        curr = temp;
        right = right - 1;
    }

    sentinel_one->next->next = curr;
    sentinel_one->next = sentinel_two;

    return struct_sentinel_one.next;
}

#include <stdlib.h>
#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

/*
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    if (l1 == NULL && l2 == NULL)
        return NULL;

    struct ListNode *dummy_head = malloc(sizeof(struct ListNode)), *tail = dummy_head;
    int carry = 0;
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int digit_sum = carry;
        if (l1) {
            digit_sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            digit_sum += l2->val;
            l2 = l2->next;
        }
        // carry can only be 0 or 1
        carry = (digit_sum >= 10) ? 1 : 0;
        tail->next = malloc(sizeof(struct ListNode));
        tail = tail->next;
        tail->val = (digit_sum >= 10) ? (digit_sum - 10) : digit_sum;
        tail->next = NULL;
    }

    struct ListNode *ans = dummy_head->next;
    free(dummy_head);
    return ans;
}

int main(int argc, char **argv) {
    struct ListNode l1 = {5, NULL};
    struct ListNode l2 = {5, NULL};
    struct ListNode *ans_iter = addTwoNumbers(&l1, &l2);
    int ans = 0, factor = 1;
    while (ans_iter != NULL) {
        ans += factor * ans_iter->val;
        factor *= 10;
        ans_iter = ans_iter->next;
    }
    printf("Answer: %i\n", ans);
    return 0;
}
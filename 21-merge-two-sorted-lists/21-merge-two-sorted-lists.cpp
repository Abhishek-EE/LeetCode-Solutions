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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *head;
        if(!list1)
            return list2;
        if(!list2)
            return list1;
        if(list1->val < list2->val){
            head = list1;
            list1 = list1->next;
        }
        else{
            head = list2;
            list2 = list2->next;
        }
        ListNode *tail = head;
        while(list1 && list2){
            if(list1->val < list2->val){
                tail->next = list1;
                tail = list1;
                list1 = list1->next;
            }
            else{
                tail->next = list2;
                tail = list2;
                list2 = list2->next;
            }
        }
        if(list1){
            tail->next = list1;
        }
        if(list2){
            tail->next = list2;
        }
    return head;
    }
    
    
};
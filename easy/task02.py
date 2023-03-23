# 21-Merge-Two-Sorted-List

from typing import Optional

# [1, 2, 3] [1, 2, 2, 4]
# [1, 1, 2, 2, 2, 3, 4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = temp = ListNode(0) # link to head of new list, link to tail (temporary) of new list
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1 
        if list2:      
            temp.next = list2
        return head.next
    

list1 = ListNode(1)
list1.next =  ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(3)
list2.next =  ListNode(5)
list2.next.next = ListNode(7)
list2.next.next.next = ListNode(9)
print(Solution().mergeTwoLists(list1, list2))

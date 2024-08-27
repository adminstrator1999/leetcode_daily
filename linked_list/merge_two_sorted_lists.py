from typing import Optional

from linked_list import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            else:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return head.next


"""
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode()
        # iterate over both list nodes
        while l1 and l2:
            # assign tail.next to smaller value
            # increment respective linked list
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # increment combined linked list
            tail = tail.next
        # assign whatever exists
        tail.next = l1 or l2
        # prevents iterating backwards to get head of linked list
        return dummy.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
print(Solution().mergeTwoLists(l1, l2))

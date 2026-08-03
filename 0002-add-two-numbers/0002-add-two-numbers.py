# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create a placeholder 'dummy' node to build our list easily
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Loop until both lists are empty AND there is no remaining carry
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if we reached the end
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create the next node in our result list with the single digit
            curr.next = ListNode(total % 10)
            
            # Move our result pointer and the input pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
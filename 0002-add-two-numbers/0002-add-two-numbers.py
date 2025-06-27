# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Iterate while there are still digits in either list or a carry exists
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum for the current digit position
            total_sum = val1 + val2 + carry

            # Update the carry for the next iteration
            carry = total_sum // 10

            # Create a new node for the current digit (total_sum % 10)
            current.next = ListNode(total_sum % 10)
            current = current.next

            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # The result is the linked list starting from the node after the dummy head
        return dummy_head.next
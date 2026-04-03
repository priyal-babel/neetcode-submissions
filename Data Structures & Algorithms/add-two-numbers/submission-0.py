# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # We loop as long as there is a digit in l1, a digit in l2, OR a leftover carry
        while l1 or l2 or carry:
            # If one list is shorter, we just substitute 0 for the missing digits
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 1. Compute the sum for this column
            total = val1 + val2 + carry
            
            # 2. Extract the digit and the new carry
            carry = total // 10   # e.g., 15 // 10 = 1
            digit = total % 10    # e.g., 15 % 10 = 5
            
            # 3. Create the new node and attach it
            current.next = ListNode(digit)
            
            # 4. Move all our pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the actual start of our newly built list
        return dummy.next
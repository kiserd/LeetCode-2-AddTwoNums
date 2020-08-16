# Author: Donald Logan Kiser
# Date: 08/11/2020
# Description: adds two numbers from linked lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode()
    carry = 0
    sum = 0
    current_1 = l1
    current_2 = l2
    current_3 = l3

    # iterate through input processing node values and populating return list
    while current_1 is not None or current_2 is not None or carry != 0:
        current_3.next = ListNode()
        current_3 = current_3.next
        
        # handle case where both input linked lists are active
        if current_1 is not None and current_2 is not None:
            sum = current_1.val + current_2.val + carry

            # handle case where we need to carry
            if sum > 9:
                carry = 1
                current_3.val = sum % 10

            # handle case where we do NOT need to carry
            if sum < 10:
                carry = 0
                current_3.val = sum

            # iterate linked lists to following nodes
            current_1 = current_1.next
            current_2 = current_2.next
        

        # handle case where only l1 is active
        elif current_1 is not None and current_2 is None:
            sum = current_1.val + carry

            # handle case where we need to carry
            if sum > 9:
                carry = 1
                current_3.val = sum % 10
            
            # handle case where we do NOT need to carry
            if sum < 10:
                carry = 0
                current_3.val = sum

            # iterate linked list to following node
            current_1 = current_1.next

        # handle case where only l2 is active
        elif current_1 is None and current_2 is not None:
            sum = current_2.val + carry

            # handle case where we need to carry
            if sum > 9:
                carry = 1
                current_3.val = sum % 10
            
            # handle case where we do NOT need to carry
            if sum < 10:
                carry = 0
                current_3.val = sum

            # iterate linked list to following node
            current_2 = current_2.next

        # handle case where neither input linked list is active, but we have a carry
        else:
            current_3.val = carry
            carry = 0

    return l3.next
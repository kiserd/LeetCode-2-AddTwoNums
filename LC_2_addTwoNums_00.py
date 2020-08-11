# Author: Donald Logan Kiser
# Date: 08/11/2020
# Description: adds two numbers from linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # declare some helper variables
        node_list = [l1, l2]
        sum = 0
        for node in node_list:
            power = 0
            current = node
            # loop through linked lists and calculate sums
            while current is not None:
                sum += current.val * (10 ^ power)
                power += 1
                current = current.next
        return sum





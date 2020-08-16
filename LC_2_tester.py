# Course: CS261 - Data Structures
# Student Name: Donald Logan Kiser
# Assignment: A2P2 bag da UNIT TESTING
# Description: unit tests for bag_da.py

import unittest
from LC_2_addTwoNums_00 import ListNode, addTwoNumbers

class leetCode2(unittest.TestCase):
    """
    definte unit tests for dynamic_array.py
    """
    def test_1(self):
        """
        test #1
        """
        l1 = ListNode()
        l1.next = ListNode()
        l1.next.next = ListNode()
        l1.val = 2
        l1.next.val = 2
        l1.next.next.val = 1

        l2 = ListNode()
        l2.next = ListNode()
        l2.next.next = ListNode()
        l2.val = 1
        l2.next.val = 1
        l2.next.next.val = 1

        l3 = addTwoNumbers(l1, l2)
        print(l3.val)
        print(l3.next.val)
        print(l3.next.next.val)



if __name__ == '__main__':
    unittest.main()
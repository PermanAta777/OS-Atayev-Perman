import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        self.assertEqual(ll.to_list(), [3, 2, 1])
    
    def test_empty_list(self):
        ll = LinkedList()
        with self.assertRaises(ValueError):
            ll.reverse()

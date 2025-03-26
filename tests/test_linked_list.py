import unittest
from src.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_reverse(self):
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(i)
        ll.reverse()
        self.assertEqual(ll.to_list(), [3, 2, 1])
        
    def test_empty(self):
        ll = LinkedList()
        with self.assertRaises(ValueError):
            ll.reverse()
            
    def test_single_node(self):
        ll = LinkedList()
        ll.append(1)
        ll.reverse()
        self.assertEqual(ll.to_list(), [1])

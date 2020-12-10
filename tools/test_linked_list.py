import unittest

from problems.tools import linked_list as ll


def make_linked_list_for_test():
    head = ll.ListNode(1)
    ln2 = ll.ListNode(2)
    ln3 = ll.ListNode(3)
    head.next = ln2
    ln2.next = ln3
    return head


class TestLinkedList(unittest.TestCase):
    def test_get_linked_list_representation(self):
        head = make_linked_list_for_test()
        self.assertEqual(ll.get_linked_list_representation(head), "1 -> 2 -> 3")

    def test_make_linked_list_from_iterable(self):
        values = [1, 2, 3, 4]
        self.assertEqual(
            ll.get_linked_list_representation(ll.make_linked_list_from_iterable(values)),
            "1 -> 2 -> 3 -> 4")

    def test_traverse(self):
        head = make_linked_list_for_test()
        self.assertEqual(ll.traverse(head), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

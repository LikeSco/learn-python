# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = []
        l1V = filter(str.isdigit, str(l1))
        l2V = filter(str.isdigit, str(l2))
        l_l1 = list(l1V)
        l_l2 = list(l2V)

        l_l1.reverse()
        l_l2.reverse()

        x = ''.join(l_l1)
        y = ''.join(l_l2)

        z = int(x) + int(y)

        for item in str(z):
            l3.append(int(item))

        l3.reverse()
        val = str(l3).replace("[", "").replace("]", "").replace(" ", "")

        return ListNode(val)

# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Brute ~ simplest
    def middleNode(self, head:Node) -> Node:
        length = 0  # no. of nodes in LL
        temp = head

        # First traversal to find length
        while temp!=None:
            length+=1
            temp = temp.next

        # Second traversal to find middle node
        cnt = 0
        temp1 = head
        while temp1:
            if cnt==length//2:
                return temp1

            cnt+=1
            temp1 = temp1.next


    # Optimal
    def middleNode2(self, head:Node) -> Node:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 5 -> 7 -> 9
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(9)

    sol = Solution()
    # print("Middle Node of LL: ", sol.middleNode(head).val)
    print("Middle Node of LL: ", sol.middleNode2(head).val)
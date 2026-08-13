# Creation of a Linked List from an array / Traversal of a Linked List

class Node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next

class Solution:
    def arr2LL(self, arr:list[int]):
        head = Node(arr[0])
        mover = head

        for i in range(1, len(arr)):
            temp = Node(arr[i])     # create new node
            mover.next = temp
            mover = temp

        return head

    def traversal(self, head):
        temp = head

        # traverse till we reach last node
        while(temp!=None):
            print(temp.data, end="->")
            temp = temp.next

        print(None)

# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list:
    arr = list(map(int, input().split()))

    sol = Solution()

    head = sol.arr2LL(arr)
    sol.traversal(head)
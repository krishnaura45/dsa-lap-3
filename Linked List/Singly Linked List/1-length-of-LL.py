# Length of a Linked List / Count nodes in a LL

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def length(self, head):
        cnt = 0
        temp = head
        # traverse till we reach Null
        while(temp!=None):
            temp = temp.next
            cnt+=1
            
        return cnt


# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 5 -> 7 -> 9
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(9)

    sol = Solution()
    print("Length of LL: ", sol.length(head))

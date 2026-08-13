# Frequency in a Linked List --> Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def count(self, head, key):
        freq = 0
        temp = head
        # until temporary node is valid
        while(temp!=None):
            if temp.data==key:
                freq+=1
                
            temp = temp.next
            
        return freq

# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 1 -> 2 -> 1
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    sol = Solution()
    key = 1
    print(f"Frequency of {key} in LL: ", sol.count(head,key))
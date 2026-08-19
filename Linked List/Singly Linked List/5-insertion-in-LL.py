# Insertion/Addition of an Element in Linked list

class Node:
    def __init__(self, data = 0, next=None):
        self.data = data
        self.next = next

class Creation:
    def arr2LL(self, arr:list[int]):
        head = Node(arr[0])
        mover = head

        for i in range(1, len(arr)):
            temp = Node(arr[i])     # create new node
            mover.next = temp
            mover = temp

        return head

class Insertion:
    def length(self, head):
        cnt = 0  
        temp = head
        # traverse till we reach Null
        while(temp!=None):
            temp = temp.next
            cnt+=1
            
        return cnt
    
    def traversal(self, head):
        temp = head

        # traverse till we reach last node
        while(temp!=None):
            print(temp.data, end="->")
            temp = temp.next

    def insertAtHead(self, head, el):
        temp = Node(el,head)
        return temp

    def insertAtLast(self, head, el):
        if head==None:
            return Node(el, None)

        temp = head

        # Traversing upto the second last element
        while temp.next!=None:
            temp = temp.next

        temp.next = Node(el, None)
        return head

    # Insert element at Kth psition of the linked list
    def insertNodeK(self, head, k, el):
        if head==None:
            if k==1:
                return Node(el)

            else:
                return None

        if k==1:
            return Node(el,head)

        cnt = 0
        temp = head
        while temp:
            cnt+=1
            if cnt==k-1:
                newNode = Node(el,temp.next)
                temp.next = newNode
                break

            temp = temp.next

        return head

    def insertbeforeValue(self, head, el, val):
        if head==None:
            return None

        if head.data==val:
            return Node(el,head)

        temp = head
        
        while temp.next!=None:  # Never going to last
            # Stop at the position one before the given value
            if temp.next.data==val:
                newNode = Node(el,temp.next)
                temp.next = newNode
                break

            temp = temp.next

        return head

    def insertNode(self, node):
        pass


if __name__ == "__main__":
    # Create a hard-coded linked list:
    arr = list(map(int, input().split()))
    obj = Creation()
    head = obj.arr2LL(arr)

    sol = Insertion()
    new = sol.insertAtHead(head,5)
    print(sol.traversal(new))

    new2 = sol.insertAtLast(new, 9)
    print(sol.traversal(new2))

    new3 = sol.insertNodeK(new2,k=4,el=6)
    print(sol.traversal(new3))

    new4 = sol.insertbeforeValue(new3,4,3)
    print(sol.traversal(new4))
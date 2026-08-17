# Deletion in Linked list

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

class Deletion:
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

    def deleteHead(self, head):
        temp = head
        head = head.next
        del temp
        return head

    def deleteTail(self, head):
        if head==None or head.next==None:
            return None
        
        temp = head

        # To remove tail of the linked list, we need to traverse upto the second last element
        while temp.next.next!=None:
            temp = temp.next

        del temp.next
        temp.next = None
        return head

    # Delete Kth element of the linked list
    def deleteNodeK(self, head, k):
        # if self.length(head)<k:
        #     print("deletion not possible!")

        if head==None:
            return None

        if k==1:
            return self.deleteHead(head)

        # cnt = 1
        # temp = head
        # while cnt<k-1:
        #     temp = temp.next
        #     cnt+=1

        # prev = temp
        # prev.next = prev.next.next
        # temp = temp.next
        # del temp
        # return head

        cnt, temp, prev = 0, head, None
        while temp!=None:
            cnt+=1
            # Traverse upto kth element
            if cnt == k:
                prev.next = prev.next.next
                del temp
                break

            prev = temp            # first update previous pointer
            temp = temp.next       # then update actual current traversal pointer

        return head

    def deleteValue(self, head, val):
        if head==None:
            return None

        if head.data==val:
            temp = head
            head = head.next
            del temp
            return head

        cnt, temp, prev = 0, head, None
        while temp!=None:
            cnt+=1
            # Traverse upto kth element
            if temp.data==val:
                prev.next = prev.next.next
                del temp
                break

            prev = temp            # first update previous pointer
            temp = temp.next       # then update actual current traversal pointer

        return head

    def deleteNode(self, node):
        """
        Delete specific node where head is not given
        """

        temp = Node(node.data)
        node.data = node.next.data
        node.next = node.next.next
        del temp


if __name__ == "__main__":
    # Create a hard-coded linked list:
    arr = list(map(int, input().split()))
    obj = Creation()
    head = obj.arr2LL(arr)

    sol = Deletion()
    new = sol.deleteHead(head)
    print(sol.traversal(new))

    new2 = sol.deleteTail(new)
    print(sol.traversal(new2))

    new3 = sol.deleteNodeK(new2,k=4)
    print(sol.traversal(new3))

    new4 = sol.deleteValue(new3,5)
    print(sol.traversal(new4))

    sol.deleteNode(new4)
    print(sol.traversal(new4))

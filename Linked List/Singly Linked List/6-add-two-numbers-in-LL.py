# Add Two numbers in Linked List

class Node:
    def __init__(self, data = 0, next=None):
        self.data = data
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
    
    def str2LL(self, s:str):
        head = Node(int(s[0]))
        mover = head

        for i in range(1, len(s)):
            temp = Node(int(s[i]))     # create new node
            mover.next = temp
            mover = temp

        return head
    
    def traversal(self, head):
        temp = head

        # traverse till we reach last node
        while(temp!=None):
            print(temp.data, end="->")
            temp = temp.next

    # Brute force
    def addTwoNumbers(self, h1, h2):
        s1, s2 = "", ""
        t1, t2 = h1, h2
        ans = None

        while t1:
            s1 += str(t1.data)
            t1 = t1.next

        while t2:
            s2 += str(t2.data)
            t2 = t2.next

        addSum = str(int(s1[::-1]) + int(s2[::-1]))

        req = addSum[::-1]
        ans = self.str2LL(req)
        return ans

    # Better
    def addTwoNumbers2(self, h1, h2):
        a = b = ""

        while h1:
            a += str(h1.data)
            h1 = h1.next

        while h2:
            b += str(h2.data)
            h2 = h2.next

        total = str(int(a[::-1]) + int(b[::-1]))

        head = cur = Node(0)

        for x in total[::-1]:
            cur.next = Node(int(x))
            cur = cur.next

        return head.next
    # TC ~ O(m+n), SC ~ O(m+n) when m is length of first number and n is length of second number

    # Optimal
    def addTwoNumbers3(self, l1, l2):
        dummy = Node(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.data if l1 else 0
            y = l2.data if l2 else 0

            total = x + y + carry
            carry = total // 10

            cur.next = Node(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    # TC ~ O(max(m,n)), SC ~ O(1)
    

if __name__ == "__main__":
    # Two numbers in form of linked lists
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    sol = Solution()
    head1 = sol.arr2LL(arr1)
    head2 = sol.arr2LL(arr2)

    # new = sol.addTwoNumbers(head1,head2)
    # new = sol.addTwoNumbers2(head1,head2)
    new = sol.addTwoNumbers3(head1,head2)
    print(sol.traversal(new))
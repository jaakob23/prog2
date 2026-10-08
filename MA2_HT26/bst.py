""" bst.py

Student: Jakob Khaytan
E-mail: jakob.khaytan.5362@student.uu.se
Reviewed by: Ivar
Date reviewed: 2026-09-28
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    # def contains(self, k): # given function
    #     n = self.root
    #     while n and n.key != k:
    #         if k < n.key:
    #             n = n.left
    #         else:
    #             n = n.right
    #     return n is not None

    def contains(self, k): # Exc8: write recursive contains
        return self._contains(self.root, k)
    def _contains(self, r, k):
        if r and r.key != k:
            if k<r.key:
                return self._contains(r.left, k)
            else:
                return self._contains(r.right, k)
        return r is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):             # Exc9     
        return self._height(self.root)
    def _height(self,r):
        if r is None:
            return 0
        return 1 + max(self._height(r.left), self._height(r.right))

        #compl runs n/2 times compl =n/2=> compl n

    # def height(self):     #doesnt work due to tree unbalanced            
    #     return self._height(0)
    # def _height(self,i):
    #     if self.size()//2**i==0:
    #         return 0
    #     elif self.size()//2**i==1:
    #         return i+1
    #     else:
    #         return self._height(i+1)

    def __str__(self):            # Exc10       
        treelst=[]
        for i in self:
            treelst.append(f'{i}') 
        return '<'+', '.join(treelst)+'>'
        

    def to_list(self):            # Exc11   
        lst=[]
        for i in self:
            lst.append(i)
        return lst
        # Complexity of to_list:
            #n? runs once for every number in the tree
        # FILL IN

    def to_LinkedList(self):                            # Exc12
        result=LinkedList()
        last=None
        for i in self:
            new_node=LinkedList.Node(i,None)
            if last is None:
                result.first=new_node
            else:
                last.succ = new_node
            last=new_node
        return result

    def remove(self, key):                      #Exc 13
        self.root = self._remove(self.root, key)
    def _remove(self, r, k):
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:   # This is the key to be removed
            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:   # Also easy case
                return r.left
            else:   # This is the tricky case.
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
                f = r.right
                while f.left  is not None:
                    f = f.left

                r.key = f.key 
                r.right = self._remove(r.right, f.key)
        return r    # Remember this! It applies to some of the cases above


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
    #for x in [1,8,9,23,4,6,10,54,23,18,24,5,3,8,11]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    print('height : ', t.height())
    print(t)
    print(t.to_list())


if __name__ == "__main__":
    main()


"""
Exc14: In a binary search tree with n nodes and height h, what is the complexity in the
following scenarios:
==============================

1. Worst case of successful search
    worsst case is n=h (only one long branch) in which the  amount of iterations
    equal n, theta(n)
2. Worst case of unsuccessful search
    unsuccessfull is the same complexity theta(n), (but amount of iterations is n+1)

"""

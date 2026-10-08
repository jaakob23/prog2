""" linked_list.py

Student: Jakob Khaytan
Mail: Jakob.khaytan.5362@student.uu.se
Reviewed by: Ivar
Review date: 2026/09/28
"""
class Person:
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __lt__(self, q): #p.__lt__(q)
        return self.name < q.name
    
    def __le__(self, q):
        return self.name <= q.name
    
    def __eq__(self, q):
        return self.name == q.name

    def __str__(self):
        return f'{self.name}:{self.pnr}'


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __contains__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Exc1
        i=0
        current = self.first
        while current != None:
            i+=1
            current=current.succ
        return i

    def remove_last(self):        # Exc2
        current = self.first
        if current == None:
            raise ValueError
        elif current.succ == None:
            last=current.data
            self.first=None
            return last
        while current.succ.succ != None:
            current=current.succ
        #if current.succ.succ == None:
        last=current.succ.data
        current.succ = None
        return last

    def remove(self, x):          # Exc3
        current=self.first
        while current != None:
            if current.data == x:
                self.first = current.succ
                return True
            elif current.succ != None and current.succ.data == x: #funkr ej utan !=None
                current.succ=current.succ.succ      #funkar för om.succ.succ = None
                return True
            current=current.succ
        return False

    def to_list(self):            # Exc4
        def _to_list(f):
            if f == None:
                return []
            else:
                return [f.data] + _to_list(f.succ)
        return _to_list(self.first)

    def __str__(self):            # Exc5
        partlst=[]
        for i in self: #letar efter __iter__ automatiskt
            partlst.append(f'{i}')
        return '('+', '.join(partlst)+')' #placerar mellan elements
            

    # def copy(self):
    #     result = LinkedList()
    #     for x in self: #n = antal noder i self
    #         result.insert(x) #kör insert med redan srterad lista, dvs n+1 >= n
    #                  #1 + 2 + 3 + ... + (n-1) insert while worst case = n(n-1)/2
    #                  # = (n^2 - n)/2=> complexity Θ(n^2)
    #     return result
        # Complexity for this implementation:
        '''
        complexity is Θ(n^2) since insert(x) increases amount of loops for 
        every iteration in while loop (worst case) (also already sorted)

        (since already sorted copy can skip sorting)
        '''
        # FILL IN

    def copy(self):               # Exc6, should be more efficient
        result = LinkedList()
        last=None
        for x in self:
            newnode=LinkedList.Node(x, None)
            if result.first==None:
                result.first=newnode
            else:
                last.succ=newnode
            last=newnode
        return result                     
        # Complexity for this implementation:
            #complexity Θ(n) where n is the amount of nmbers in self (linkedlist)
        # FILL IN



def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:
    #print(LinkedList.length(lst))
    #print(LinkedList.remove_last(lst))
    #print(LinkedList.remove(lst, 3))
    #print(LinkedList.to_list(lst))
    


    #plist=LinkedList()
    #p= Person("Jakob", "010203-1234")
    #q= Person("Adam", "040506-5678")
    #plist.insert(p)
    #plist.insert(q)
    #plist.print()


if __name__ == '__main__':
    main()

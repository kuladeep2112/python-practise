# setup the data structure
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def add(self):
        for i in range(1,10):
            if i == 1:
                node = Node(i)
                self.head=node
            else:
                node.next= Node(i)
                node=node.next

    def printlist(self):
        temp=self.head
        lstr=''
        while(temp):
            lstr=lstr+str(temp.data)+' '
            temp=temp.next
        print(lstr)

    # insertion --> insert at random place
    def insert(self,data,position):
        newnode=Node(data)
        temp=self.head
        if position < 1:
            print("Invalid position!")
        if position == 1:
            newnode.next = self.head
            self.head = newnode
        while(position!=0):
            position=position-1
            if position==1:
                newnode.next=temp.next
                temp.next=newnode
                break
            temp=temp.next

    # retrival --> search
    def search(self,x):
        temp=self.head
        while (temp):
            if temp.data == x:
                print("Found")
                break
            temp=temp.next
        if temp == None:
            print("Not found")

    # update --> update at a given index
    def update(self,data,position):

        current = self.head

        if position < 1:
            print("Invalid position!")
        if position == 1:
            current.data=data

        while(position!=0):
            position=position-1
            if position == 0:
                current.data=data
                break

            current  = current.next
    # delete a node

    def remove(self,index):
        current=self.head
        prev=None
        if index == 1:
            current=current.next
            self.head=current
        if index < 1:
            print("Invalid position!")
        while(index!=1):
            index=index-1
            prev=current
            current=current.next

        prev.next=current.next
        current=None

    #add a node as a last node to linked list
    def append(self,data):
        newnode=Node(data)
        current=self.head
        prev=None
        if current == None:
            current=newnode
        while(current):
            prev=current
            current=current.next
        prev.next=newnode



fun=linkedlist()
fun.add()


fun.search(1)

fun.printlist()
fun.remove(8)

fun.printlist()



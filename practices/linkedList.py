class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,head = None):
        self.head = head
    def append():
    def remove():
        #   n-
        # 1-2-3-4
    def insert(self,newElement,position):
        count =1
        current = self.head
        if position ==1:
            newElement.next = self.head
            self.head = newElement
        while current:
            if count+1 == position:
                newElement.next = current.next
                current.next = newElement
                return
            else:
                count+=1
                current = current.next
        



    

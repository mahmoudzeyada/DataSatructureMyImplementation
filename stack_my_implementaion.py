class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class linked_list(object):
    def __init__(self,head=None):
        self.head=head
    def append(self,new_element):
        pointer=self.head
        if self.head:
            while pointer.next:
                pointer=pointer.next
            pointer.next=new_element
        else:
            self.head=new_element
    def insert_first(self,new_element):
        pointer=self.head
        self.head=new_element
        new_element.next=pointer
    def delete_first(self):
        pointer=self.head
        if self.head:
            self.head=self.head.next
            pointer.next=None
            return pointer






    def get_position(self,position):
        pointer=self.head

        if self.head :
            for  count in range(position):

                count+=1
                if count==position :
                    return pointer
                pointer=pointer.next



            return None
        else:
            return None
    def insert(self,new_element,position):
        old_pointer=self.get_position(position)
        if position==1:
            temp=self.head
            self.head=new_element
            self.head.next=temp
        else:
            past_pointer=self.get_position(position-1)
            past_pointer.next=new_element
            new_element.next=old_pointer

    def delete(self,value):
        pointer=self.head
        prev=None
        if self.head:
            #this my code but it is not right when delteting any value theat doesnot exisit in the list it will remove the last element i should to take it easy and find more simple way to do it xd
            #while pointer.value!=value and pointer.next:
                #position+=1
                #pointer=pointer.next
            #if position==0 :
                #pointer.next=None
                #self.head=self.get_position(2)
                #pointer.next=-1

            #elif pointer.next==None and self.get_position(position)!=None :
                #self.get_position(position).next=None

            #else:    #self.get_position(position+1).next=-1   #idk
                #self.get_position(position).next=self.get_position(position+2)
            #self.get_position(position+1).next=-1
            while pointer.next and pointer.value!=value:
                prev=pointer
                pointer=pointer.next
            if pointer.value == value:
                if prev:
                    prev.next=pointer.next
                else:
                    self.head=pointer.next
class Stack(object):
    def __init__(self,top=None):
        self.ll=linked_list(top)

    def push(self,new_element):
        self.ll.insert_first(new_element)

    def pop (self):
        return self.ll.delete_first()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

stack=Stack(n1)
stack.push(n2)
stack.push(n3)
stack.push(n4)

print stack.pop().value

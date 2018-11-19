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

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

ll=linked_list(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

#test get_position
#print (ll.get_position(1).value)
#test insert
#ll.insert(n4,2)
#print (ll.get_position(2).value)

#test delete
ll.delete(5)
#print ll.head.value
print ll.get_position(1).value
print ll.get_position(2).value
print ll.get_position(3).value
print ll.get_position(4).value

'''
Given a linked list of characters. Write a python function to return a new string that is created by appending all the
characters given in the linked list as per the rules given below.
Rules:
Replace '*' or '/' by a single space
In case of two consecutive occurrences of '*' or '/', replace
those two occurrences by a single space and convert
the next character to upper case
Assume that
There will not be more than two consecutive occurrences of '*' or "/".
The linked list will always end with an alphabet
Sample Input
A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,
r,*,A,w,a,y

expected output:
An apple a day Keeps a Docter Away
'''
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class L:
    def __init__(self):
        self.head=None
    def disp(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
    def sol(self):
        curr=self.head
        s="*/"
        r=""
        t=""
        k=0
        while curr:
            if curr.data in s and k==0:
                k=1
                t=curr.data
                curr=curr.next
            if curr.data in s and k==1:
                if curr.data==t:
                    curr=curr.next
                    r+=" "+curr.data.upper()
                    curr=curr.next
                    k=0
                    t=""
                else:
                    r+=" "
                    curr=curr.next
                    k=0
            else:
                if k==1:
                    r+=" "
                k=0
                t=""
                r+=curr.data
                curr=curr.next
        return r
        
l=['n','*','/','a','p','p','l','e','*','a','/','day','*','*','k','e','e','p','s','/','*','a','/','/','d','o','c','t','o','r','*','A','w','a','y']
ll=L()
ll.head=Node('A')
curr=ll.head
for i in l:
    curr.next=Node(i)
    curr=curr.next
print(ll.sol())

##CacheProject
#dhruv nain

class ContentItem:
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

    __repr__=__str__


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class CacheList:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))     

    __repr__=__str__

    def __len__(self):
        return self.numItems
    

    def put(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        newnode=Node(content)
        if content.size>self.maxSize:
            return "Insertion not allowed. Content size is too large."

        if self.head==None: #if the list is empty and its size is less than 200 we always insert.
            self.head=newnode
            self.tail=newnode
            newnode.next=None
            self.numItems+=1
            self.remainingSize=self.remainingSize-content.size
            return ('{} {}'.format("INSERTED:",content))
        else:
            self.remainingSize=self.remainingSize-content.size
            if self.numItems==1: #if only 1 item
                if self.head.value.cid==content.cid:
                    self.remainingSize=self.remainingSize+content.size
                    return ('Insertion of content item {} not allowed. Content already in cache.'.format(content.cid))
            else:
                current=self.head
                while current.next is not None:#cheching if there is same object in the list
                    if current.value.cid==content.cid:
                        self.remainingSize=self.remainingSize+content.size
                        return ('Insertion of content item {} not allowed. Content already in cache.'.format(content.cid))
                    else:
                        current=current.next

            if evictionPolicy=='mru':
                if self.remainingSize<0:
                    self.remainingSize=self.remainingSize+content.size
                    while self.remainingSize<newnode.value.size:
                        self.remainingSize=self.remainingSize+self.head.value.size
                        self.numItems-=1
                        self.mruEvict()

                    if self.head==None: # if list is empty after making space.
                        self.head=newnode
                        self.tail=newnode
                        newnode.next=None
                        self.numItems+=1
                        self.remainingSize=self.remainingSize-content.size
                        return ('{} {}'.format("INSERTED:",content))

                    else:
                        newnode.next=self.head # adding at the head
                        self.head=newnode
                        self.numItems+=1
                        self.remainingSize=self.remainingSize-content.size

                        return ('{} {}'.format("INSERTED:",content))

                else:
                    newnode.next=self.head
                    self.head=newnode
                    self.numItems+=1
                    return ('{} {}'.format("INSERTED:",content))


            if evictionPolicy=='lru':
                if self.remainingSize<0:
                    self.remainingSize=self.remainingSize+content.size
                    while self.remainingSize<newnode.value.size:
                        self.remainingSize=self.remainingSize+self.tail.value.size
                        self.numItems-=1
                        self.lruEvict()

                    if self.head==None: # if list is empty after making space.
                        self.head=newnode
                        self.tail=newnode
                        newnode.next=None
                        self.numItems+=1
                        self.remainingSize=self.remainingSize-content.size
                        return ('{} {}'.format("INSERTED:",content))

                    else:
                        newnode.next=self.head # adding at the head
                        self.head=newnode
                        self.numItems+=1
                        self.remainingSize=self.remainingSize-content.size
                        return ('{} {}'.format("INSERTED:",content))

                else:
                    newnode.next=self.head
                    self.head=newnode
                    self.numItems+=1
                    return ('{} {}'.format("INSERTED:",content))


    def find(self, cid):
        # YOUR CODE STARTS HERE
        
        if self.numItems==0: # if list is empty then always a cache miss
            return "Cache miss!"
        elif self.numItems==1: # if only 1 item and that not what we are looking ofr then cache miss
            if self.head.value.cid==cid:
                return self.head.value
            else:
                return "Cache miss!"
        elif self.numItems==2: # if 2 itmes then either head is the what we are looking for or the tail 
            current=self.head
            if current.value.cid==cid:
                return current.value

            elif current.next.value.cid==cid:
                start=current
                last=current.next
                start.next=None
                last.next=self.head
                self.head=last
                return self.head.value
            else: # if neither then miss
                return "Cache miss!"
        else:
            current=self.head
            if self.head.value.cid==cid:
                return self.head.value

            elif self.tail.value.cid==cid:
                start=self.head
                last=None
                while start and start.next :
                    last=start
                    start=start.next
                last.next=None
                start.next=self.head
                self.head=start
                return self.head.value

            while current.next is not None: # if more then 2 elements 
                if current.next.value.cid==cid:
                    
                    if current.next.next==None:# if second last element
                        start=current
                        last=current.next
                        start.next=None
                        last.next=self.head
                        self.head=last
                    else:
                        start=current #else 
                        last=current.next
                        start.next=last.next
                        last.next=self.head
                        self.head=last

                    return self.head.value
                    
                else:
                    current=current.next
                return "Cache miss!"
        

                    
    def update(self, cid, content):
        # YOUR CODE STARTS HERE
        updatenode=Node(content)
        if self.numItems==0: 
            return "Cache miss!"
        elif self.numItems==1:
            if self.head.value.cid==cid:
                self.head=None
                self.head=None
                self.head=updatenode
                updatenode.next=None
                self.tail=updatenode
                return ('{} {}'.format("UPDATED:",self.head.value))
            else:
                return "Cache miss!"
        else: #code similar to LAB5 handson 
            current = self.head
            previous = None
            while current is not None and current.value.cid!=cid:
                previous=current
                current=current.next

            if current is None:
                return "Cache miss!"
            elif previous is None:
                self.head=current.next
                current.next=None
                self.head=updatenode
                updatenode.next=current.next
                return ('{} {}'.format("UPDATED:",self.head.value))

            elif current.next is None:
                previous.next=None
                self.tail=previous
                updatenode.next=self.head
                self.head=updatenode
                return ('{} {}'.format("UPDATED:",self.head.value))
            else:
                previous.next=current.next
                current.next=None
                updatenode.next=self.head
                self.head=updatenode
                return ('{} {}'.format("UPDATED:",self.head.value))
         


    def mruEvict(self):
        # YOUR CODE STARTS HERE
        if self.head.next==None:
            self.head=None
            self.tail=None
        else:
            current=self.head # removinh head from list
            self.head=current.next
            current=None
    
    def lruEvict(self):
        # YOUR CODE STARTS HERE
        if self.head.next==None: #removinh tail from list
            self.head=None
            self.tail=None
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
            self.tail=current
            
    def clear(self):
        # YOUR CODE STARTS HERE
        self.remainingSize=self.maxSize #bringback everything to 0 and making the list empty
        self.numItems=0
        current=self.head
        if current==None:
            pass
        if current.next==None:
            self.head=None
            self.tail=None
        else:
            while current is not None:
                self.head=current.next
                current.next=None
                current=None
                current=self.head
        return 'Cleared cache!'
class Cache:

    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__

    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    def hashFunc(self, contentHeader):
        # YOUR CODE STARTS HERE
        s1=0
        for i in contentHeader:# adding ascii codes of the header to find hash function
            s1=s1+ord(i)
        hf=s1%3
        return hf

    def insert(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        hf=self.hashFunc(content.header) #creating object of hashfunction
        if hf==0:
            return self.hierarchy[0].put(content,evictionPolicy)
        elif hf==1:
            return self.hierarchy[1].put(content,evictionPolicy)
        elif hf==2:
            return self.hierarchy[2].put(content,evictionPolicy)

    def retrieveContent(self, content):
        # YOUR CODE STARTS HERE
        hf=self.hashFunc(content.header) #creating object of hashfunction
        if hf==0:
            return self.hierarchy[0].find(content.cid)
        elif hf==1:
            return self.hierarchy[1].find(content.cid)
        elif hf==2:
            return self.hierarchy[2].find(content.cid)

        

    def updateContent(self, content):
        # YOUR CODE STARTS HERE
        hf=self.hashFunc(content.header) #creating object of hashfunction
        if hf==0:
            return self.hierarchy[0].update(content.cid, content)
        elif hf==1:
            return self.hierarchy[1].update(content.cid, content)
        elif hf==2:
            return self.hierarchy[2].update(content.cid, content)
        

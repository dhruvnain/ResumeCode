

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top==None#if there is nothing on the the top that means list is empty
        

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count
        


    def push(self,value):
        # YOUR CODE STARTS 
        nn=Node(value)
        if self.isEmpty():
            self.top=nn #the new node becomes the top
            self.top.next=None#since only one node, the next becomes none.
            self.count+=1
        else:
            nn.next=self.top #the top goes one position down.
            self.top=nn #the new node becomes the top
            self.count+=1

        
     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return 
        if self.__len__==1:
            a=self.top.value
            self.top==None#if stack only had the top then after popping stack is empty
            self.count-=1
            return a
        else:
            a=self.top
            self.top=a.next# the second element becomes the top
            self.count-=1
            return a.value

        

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return 
        else:
            return self.top.value #returns the value of the top node.
        
import re
import operator
class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
      
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in isNumber")
            return False
        try:
            float(txt)
            return True

        except (ValueError):
            return False

    def _getPostfix(self, txt):
        
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfix_Stack=Stack()
        txt=txt.strip()
        txt2=txt
        txt3=txt
        lst1=[]
        lst2=[]
        lst3=[]
        lst4=[]
        lst=['^','/','*','+','-']
        dicti={'^':3,'/':2,'*':2,'+':1,'-':1,'(':0}
        str1=''
        str2=''
        j=0
        x=0
        c1=0
        c2=0
        for i in range(0,len(txt)):#condition to check unbalanced paranthesis
            if txt[i]==')':
                c1+=1
            elif txt[i]=='(':
                c2+=1
            else:
                continue
        
        if c1 != c2:#condition to check unbalanced paranthesis
            return
        if txt[-1] in lst:#condition to check the last element isnt an operator
            return
        if txt[0]==')' or txt[-1]=='(':
            return 
        txt=txt.replace('(',' ')
        txt=txt.replace(')',' ')
        if txt[0]==')' or txt[-1]=='(':
            return
        tx=''
        for i in range(0,len(txt)):#condition to check no two operators are together
            if txt[i]==' ':
                continue
            else:
                tx+=txt[i]

        for i in range(0,len(tx)-1):#condition to check no two operators are together
            if tx[i] in lst and tx[i+1] in lst:
                return
            else:
                continue

        for j in range(0,len(txt)):
            for i in range(0,len(lst)):
                if txt[j]==lst[i]:
                    str1=str1+' '+txt[x:j]+' '#provides us a string of all numbers from the txt
                    str2=str2+txt[j]#provides us with a string containing all the operators 
                    x=j+1
                else:
                    continue
        
        str1=str1+' '+txt[x:]+' '
        for i in range(0,len(str2)):#condition to check if there are any non supported operators
            if str2[i] in lst:
                continue
            else:
                return
        
        y=0
        for i in range(0,len(str1)):#removing spaces from str1 and adding them to a list.
            if str1[i]==' ':
                lst1.append(str1[y:i])
                y=i+1
            else:
                continue
     
        for i in range(0,len(lst1)):#removing spaces and empty indexes from list.
            if lst1[i]=='':
                continue
            else:
                lst2.append(lst1[i])
        
        count=0
        for i in range(0,len(lst2)):
            if self.isNumber(lst2[i])==True:#putting each number into isnumber to check wether its valid or not
                count+=1
            else:
                return
        


        if count==len(lst2):
            res=re.split(r'(\^|\/|\*|\+|\-|\(|\)|\s)',txt3) #making list by splitting across all operators, spaces and paranthesis.
            for i in range(0,len(res),1):
                if res[i]==''or res[i]==' ': #ignore the spaces and empty indexes
                    continue
                else:
                    lst3.append(res[i])
            try:
                for i in range(0,len(lst3)):#trial to perform extracredit of multiplying when brackets are there
                    if lst3[i]=='(' and i!=0:
                        if self.isNumber(lst3[i+1]) :
                            if self.isNumber(lst3[i-1]) or lstr3[i-1]==')':
                                lst3.insert(i,"*")
                                str2+='*'
                                continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
            except:
                pass


            for i in range(0,len(lst3)):
                if lst3[i]=='(':#if an open bracket ,push it into the stack
                    postfix_Stack.push(lst3[i])
                elif lst3[i]==')':#if an closed bracket start poping from stack until you encounter an opening bracket
                    while postfix_Stack.peek() != '(':
                        lst4.append(postfix_Stack.peek())
                        postfix_Stack.pop()
                        
                    postfix_Stack.pop()#pop the opening bracket too
                elif lst3[i] in lst:
                    if postfix_Stack.isEmpty() or postfix_Stack.peek()=='(':# if empty or an opening brsacket on top then push operator in stack
                        postfix_Stack.push(lst3[i])
                    else:

                        if dicti[postfix_Stack.peek()]<dicti[lst3[i]]:# if the operator's precedence is more than operator on the top of the stack, push it on the stack
                            postfix_Stack.push(lst3[i])
                           
                        else:
                            

                            while (postfix_Stack.peek() != None) and dicti[postfix_Stack.peek()]>=dicti[lst3[i]]: #If the operator has a lower or equal precedence than the operator on the top of the stack, pop from the stack until this is not true.
                                lst4.append(postfix_Stack.peek())
                                postfix_Stack.pop()
                            postfix_Stack.push(lst3[i]) #push the incoming operator on the stack
                               

                else:
                    lst4.append(float(lst3[i])) #appends the numbers into the list

        else:
            return
        while postfix_Stack.peek()!=None:#the stack would have some operators left so to remove them from the stack 
            if postfix_Stack.peek() in lst:
                m=postfix_Stack.peek()
                lst4.append(m)
                postfix_Stack.pop()

            else:
                postfix_Stack.pop()

                    
                    
        str3= ' '.join([str(elem) for elem in lst4]) #putting elements from list to string 
        if len(lst2)-len(str2)==1: #if the numbers - number of operators != 1 that means its invalid
            return str3
        else:
            return 

                            

    @property
    def calculate(self):

        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculator_Stack=Stack()
        # YOUR CODE STARTS HERE
        lst5=[]
        postfixed=self._getPostfix(self.getExpr)#postfixing the expression
        
        if postfixed is None:
            return #if postfix returned None that means expression was invalid so calculate also return None.  
        lst5=postfixed.split() #splitting across space.
        operators={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,'^':operator.pow}#using a dictionary to convert operands from of string to real mathematical operands.
        if len(lst5)==0:
            return
        else:

            for i in lst5:

                if i in operators:
                    num1=float(calculator_Stack.peek())#num1 is the top number.
                    calculator_Stack.pop()
                    num2=float(calculator_Stack.peek())#num 2 is the 2nd number.
                    calculator_Stack.pop()
                    num3=operators[i](num2,num1)#performing the operation
                    calculator_Stack.push(num3)#pushing the solution into the stack
                    


                else:
                    calculator_Stack.push(i)#pushing numbers into the stack
            return calculator_Stack.peek()#returning the top value which is the 



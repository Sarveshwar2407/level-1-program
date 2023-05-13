#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=a+b
print("Sum=",c)


# In[3]:


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=a+b
b=c-b
a=c-a
print("value of a=",a)
print("value of b=",b)


# In[4]:


km=int(input("Enter km value"))
m=km*0.621371
print("miles=",m)


# In[5]:


a=int(input("Enter value:"))
if(a>0):
    print("It is positive value")
elif(a<0):
    print("It is negative value")
else:
    print("It is zero")


# In[6]:


year=int(input("Enter year value:"))
if(year%400==0)&(a%100==0):
    print("It is a leap year")
elif(year%4==0)&(year%100!=0):
    print("It is leap year")
else:
    print("It is not a leap year")


# In[8]:


lower=int(input("Enter lower limit value: "))
higher=int(input("Enter higher limit value: "))
for num in range(lower, higher + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[10]:


value=int(input("Enter value:"))
n1=0
n2=1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, value):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")


# In[13]:


a=int(input("Enter a number: "))
b=a//100
c=a%100
d=c//10
e=c%10
num=(b**c)+(d**3)+(e**3)
if num==a:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")


# In[16]:


num=int(input("Enter value: "))
a=0
if(num<=0):
    print("it is not a natural number")
else:
    for i in range(0,num+1):
        a=a+i
print(a)


# In[17]:


row=int(input("Enter number of lines: "))
for i in range(1,row+1):
    print("*"*i)


# In[18]:


s=input("Enter any string: ")
a=int(input("Enter how much to remove:"))
b=len(s)
print(s[a:])


# In[1]:


l=[1,5,8,10,31,62,85,30,40]
for i in l:
    if i%5==0:
        print(i)


# In[3]:


str=input("Enter the string :")
str2= 'hi'

count=str.count(str2)
print("Number of substring occurrences:",count)


# In[5]:


row=int(input("Enter number of lines: "))
for i in range(1,row+1):
    print("% s" % i*i)


# In[7]:


pal=input("Enter a number")
if pal==pal[::-1]:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")


# In[9]:


l=[5,2,3,4,1]
print("Before interchanging:  ",l)
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("After interchanging:  ",l)


# In[10]:


l=[5,4,3,2,1]
print("Before swapping: ",l)
x, y = int(input("Index one: ")), int(input("Index two: "))
l[x],l[y]=l[y],l[x]
print("After swapping: ",l)


# In[11]:


l=[12,22,14,32,24]

#using built-in function
print("Length of list: ",len(l))

#using for loop
c=0
for i in l:
    c+=1
print("Length of list: ",c)


# In[12]:


a=int(input("enter value 1: "))
b=int(input("enter value 2: "))
if a>b:
    print("Maximum value is= ",a)
else:
    print("Maximum value is= ",b)


# In[13]:


a=int(input("enter value 1: ")) 
b=int(input("enter value 2: "))
if a>b:
    print("Minimum value is= ",b)
else:
    print("Minimum value is= ",a)


# In[14]:


val=input("Enter sting value: ")
print("pallindrome checking:\n")
if val==val[::-1]:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
print("symmentrical checking:\n")

half=len(val)//2
if val[half:]==val[:half]:
    print("It is symmentrical")
else:
    print("It is not symmentrical")


# In[19]:


val=input("Enter sting value: ")
print(val[::-1])


# In[17]:


s=input("Enter the string :")
i=int(input("Enter index  value: "))
s1=s[:i]+s[i+1:]
print(s1)


# In[18]:


s=input("Enter the string :")

#using built-in function
print("Length of string: ",len(s))

#using for loop
c=0
for i in s:
    c+=1
print("Length of string: ",c)


# In[25]:


n=input("Enter the string :")
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)


# In[26]:


t=(1,2,3,4,5)
print(len(t))


# In[29]:


t=(24,18,6,14,25)
print("Maximum value= ",max(t))
print("Minimum value= ",min(t))


# In[30]:


t=(2,4,6,8)
print("Sum of elements in the tuple:",sum(t))


# In[31]:


tmatrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for row in tmatrix:
    s=sum(row)
    print("Row sum:",s)


# In[ ]:





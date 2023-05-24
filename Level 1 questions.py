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


# In[1]:


l = [1,2,3,4,5]
p = [(i, pow(i, 3)) for i in l]
print(p)


# In[3]:


Dict = {'rolex': 24, 'telex': 46,'levi': 36, 'erwin': 27, 'ryuk': 45}
K= list(Dict.keys())
K.sort()
sdict={i: Dict[i] for i in K}
print(sdict)


# In[5]:


d= {}
a,b,c= 5, 3, 10
p,q,r= 12, 6, 9
d["x-y+z"] = [a-b+c,p-q+r]
print(d)


# In[6]:


d={'x':455,'y':223,'z':300,'p':908 }
print("Dictionary: ", d)
print("sum: ",sum(d.values()))


# In[7]:


dic1 = {"A": 1,"B": 2,"C": 3}
print("Size of dic1: ",len(dic1))


# In[8]:


s={1,2,3,4,5}
print("Size of set: ",len(s))


# In[9]:


s=set("Hello_World")
for i in s:
    print(i)


# In[10]:


s={1,2,3,4,5}
print("Maximum of the set: ",max(s))
print("Minimum of the set: ",min(s))


# In[11]:


s={1,2,3,4,5}
print("Initial list: ",s)
s.remove(5)
print("Final list: ",s)


# In[12]:


s={1,2,3,4,5}
p={5,6,7,8,9}
for i in s:
    for j in p:
        if i==j:
            print("Element common is:", i)


# In[13]:


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("My matrix is:")
# Assign subsequent rows to the first row elements
for i in range(1, len(matrix)):
    matrix[i] = matrix[0]

print(matrix)


# In[14]:


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
 
# Printing elements of matrix1
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
 
# Printing elements of matrix2
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
 
# Subtracting two matrices
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
 
# Printing the result
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()


# In[15]:


elements = [1, 2, 3, 2, 1, 3, 4, 5, 4, 5, 5]

# Count the occurrences of each element
element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1

# Determine the dimensions of the matrix
num_rows = max(element_counts.values())
num_cols = len(element_counts)

# Create the matrix and fill it with the elements
matrix = [[None] * num_cols for _ in range(num_rows)]
for col, element in enumerate(element_counts):
    count = element_counts[element]
    for row in range(count):
        matrix[row][col] = element

# Print the resulting matrix
for row in matrix:
    print(row)


# In[16]:


matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))

# Perform row-wise element addition
row_sums = [sum(row) for row in zip(*matrix)]

# Print the row-wise sums
print("Row-wise sums:")
for sum_value in row_sums:
    print(sum_value)


# In[17]:


def create_even_submatrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1

    return matrix


# Test the function
n = 4
result = create_even_submatrix(n)

# Print the resulting matrix
for row in result:
    print(row)


# In[19]:


import inspect

def my_function(erwin,levi, mikasa):
    pass

# Get the parameter names of the function
parameters = inspect.signature(my_function).parameters
parameter_names = list(parameters.keys())

# Print the parameter names
print(parameter_names)


# In[21]:


name = "levi"
age = 30
city = "germany"

print(name, age, city)


# In[22]:


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# Example usage
base =int(input("Enter the base: "))
exponent =int(input("Enter the power: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")


# In[23]:


class grade:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return str((self.a, self.b))
  

g= [grade("ram", 'a'),
       grade("ravi", 'b'),
       grade("raj", 'c'),
       grade("mani", 'd'),
       grade("goku", 's')]
  

print(sorted(g, key=lambda x: x.b))


# In[24]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_kwargs(name="eren", age=18, city="germany")


# In[ ]:




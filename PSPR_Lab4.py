#!/usr/bin/env python
# coding: utf-8

# # Problem Solving Using Python and R Lab

# ## Lab-3  Python Functions and Modules 

# # Name    : `Berchmans Kevin S`
# 
# 

# ### Question 1. Create a function prime() that receives an integer and returns whether n is prime or not. Print all prime numbers from 1 to 100 by calling prime() function.

# In[ ]:


n=int(input("Enter an integer:")) 
def test_prime(n): 
    if (n==1): 
        return False 
    elif (n==2): 
        return True; 
    else: 
        for x in range(2,n): 
            if(n % x==0): 
             return False 
    return True 
print("Is it a prime number?:",test_prime(n)) 

start=1 
end=100 

def prime(): 
 for i in range(start, end+1): 
    if i>1: 
     for j in range(2,i):  
        if(i % j==0): 
         break 
 else: 
     print(i) 
prime() 


# ### Question 2. Develop a simple arithmetic calculator for 4 operations. The program should continue calculation until user types ‘q’ to quit.

# In[ ]:


while True:
    def add(num1 , num2):
        return num1 + num2
    def subtract(num1 ,num2):
        return num1 - num2
    def multiply(num1 , num2):
        return num1 * num2
    def divide(num1 , num2):
        if (num == 0):
            print("Cannot be dined by zero")
        else:
            return num1/num2
        
select = str("Select an Operator: ")
a = int(input("Enter value 1 "))
b = int(input("Enter value 2 "))
if select == '+':
    print(a, '+', b, '=', add(a,b))
elif select == '-':
    print(a, '-', b, '=', subtract(a,b))
elif select == '*':
    print(a, '*', b, '=', multiply(a,b))
elif select == '/':
    print(a, '/', b, '=', divide(a,b))
else:
    print("Invalid Input")
    
q = input("Type q to quit ")
if q=='q':
    break


# ### Question3. Create a function factorial() that takes an integer and returns its factorial value. 
#  You can create as a non-recursive version of factorial. 
# 
#  Also, check factorial of negative number does not exist. 
# 
#  Factorial of 0 is 1. 
# 
#  Save this Python file as factorial_definition.py. 
# Now, open another file and you can import factorial_definition.py as follows:
# 
#  import factorial_definition 
# 
#  You can call factorial function as factorial_definition.factorial(). 
# Now, print the following factorial values:
# 
# 1. factorial_definition.factorial(3) 
# 2. factorial_definition.factorial(5) 
# 3. factorial_definition.factorial(10)

# In[ ]:


def findFact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

print("Enter a Number: \n ", end="")
try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    
    fact1 = findFact(num1)
    fact2 = findFact(num2)
    fact3 = findFact(num3)
    
    print("\nFactorial of", num1, "=", fact1)
    print("\nFactorial of", num2, "=", fact2)
    print("\nFactorial of", num3, "=", fact3)
except ValueError:
    print("\nInvalid Input!")


# In[ ]:


while True:
    def add(num1 , num2):
        return num1 + num2
    def subtract(num1 ,num2):
        return num1 - num2
    def multiply(num1 , num2):
        return num1 * num2
    def divide(num1 , num2):
        if (num2==0):
            print("Cannot be dined by zero")
        else:
            return num1/num2
        
select = str("Select an Operator: ")
a = int(input("Enter value 1 "))
b = int(input("Enter value 2 "))
if select=="+":
    print(a, "+", b, "=", add(a,b))
elif select=="-":
    print(a, "-", b, "=", subtract(a,b))
elif select=="*":
    print(a, "*", b, "=", multiply(a,b))
elif select=="/":
    print(a, "/", b, "=", divide(a,b))
else:
    print("Invalid Input")
    
q = input("Type q to quit ")
if q=="q":
    break
    


# In[ ]:





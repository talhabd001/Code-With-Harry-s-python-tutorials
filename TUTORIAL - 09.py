                                               # TUTORIAL - 09
                                                # List
  # Example-01

#EX-01
num1=[]

num1.append(1)
print(num1)

#EX-02
num2=[]

num2.append(2)
num2.append(3)
num2.append(5)
num2.append(8)
print(num2)

#EX-02
num3=[2,5,6,8,4,0,1]

num3.append(777)
num3.append(778)
print(num3)

 # Example-02
num4=[4,2,3,0,1]

num4.insert(3,9)
print(num4)

num4.insert(1,7)
print(num4)


  # Example-03
num5=[1,5,6,7,0,3,8]

num5.remove(0)
print(num5)


  # Example-04

#EX-01
num6=[2,5,5,6,0]

num6.pop()
print(num6)

#EX-02
num7=[45,56,47,4654]

num7.pop()
print(num7)

print(" ",end='\n\n')     #not example
                                                  #Tuple
  # Example-01

#EX-01/mutable
numbers=[1,3,5,0]

numbers[2]=1000
print(numbers)

#EX-02/immutable
numbers2=(1,3,5,0)

numbers2 [2]=1000         #TypeError: 'tuple' object does not support item assignment
print(numbers2)  


                                                   #How to Inter-change

# Example-01/using variables idea

a="same"
b=5
temp=a
a=b
b=temp
print(a,b)

# Example-02/using python own

a="same"
b=5

a,b=b,a
print(a,b)

# Example-03

a=17
b='old'
c='years'
d='Saad is'

a,b,c,d= d,a,c,b
print(a,b,c,d)
                                     # TUTORIAL - 21
#01-Arithmetic Operators
print('5+6 is ',5+6)
print('5-6 is ',5-6)
print('5*6 is ',5*6)
print('50/5 is ',int(50/5))
print('56//6 is ',56//6)  #whithout int() , it will in float()
print('5**3 is ',5**3)
print('10%5 is ',10%5)

#02-Assignment operators

#example-01

x1=7
x1**=2    # x1=x1**2
print(x1)

#example-02
x=8

x+=7
print(x)
x-=6       #mojar bisoy holo,, akhane 8-6=2 howar kotha,
           # but seta 15-6=9(mane ager 8+7=15 er sathe 6 biyog hoyece ) hoiche
print(x)

#example-03
'''it can be questioned by any one that what need to add assignment operator?
is not it better to add any number  in one line (such as: x=5+7,x=5-1) ?
the answer is,  sometimes  we need to input number or operator(+,-,/,*) from user ,,
for this type of case we need this type of useful operators
the example is in below :
'''
#using input function and varriables ideas

x=5
var1=int(input('enter the number that you want to addition(+) with 5\n\t->'))
x+=var1
print(x)


#03-Comparison operators/tulona kora ke bujhai
i=5
print( i == 5)
print(i > 2)
print(i < 56)
print(i != 4 )
print(i >= 4 )
print(i >= 5 )
print(i <= 5 )  #je kono akta sorto mile gelei hobe(mane,, = or <)


#04- Logical operators
a= True
b= False

print(a and a)  #true and true=true
print(a or a)   #true or true=true
print(b and b)  #false and false=false
print(b or b)   #false or false=false
print(a and b)  #true and false=False
print(b and a)  #false and true=False
print(a or b)   #true or false=true

#05-Identity Operators
c=True
d=False

print(c is d)
print(c is not d)

print(56 is not 8)
print(6 is 6)


#06-Membership Operators
var1=[5,6,55,99,'saad']
var2={5,6,252,85,'salam'}

print(99 and 'saad' in var1)
print(5  not in var2)

#07-Bitwise Operators/it works with binarry (0,1) numbers

#0-00
#1-01
#2-10
#3-11

print(0 & 2)

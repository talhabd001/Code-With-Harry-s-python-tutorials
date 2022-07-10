                                                # TUTORIAL - 07
                                                 # Variable


var1="10"
var2="30"
var3=10
var4=30
var5="My age isn't "

print(var1+var2)
print(var3+var4)
print(var5+var1)

print(" ",end='\n\n')     #not example
                                                 #Type Casting

 #Example-01/use of type casting into variables
var6=int("70")
var7=float("30")

print(var6+var7)
print(" ",end='\n\n')     #not example

 #Example-02/use of type casting into print function
var8="70.0"
var9="20.0"

print(float(var8)+float(var9))
print(" ",end='\n\n')     #not example

 # Example-03/use of type casting for string
var10=150
var11=50

converter=str(var10)+str(var11)

print(converter)
print(" ",end='\n\n')     #not example

 # Example-04/ * of string

 #Ex-01 of 10*'string'
                                         #but in the case for number -print(10 * 10) = print(10x10)
print(10 * '...Hellow World!...',)       #& print(10 ** 10)= print(10x10x10x10x10x10x10x10x10x10) 10times

print(" ",end='\n\n')     #not example

# Ex-02 of 10*'string'
print(10 * 'MD\n''\tSaad\n' )

print(" ",end='\n\n')     #not example

# Ex-03 of 10*'string'
print(10 * 'MD\n\t''Saad\n' )


 # Example-05/ * of int/float
var12='10'
var13='10'

var14= int(var12)+int(var13)
print(10 * var14)

print(10 * str( int(var12)+ int(var13) ) )
print(" ",end='\n\n')     #not example



                                           #User Input
 #Example-01
print('Enter your number' )
var15=input()
print('You entered',int(var15)+10)

 #Example-02
print('You entered',int(input('Enter your number\n'))+10)



                                                        # Quize of tutor 7

print('My Calclulator\nCalculate any number :)')
print('----------------')
print('Start Here -->>>')

var1=int(input('Enter your first number\n-> '))
var2=int(input('Enter your secound number\n-> '))
sum=var1+var2
print('Your answer is \n\t-->> ',sum)
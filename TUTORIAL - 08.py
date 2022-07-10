                                                          # TUTORIAL - 08
                                                          # String Slicing

 # Example-01
mystr1 = 'I am a very lazy boy,it is really true :('

print(mystr1[21])
print(mystr1[39:41])
print(len(mystr1))
print(mystr1[0:80])

print(" ",end='\n\n')#not example

 # Example-02

#EX-01
mystr2= '123456789'
mystr3= '0123456789'

print(mystr2[6])
print(mystr3[6])

#EX-02
mystr4= '123456789'
mystr5= '0123456789'

print(mystr4[0:8])
print(mystr5[0:8])

print(mystr4[2:8])

#EX-03
mystr6= '123456789'
mystr7= '0123456789'

print(len(mystr6))
print(len(mystr7))

print(" ",end='\n\n')#not example

  # Example-03
mystr8= '123456789'

print(mystr8[5])
print(mystr8[0:6])
print(mystr8[0:6:2])

print(" ",end='\n\n')#not example

print(mystr8[0:])
print(mystr8[:])
print(mystr8[:7])
print(mystr8[0:9:1])
print(mystr8[::])

print(" ",end='\n\n')#not example

  # Example-03
mystr9= '123456789'

print(mystr9[-4])
print(mystr9[-4:-2])
print(mystr9[::-3])


                                                           #Some Function
 # Example-01
mystr10= 'I am a very good coder'
mystr11= 'Iamaverygoodcoder'

print(mystr10.isalnum())
print(mystr11.isalnum())

 # Example-02
mystr12= 'I am a very good coder'
mystr13= 'iamaverygoodcoder'

print(mystr12.isalpha())
print(mystr13.isalpha())

 # Example-03
mystr14= 'I am a very good coder'

print(mystr14.endswith('coder'))
print(mystr14.endswith('d coder'))
print(mystr14.endswith('d  coder'))

 # Example-04
mystr15= 'I am a very good coder'

print(mystr15.count('e'))
print(mystr15.count('E'))

 # Example-05
mystr16= 'i am a very good coder'

print(mystr16.capitalize())

 # Example-06
mystr17=  'i am a very good coder'

print(mystr17.find('is'))       #Q- Why showing -1?
print(mystr17.find('am'))

 # Example-07
mystr18= 'I AM A VERY GOOD CODER'

print(mystr18.lower ())

 # Example-08
mystr19= 'i am a very good coder'

print(mystr19.upper())

 # Example-09
mystr20= 'i are a very good coder'
mystr21= 'i am a very good coder'

print(mystr20.replace('are','am'))
print(mystr21.replace('i am a very good coder','Nothing to say'))


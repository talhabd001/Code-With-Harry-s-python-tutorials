                                                # TUTORIAL - 10
                                                # Dictionary

 # Example-01/tuple,list,dictonary
d1=()
d2=[]
d3={}

print(type(d1))
print(type(d2))
print(type(d3))


# Example-02/
#EX-01

d4={'A':'Apple','B':'Bag','C':'Cat','D':{'Dog','Dum','Domain'}}
print(d4['D'])

#EX-02
d5={'A':'Apple','B':'Bag','C':'Cat','D':{'da':{'dance','dad','daughter'},'db':{'dbeat','dbt','dibon'}}}
print(d5['D']['da'])

# Example-03/ add new values in dictionary
d6={'A':'Apple','B':'Bag','C':'Cat','D':{'Dog','Dum','Domain'}}
d6['E']={'Egg','Eat'}
d6['F']='Fail'
del d6['F']
print(d6)

# Example-04
#Ex-01/without .copy

d7={'A':'Apple','B':'Bag','C':'Cat'}
d8=d7
del d8['A']
print(d7)

#Ex-02/with .copy
d9={'A':'Apple','B':'Bag'}
d10=d9.copy()
del d10['A']
print(d9)

# Example-04/Other functions

#Ex-01
d11={'A':'Apple','B':'Bag','C':'Cat','D':{'Dog','Dum','Domain'}}
print(d11.get('A'))

#Ex-02
d12={'A':'Apple','B':'Bag','C':'Cat'}
d12.update({'D':{'Dog','Dum','Domain'}})
print(d12)

#Ex-03
d13={'A':'Apple','B':'Bag','C':'Cat','D':{'da':{'dance','dad','daughter'},'db':{'dbeat','dbt','dibon'}}}
print(d13.keys())

#Ex-04
d14={'A':'Apple','B':'Bag','C':'Cat','D':{'da':{'dance','dad','daughter'},'db':{'dbeat','dbt','dibon'}}}
print(d14.items())

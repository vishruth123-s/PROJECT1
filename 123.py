'''Dict={'a':1, 'b':2,'c':3,'d':4}
print(Dict)
print(len(Dict))
print(type(Dict))
print(Dict.get('b'))
print(Dict.keys())
print(Dict.values())
Dict.pop('a')
print(Dict)'''

'''Dict={'a':1, 'b':2,'c':3,'d':4}
print(list(Dict.keys())[0])
print(list(Dict.values())[0])'''

'''employee={'name':'Gowrish','age':18,'Salary':80000, 'Company':'Microsoft'}
for x in employee:
    print(x)
for y in employee.keys():
    print(y)
for i in employee.items():
    print(i)'''

Square={x:x**2 for x in range (6)}
print(Square)

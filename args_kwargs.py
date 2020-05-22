
### **kwargs example
def concate(**kwargs):
    new = ''
    for j in kwargs.values():
        new+=j
    return new


x=concate(company='Consultadd', training='Python', fname= 'sagar', lname='patel')
print(x)

## *args example
def sum(first,*args):
    sum = 0
    print("First: ",first)
    for i in args:
        sum+=i
    return sum

y = sum(1,2,3,4,5,6,7)
print(y)

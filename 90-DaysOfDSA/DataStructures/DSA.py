#array using list
x= [1,2,3,4,5]

x.append(6)
x.append(13)
x.append(11)
x.pop()
#print(x[-1])

#dictionary
y= {"a":"1", "b":"2", "c":3, 6:"f"}
#print(y.get(6))

z = (1,2,3,4,5)


#set

a = {"a", 3, "s", "e", 1}

a.add(9)
print(a)
from dataclasses import dataclass
#dataclasses
@dataclass
class Person:
    name: str
    address : str
    
print(Person)

#frozen set
a = frozenset(["a", 1, "f"])
print(a)


import sys

a=[1,2,3,4,5]  #creating a list memory is needed
b=a
c=b
del b   
del c 
           #deleting a meoryis freed
print(sys.getrefcount(a))



# class Poly:
#     def add(self,a,b):
#         return a+b
    
#     def add(self,a,b,c,):
#         return a+b
#     def add(self,a,b,c=2,d=3):
#         return a+b+c+d
    
# obj= Poly()
# print(obj.add(2,3)) 
#this is method overloading
#####################################################################
# class A:
#     def display(self):
#         print("this is class A")
# class B(A):
#     def display(self):
#         print("this is class B")
#         super().display()
# obj=B()
# obj.display() #this is method overriding
##############################################
class student:
    bank_name='sbi'
    def __init__(self,card):
       self._name= card['name']        #public
       self._accno=card['accno']       #protected
       self.__balance=card['balance']  #private
    
    
p1= student({"name": "Navya","accno": 12345,"balance": 5000})
print(p1._accno)
#print(p1.__balance)
print(p1._name)

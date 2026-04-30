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
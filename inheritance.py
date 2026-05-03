# class simCal:
#     def add(self,a,b):    #with out constarctor
#         return a+b
# class advCal(simCal):
#         def sub(self,a,b):
#             return a-b
# obj=advCal()
# print(obj.add(2,3))
# print(obj.sub(5,3))

 ####this is single inheritance#####
# class simCal:
#     def __init__(self,a,b):      #this is with constractor single inheritace
#          self.a=a
#          self.b=b
#     def add(self):
#         return self.a+self.b
# class advCal(simCal):
#     def sub(self):
#         return self.a-self.b
# obj=advCal(5,3)
# print(obj.add())
# print(obj.sub())

###########################################
# class simCal:
#     def __init__(self,a,b):      #this is with constractor multilevel inheritace
#          self.a=a
#          self.b=b
#     def add(self):
#         return self.a+self.b
# class advCal(simCal):
#     def sub(self):
#         return self.a-self.b
# class supCal(advCal):
#         def mul(self):
#             return self.a* self.b
# obj=supCal(5,3)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())

###########################################################
# class simCal:
#     def __init__(self,a,b):      #this is  multiple inheritace
#          self.a=a
#          self.b=b
#     def add(self):
#         return self.a+self.b
# class advCal:
#     def sub(self):
#         return self.a-self.b
# class supCal(advCal,simCal):
#         def mul(self):
#             return self.a* self.b
# obj=supCal(5,3)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())
####################################
# class simCal:
#     def __init__(self,a,b):      #this is hirarchical inheritace
#          self.a=a
#          self.b=b
#     def add(self):
#         return self.a+self.b
# class advCal(simCal):
#     def sub(self):
#         return self.a-self.b
# class supCal(simCal):
#         def mul(self):
#             return self.a* self.b
# obj=supCal(5,3)
# obj1=advCal(5,3)
# print(obj.add())
# print(obj1.sub())
# print(obj.mul())
#########################################################################
# class simCal:
#     def __init__(self,a,b):      #this is  multiple inheritace
#          self.a=a
#          self.b=b
#     def add(self):
#         print('sim add')
#         return self.a+self.b
# class advCal:
#      def __init__(self,a,b):      #this is  multiple inheritace
#          self.a=a
#          self.b=b
#      def sub(self):
#         return self.a-self.b
#      def add(self):
#         print('adv add')
#         return self.a+self.b
# class supCal(simCal,advCal): #this is method resokution order(MRO)
#      def mul(self):
#             return self.a* self.b
# obj=supCal(5,3)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())
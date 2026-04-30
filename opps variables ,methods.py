class dressshop:
    shop_name ='mangalya'
    shop_established=' boduppal'
    def __init__ (self,model,price):
        self.__model= model
        self.__price= price
    def get_dress_details(self):
        return {self.__model,self.__price}
    @classmethod
    def get_shop_details(cls):
        return{'shopname':cls.shop_name,'shopdetails':cls.shop_established}
    @staticmethod
    def welcome_sir():
        return {'welcome sir'}
    
    
p1= dressshop( 'panjabimoel',800)
print(dressshop.get_shop_details())   # global access   direct class nametho access cheyyochu
print(p1.get_shop_details()) # this object nametho access cheyyochu
print(p1.get_dress_details())
print(dressshop.welcome_sir())  #class  nametho access cheyyochu
print(p1.welcome_sir())         # object nametho access cheyyochu
    
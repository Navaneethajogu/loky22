

# prime numbers
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
         
 #########################################################################
        
# num=9
# is_prime=True
# for i in range(2,num):
#   if(num%i==0):
#     is_prime=False
#     print(i)
#     break       # breac use cheyadam valla loop  first factorial daggara stop avuthundhi next numbers check cheyadhi ( fast and time complexty is less)
# print( is_prime)
# if(is_prime):
#   print("this is a prime number")
# else:
#   print("this is not a prime number")


########################################################
# def is_prime(n):
#   for i in range(2,n):
#     print(i)
#     if(n%i==0):
#       return False
#   return True

# res=is_prime(97)
# print (res)
# if(res):
#   print("this is prime number")
# else:
#   print("this is not a prime number")
  
  #########################################################
#   Optimised approach :
# def is_prime(n):
#   for i in range(2,n//2):
#     print(i)
#     if(n%i==0):
#       return False
#   return True

# res=is_prime(97)
# if(res):
#   print("this is prime number")
# else:
#   print("this is not a prime number")



#####################################################

#Optimal approach :
# import math

# def is_prime(n):
#   for i in range(2,int(math.sqrt(n))):
#     print(i)
#     if(n%i==0):
#       return False
#   return True

# res=is_prime(97)
# if(res):
#   print("this is prime number")
# else:
#   print("this is not a prime number")


#######################################
for num in range(2, 21):   # numbers from 2 to 20
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
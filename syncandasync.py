import asyncio
from threading import Thread
import time
import multiprocessing

# async def waiter( juice,time):
#     print( juice,"waiting for the juice")
#     print(f" please wait {time} minuts ")
#     await asyncio.sleep(time)
#     print(juice,"juice is completed")
# t1=waiter("apple",5)
# t2=waiter("apple",6)
# t3=waiter("apple",3)
# t4=waiter("apple",4)

# async def trigger_at_a_time():
#     await asyncio.gather(t1,t2,t3,t4)
# start=time.time()
# asyncio.run(trigger_at_a_time())
# print(time.time() - start)  
# ###############################################################################

# def waiter(juice,t):
#     print( juice,"waiting for the juice",t)
#     time.sleep(t)
#     print(juice,"juice is completed")
    
# t1=waiter("apple",5)
# t2=waiter("banana",6)
# t3=waiter("mango",3)
# t4=waiter("orange",4)

#####################################################
# def order(menu,t):   #this is threading 
#     print(f" your {menu} is prepairing ")
#     print(f" please wait {t} minuts ")
#     time.sleep(t)
#     print(f" your {menu} is completed ")
    
# t1=order
# t2=order
# t3=order
# t4=order
# w1=Thread(target=t1,args=("apple", 5))
# w2=Thread(target=t2,args=("banana", 7))
# w3=Thread(target=t3,args=("orange", 4))
# w4=Thread(target=t4,args=("mango", 6))
# start=time.time()
# w1.start()
# w2.start()
# w3.start()
# w4.start()
# w1.join()
# w2.join()
# w3.join()
# w4.join()
# end=time.time()
# print(end-start)
###############################################################################
def sum(num):
    print(multiprocessing.current_process().name)
    time.sleep(num)
    res=0
    for i in range(num):
         res+=i
    return res
if __name__=="__main__":
    with multiprocessing.Pool(processes=6) as p:
        start=time.time()
        res= p.map(sum,[1,2,3,4])
        end=time.time()
        print(end-start)
        print(res)


    
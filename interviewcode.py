import threading
import time
from datetime import datetime
import random
#員工&肉品數量
employees = ['A','B','C','D','E']
meats = {
    '牛肉' : 10,
    '豬肉' : 7,
    '雞肉' : 5
    }

#取肉&處理肉
def Employee_work(name):
    while(len(meats) != 0):
        #取肉
        lock.acquire()
        choosemeat = random.choice(list(meats))
        #取肉後若沒肉了則dict刪除該肉品
        meats[choosemeat] -=1
        for meat in list(meats):
            if meats[meat] == 0:
                del meats[meat]
        print('{} 在 {} 取得{}'.format(name,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),choosemeat))
        lock.release()
        #處理時間
        if choosemeat == '牛肉':
            time.sleep(1)
        elif choosemeat == '豬肉':
            time.sleep(2)
        elif choosemeat == '雞肉':
            time.sleep(3)
        print(('{} 在 {} 處理完{}'.format(name,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),choosemeat)))
        
  

lock = threading.Lock()
for employee in employees:
    threading.Thread(target=Employee_work,args=(employee,)).start()

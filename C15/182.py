#1.1.跨目录调用
import sys
sys.path.append("./C13")
from C13 import carter

carter.printName()

#1.2 同一目录调用
from carter import printName

printName()

# 3
import random

for i in range(5):
    print (random.randint(1,20))

#4
import random
import time

for i in range(10):
    print (random.random())
    time.sleep(3)
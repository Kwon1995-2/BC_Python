# import myModule
# hab = myModule.sum(10)
# pwr = myModule.power(2,3)
# print(hab, pwr)

import sys, myModule

cnt = len(sys.argv)
if cnt == 2:
    result = myModule.sum(int(sys.argv[1]))
elif cnt == 3:
    result = myModule.power(int(sys.argv[1]), int(sys.argv[2]))
else :
    result = "Usage : python myTest.py n [m]"
print(result)
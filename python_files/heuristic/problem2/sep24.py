import OptimalTouring as Game
from OptimalTouring import OptimalTouring
x = Game.OptimalTouring("sites.txt")
'''
i = 1
while x.getTime() < x.getDay()*1440:
    x.sendMove(siteId=i)
    x.sendMove(delayTime=240)
    i += 1
x.settlement()

#OptimalTouring().getState("sites.txt")

print('ok',x.getState()[0])
'''

#print(x.send(siteId = 1))

#x.sendMove(siteId = 1)

print('ok',x.getState()[3])

x_location = x.getState()[3][i][0]
y_location = x.getState()[3][i][1]
time_required = x.getState()[3][i][2]
value = x.getState()[3][i][3]
open_time = x.getState()[3][i][4][0]
close_time = x.getState()[3][i][4][1]

'''
动态规划 每一天做一次动归，因为第二天可以从新的点开始
动归的初始点可以是1。开始时间最早 2.价值最高 或者可以都做，二选一。或者开始时间最早+30分钟，这其中价值最高的
'''
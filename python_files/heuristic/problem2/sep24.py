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

'''

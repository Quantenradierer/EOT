# -*- coding: utf-8 -*-

import datetime

from logic.entities.human import Human
from logic.scheduler import Scheduler
from world.vector2d import Vector2D
from world.world import World
import constants

start = datetime.datetime.now()

scheduler = Scheduler()


for i in range(constants.NPCS):
    scheduler.AddAction(0, Human(0, Vector2D(0,0), constants.NAMES[i]))

scheduler.Schedule(0, constants.ROUNDS)


end = datetime.datetime.now()


for time in range(constants.ROUNDS - 10):
    World.entities[0].Get(time, "Position")
    #Output(t)
    #sleep(constants.SLEEP_TIME)

end2 = datetime.datetime.now()


print "Dauer Datenerzeugung:", end - start
print "Dauer Datenlesen:", end2 - end

raw_input("TEST")

World.entities

'''
while True:
    times = list(scheduler.times)
    times.sort()
    if times: 
        scheduler.Schedule(times[0])

        time.sleep(0.1)
        Output()
            
    else:
        break

#print A.actions
#print B.actions
#print C.actions
#print D.actions



'''



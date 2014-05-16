# -*- coding: utf-8 -*-

from logic.entities.entity import Entity
from logic.action import Action
from world.action import DefaultAction
from world.world import World
from logic.base.rand import Random
from world.vector2d import Vector2D
from logic.scheduler import Scheduler

from constants import RESEED_TIME, GROW_TIME

class Grow(Action):
    def Start(self, time):
        Action.Start(self, time)
        self.needed = 10

    def Stop(self, time):
        Action.Stop(self, time)
        if self.IsDone(time):
            self.world_entity.data.Change(time, "Icon", "T")

class Plant(Action):
    def Start(self, time):
        Action.Start(self, time)
        self.needed = 30

    def Stop(self, time):
        Action.Stop(self, time)
        if self.IsDone(time):
            add_x = Random.randint(self.world_entity, -1, 1, seed=time)
            add_y = Random.randint(self.world_entity, -1, 1, seed=time + 1)
            plant_position = self.world_entity.data.Get(time, "Position") + Vector2D(add_x, add_y)

            if World.IsInWorld(plant_position):
                if not World.GetEntitiesOnPosition(time, plant_position):
                    entropy = Random.random(self.world_entity, seed=time)
                    Scheduler.instance.CreateEntity(Tree, entropy, plant_position)

class Tree(Entity):
    def __init__(self, *args, **kwargs):
        Entity.__init__(self, icon="t", *args, **kwargs)
        self.replants = 10

    def GetNextAction(self, time):
        if self.replants:
            if self.world_entity.GetLatest("Icon") == "t":
                return Grow(self.world_entity)
            if self.world_entity.GetLatest("Icon") == "T":
                self.replants -= 1
                return Plant(self.world_entity)
        else:
            return Action(self.world_entity)

# -*- coding: utf-8 -*-
import sys

class Type():
    def __init__(self, entropie, position, icon = ""):
        self.icon     = icon
        self.position = position
        self.entropie = entropie
        self.actions  = []
    
    def GetPosition(self):
        return self.position
    
    def Action(self):
        if self.actions:
            self.StopAction()
        self.AddAction()      

    def StopAction(self):
        return None
        
    def AddAction(self):
        return None

    def __repr__(self):
        return self.icon
        
        
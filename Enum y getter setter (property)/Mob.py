from enum import Enum
import random


class MobRace(Enum):
    SKELETON = 1
    ZOMBIE = 2
    RAT = 3

class Mob:

    def __init__(
        
        self,
        race,
        hp,
        dmg
                 ):

        self.race = race
        self.hp = hp
        self.dmg = dmg



    @property
    def race(self):
        return str(self._race).split('.')[1].lower().title()


    @race.setter
    def race(self, race: MobRace):
        if race not in MobRace:
            raise Exception
        self._race = race


    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp


    @property
    def dmg(self):
        return self._dmg
    
    @dmg.setter
    def dmg(self, dmg):
        self._dmg = dmg

        
    def __str__(self):
        return f'Mob\nRace: {self.race}\nHP: {self.hp}\nDMG: {self.dmg}'


    def __repr__(self): 
        return f'<Mob {race} {self.hp} {self.dmg}>'



#m1 = Mob(MobRace.SKELETON,100,25)

#print(str(m1))

mobs = []
for r in MobRace:
    mobs.append(Mob(r,100, 25))

for m in mobs:
    print(m, '\n')
mobs[2].dmg = 5  
print(mobs[2])

from char_flyweight import Flyweight
from character import Character

#Singleton implementation

class CharFactory:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getFlyweight(self,unicode):
        unicodeChar = Character.getCharacter(unicode)
        flyweightObj = Flyweight(unicodeChar)
        return flyweightObj
    
    

    

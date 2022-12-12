from char import CharFlyweight
from character import Character

#Singleton implementation of a Character factory for Flyweight pattern implementation

class CharFactory:
    __instance = None

    '''
    desc: Function for creating single point of access. 
    '''
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    '''
    desc: Function for returning the character flyweight class object for the character fetched based on the unicode
    input: Character Unicode
    output: Character Flyweight object
    '''
    
    def getFlyweight(self,unicode):
        unicodeChar = Character.getCharacter(unicode)
        flyweightObj = CharFlyweight(unicodeChar)
        return flyweightObj
    
    

    

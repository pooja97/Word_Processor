#Font Flyweight Factory
from font import Font
class FontFactory:

    #Singleton implementation
    __instance = None

    def __new__(cls,*args, **kwds):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def getFontObj(self,name,size,type):
        font = Font(size,name,type)
        return font
        



    
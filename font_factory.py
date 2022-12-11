#Font Flyweight Factory
from font import Font
class FontFactory:

    #Singleton implementation
    __instance = None

    '''
    desc: Function for creating single point of access. 
    '''
    def __new__(cls,*args, **kwds):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    '''
    desc: Function for creating Font class object
    input: Font name, Size and type
    output: returns Font class object
    '''
    
    def getFontObj(self,name,size,type):
        font = Font(size,name,type)
        return font
        



    
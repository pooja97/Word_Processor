#Font Flyweight Factory
class FontFactory:

    #Singleton implementation
    __instance = None

    def __new__(cls,*args, **kwds):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self,name,size,style):
        self.name = name
        self.size = size
        self.style = style


    
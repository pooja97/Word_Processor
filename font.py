#Font flyweight class
'''
desc: Font class which stores the font name, size and type
'''
class Font:
    def __init__(self,name,size,type):
        self.name = name
        self.size = size
        self.type = type

        
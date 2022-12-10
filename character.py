class Character:
    char_dict = {}

    def charUnicode(self,char):
        unicode = ord(char)
        self.char_dict[unicode] = char
    
    def getCharacter(uniCode):
        if uniCode not in Character.char_dict.keys():
            Character.char_dict[uniCode] = chr(uniCode)
        return Character.char_dict[uniCode]

    def cha(self):
        return self.char_dict
    
class Character:
    char_dict = {}

    '''
    desc: Function for storing the unicode along with the character in a dictionary. Key : Unicode, Value: Character
    input: character
    '''
    def charUnicode(self,char):
        unicode = ord(char)
        self.char_dict[unicode] = char
    

    '''
    desc: Function for getting the character based on the unicode
    input: Unicode
    output: Character 
    '''
    def getCharacter(uniCode):
        if uniCode not in Character.char_dict.keys():
            Character.char_dict[uniCode] = chr(uniCode)
        return Character.char_dict[uniCode]


    '''
    desc: Function for returning the character dictionary with its unicode and the character
    input: Character dictionary
    '''
    def cha(self):
        return self.char_dict
    
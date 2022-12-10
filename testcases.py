from character import Character
from char_factory import CharFactory
from font_factory import FontFactory

if __name__ == "__main__":
    charObj = Character()
    charObj.charUnicode('A')
    charObj.charUnicode('a')
    charObj.charUnicode('B')
    charObj.charUnicode('C')
    charObj.charUnicode('!')

    print(charObj.cha())

    # print(Character.getCharacter(65))
    # print(Character.getCharacter(99))


    #charfactory 
    CharFactoryObject = CharFactory()
    CharFlyweightObject = CharFactoryObject.getFlyweight(34)
    # print(CharFlyweightObject)


    charfactoryobject = CharFactory()

    # print(CharFactoryObject)
    # print(charfactoryobject)

    font1 = FontFactory('T',12,'I')

    font2 = FontFactory('T',14,'B')

    # print(font1)
    # print(font2)

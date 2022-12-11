from character import Character
from char_factory import CharFactory
from font_factory import FontFactory
from runarray import RunArray


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

    font1 = FontFactory()

    font2 = FontFactory()


    test = RunArray()
    test.addRun(0,2,'A')
    test.appendRun(10,'B')
    test.addRun(3,6,'C')
    test.runArrayPrint()
    test.appendRun(15,'D')
    test.runArrayPrint()

    print(font1.getFontObj('Times',11,'Italic'))
    print(font2.getFontObj('Times',12,'Bold'))



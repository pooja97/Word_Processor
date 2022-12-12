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
    test.addRun(0,2,font1.getFontObj('Ariel',10,'Bold'))
    test.appendRun(10,font1.getFontObj('Times New Roman',10,'Bold'))
    test.addRun(3,6,font1.getFontObj('Verdana',15,'Italic'))
    test.appendRun(15,font1.getFontObj('Calibri',8,'Underline'))
    # test.runArrayPrint()

    # print(font1.getFontObj('Times',11,'Italic'))
    # print(font2.getFontObj('Times',12,'Bold'))



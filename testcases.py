from character import Character
from char_factory import CharFactory
from font_factory import FontFactory
from runarray import RunArray
from sizeCheck import sizeCheck

if __name__ == "__main__":

    '''
    Character class object which takes character as a input and store it's unicode
    '''
    charObj = Character()
    charObj.charUnicode('A')
    charObj.charUnicode('a')
    charObj.charUnicode('B')
    charObj.charUnicode('C')
    charObj.charUnicode('!')

    print(charObj.charDict())

    '''
    prints the character given a unicode
    '''
    print("Character with Unicode 65 is: ",Character.getCharacter(65))
    print("Character with Unicode 99 is: ",Character.getCharacter(99))


    '''
    Character factory object which returns the character flyweight object given the unicode of the character
    '''
    charFactoryObject = CharFactory()
    charFlyweightObject = charFactoryObject.getFlyweight(34)


    '''
    Font factory object which returns the Font class object given Font name,size and type
    '''
    fontFactory = FontFactory()
    Fontfactory = FontFactory()

    '''
    Checking the Font factory object. As it has a single point of access, both the object should be same 
    '''
    print("Font Factory object: ",fontFactory)
    print("Font Factory object: ",Fontfactory)



    '''
    RunArray class object which stores the run of the Font in the document. Stores the Font class object given its start and end position
    '''
    runArray = RunArray()
    runArray.addRun(0,2,fontFactory.getFontObj('Ariel',10,'Bold'))
    runArray.appendRun(10,fontFactory.getFontObj('Times New Roman',10,'Bold'))
    runArray.addRun(3,6,fontFactory.getFontObj('Verdana',15,'Italic'))
    runArray.appendRun(15,fontFactory.getFontObj('Calibri',8,'Underline'))
   

    '''
    Prints the object size with Flyweight pattern
    '''
    print("Object size using Flyweight: ", sizeCheck.getSize(charFactoryObject,charFlyweightObject,fontFactory,runArray))


    '''
    Prints the object size without flyweight pattern
    '''
    print("Object size without using Flyweight: ",sizeCheck.Checksize('A'))

    




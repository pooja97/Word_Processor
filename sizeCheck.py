import sys
from unsharedcharacter import UnsharedCharacter
from char import CharFlyweight
from font import Font



class SizeCheck:
    total_sum = 0
    count = 0

    '''
    desc: Function for getting average object size using Flyweight pattern
    Output: Returns the average object size using Flyweight Pattern
    '''
    def getSize(charFactory,charFlyweight,fontFlyweight,runArray):
        for v in locals().values():
            SizeCheck.count+=1
            SizeCheck.total_sum+= sys.getsizeof(v)

        return SizeCheck.total_sum/SizeCheck.count

    '''
    desc: function for checking the object size without using Flyweight Pattern
    Output: Returns the Object size without using Flyweight Pattern
    '''

    def checkSize(ch):
        chList = list()
        chList.append(UnsharedCharacter(CharFlyweight(ch),Font('Times',12,'Bold')))
        return sys.getsizeof(chList)


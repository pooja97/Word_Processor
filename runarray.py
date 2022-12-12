
class RunArray:
    #[start,end,font]
    def __init__(self):
        '''
        desc: runArray for storing document font's start, end and font data
        '''
        self.runArray = [] 

    '''
    desc: Adding the font run with the start and end value in the runarray
    input: Start, End, and the Font value
    '''
    def addRun(self,start,end,font):
        # fontlist = [font]*(end-start)
        # self.runArray[start:end] = fontlist
        self.runArray.append([start,end,font])

    '''
    desc: function for appending the font run with the end value in the runarray
    input: End and the Font value
    '''
    def appendRun(self,end,font):
        # fontlist = [font]*(end - len(self.runArray))
        # self.runArray.extend(fontlist)
        self.runArray.append([end,font])

    '''
    desc: Function for printing the runArray
    '''
    def runArrayPrint(self):
        print(self.runArray)


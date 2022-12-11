class RunArray:
    #[start,end,font]
    def __init__(self):
        self.runArray = []  

    #adding the font run with the start and end value in the runarray
    def addRun(self,start,end,font):
        fontlist = [font]*(end-start)
        self.runArray[start:(end)] = fontlist
    
    #appending the font run at the end of the runarray
    def appendRun(self,end,font):
        fontlist = [font]*(end - len(self.runArray))
        self.runArray.extend(fontlist)

    def runArrayPrint(self):
        print(self.runArray)


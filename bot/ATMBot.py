class ATMBot(object):
    def __init__(self):
        self.yes = 1
        self.no = 1
        self.location = ""
        self.minBill = ""
        self.gonnaUpdate = False
    def __str__(self):
        print(self.yes)
        print(self.no)
        print(self.location)
        print(self.minBill)
        print(self.gonnaUpdate)
        return ""
    #Setters    
    def countYes(self):
        self.yes=self.yes+1
    def countNo(self):
        self.no=self.no+1
        self.gonnaUpdate = False
    def setLocation(self, location):
        self.location = location
    def setMinBill(self, minBill):
        if( (int)(minBill) < (int)(self.minBill) or self.minBill == ""):
            self.minBill = minBill
    def setGonnaUpdate(self, gonnaUpdate):
        self.gonnaUpdate = gonnaUpdate
    
    #Getters
    def getLocation(self):
        return self.location
    def getMinBill(self):
        return self.minBill
    def getYes(self):
        return self.yes
    def getNo(self):
        return self.no
    def isGonnaUpdate(self):
        return self.gonnaUpdate

    def analyze(self):
        percentage = (int) (self.yes * 100 / (self.yes + self.no))
        if percentage >= 0 and percentage <10:
            worksStr = " doesn't work"
        elif percentage >= 10 and percentage <50:
            worksStr = " probably doesn't work" 
        elif percentage >= 50 and percentage <90:
            worksStr = " probably works"
        elif percentage >= 90 and percentage <=100:
            worksStr = " works"
        percentageStr = "("+(str)(percentage)+"%)"
        ansStr = self.location + worksStr + percentageStr + "\n"
        if(self.minBill != ""):
            ansStr = ansStr + "Minimum bill in " + self.location + " is: " + self.minBill
        else:
            ansStr = ansStr + "Information about minimum bill in " + self.location + " is unavailable right now"
        return ansStr
    
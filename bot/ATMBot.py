class ATMBot(object):
    def __init__(self):
        self.yes = 1
        self.no = 0
        self.location = ""
        self.minBill = 0
    
    #Setters    
    def countYes(self):
        self.yes=self.yes+1
    def countNo(self):
        self.no=self.no+1
    def setLocation(self, location):
        self.location = location
    def setMinBill(self, minBill):
        self.minBill = minBill
    
    #Getters
    def getLocation(self):
        return self.location
    def getMinBill(self):
        return self.minBill
    def getYes(self):
        return self.yes
    def getNo(self):
        return self.no

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
        ans = self.location + worksStr + percentageStr;
        return ans
    
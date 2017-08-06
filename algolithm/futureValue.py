 #
 #
 # @param {number} pYen - Amount to look for future value
 # @param {number} pRate - Annual interest rate
 # @param {number} pYear - Operating year
 #
 # @return {number} future value
 #
class FutureValue:

    def __init__(self,year,yRate,yen):

        self.year = year
        self.yRate = yRate
        self.yen = yen

    def calc(self):

        value = self.yen * (1 + self.yRate/100.0) ** self.year

        return value

futureValue = FutureValue(2,5,1000000)

print(futureValue.calc())
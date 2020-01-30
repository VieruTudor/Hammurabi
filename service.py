import random


class Error(Exception):
    pass


class Service:
    def __init__(self, year):
        self.currentYear = year
        self.gameLost = False
        self.gameWon = False

    '''
    Function that receives from UI an amount of acres to buy, checks if the amount is available for purchase or sell
    Selling : adds the grain for the sold land, depending on the current year price, then subtracts the sold land
    Buying : subtracts the grain for the bought land, then adds the bought land
    '''

    def serviceBuyAcres(self, acresToBuy):
        if acresToBuy < 0:  # selling
            acresToSell = acresToBuy
            if abs(acresToSell) > self.currentYear.acres:
                raise Error("You cannot sell more than you have")
            else:
                self.currentYear.grain += abs(acresToSell) * self.currentYear.landPrice
                self.currentYear.acres += acresToSell
        if acresToBuy > 0:  # buying
            if acresToBuy * self.currentYear.landPrice > self.currentYear.grain:
                raise Error("You don't have enough grains to buy this land.")
            else:
                self.currentYear.acres += acresToBuy
                self.currentYear.grain -= acresToBuy * self.currentYear.landPrice

    def getYear(self):
        return self.currentYear.year

    '''
    Function that receives from UI a number of units to feed to the people, checks if the amount is available, then
    proceeds to subtract the fed units from the available grains, and computes the number of starving persons, based
    on the population and the number of units that received grains.
    '''

    def serviceFeedPopulation(self, unitsToFeed):
        if unitsToFeed < 0:
            raise Error("Insert a value >= 0")
        if unitsToFeed > self.currentYear.grain:
            raise Error("You can't feed that many people")
        if unitsToFeed // 20 > self.currentYear.population:
            raise Error("You cannot feed more people than you have.")
        self.currentYear.grain -= unitsToFeed
        self.currentYear.rip = self.currentYear.population - unitsToFeed // 20

    '''
    Function that gets from UI the number of acres to plant for the next year, checks if they can be planted then
    proceeds to subtract the planted acres from the available grains
    '''

    def servicePlantAcres(self, acresToPlant):
        if acresToPlant > self.currentYear.acres:
            raise Error("You cannot plant more acres than you have")
        if acresToPlant > self.currentYear.grain:
            raise Error("You cannot plant more grains than you have")
        else:
            self.currentYear.plantedAcres = acresToPlant
            self.currentYear.grain -= acresToPlant

    '''
    Based on the current year information and uncontrollable variables (land price, probability of rats to occur, the
    harvest amount for each acre and the new people that came in town if no one starved), updated the next year starting
    point
    - Old stats, population, acres, grains
    - The new people that came into town if no one starved
    - The price for the land
    - The harvest amount for each acre
    - The probability of rats appearing
    '''

    def newYear(self):
        self.currentYear.year += 1
        self.currentYear.harvest = random.randint(1, 6)
        self.currentYear.grain += self.currentYear.plantedAcres * self.currentYear.harvest
        self.currentYear.landPrice = random.randint(15, 25)

        if self.currentYear.rip == 0:  # if nobody died, get new people
            newPeople = random.randint(0, 10)
            self.currentYear.newPeople = newPeople
            self.currentYear.population += newPeople
        else:  # somebody ded
            originalPopulation = self.currentYear.population
            self.currentYear.population -= self.currentYear.rip
            if self.currentYear.population < originalPopulation // 2:
                self.gameLost = True
            self.currentYear.newPeople = 0
        chanceList = [False, False, False, False, True]
        ratsChance = random.randint(0, 4)
        print(chanceList[ratsChance])
        if chanceList[ratsChance] is True:
            self.currentYear.rats = (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) * self.currentYear.grain // 100
            self.currentYear.grain -= self.currentYear.rats
        else:
            self.currentYear.rats = 0

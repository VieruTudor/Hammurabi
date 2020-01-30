from service import *


def numericalTypeCheck(inputNumber):
    try:
        inputNumber = int(inputNumber)
    except ValueError:
        raise ValueError("Please insert numerical values only")


class UI:
    def __init__(self, service):
        self.service = service

    # function that takes the acres number from user, checks it for valid input then sends it to service
    def UIBuyAcres(self, acresToBuy):
        try:
            numericalTypeCheck(acresToBuy)
            self.service.serviceBuyAcres(int(acresToBuy))
        except ValueError as ex:
            print(str(ex))
            self.UIReadAcresToBuy()
        except Error as er:
            print(str(er))
            self.UIReadAcresToBuy()

    # function that takes the number of units to be fed, checks for valid input and sends it to service
    def UIFeedPopulation(self, unitsToFeed):
        try:
            numericalTypeCheck(unitsToFeed)
            self.service.serviceFeedPopulation(int(unitsToFeed))
        except Exception as ex:
            print(str(ex))
            self.UIReadUnitsToFeed()

    # function that takes the number of units to be fed, checks for valid input and sends it to service
    def UIPlantAcres(self, acresToPlant):
        try:
            numericalTypeCheck(acresToPlant)
            self.service.servicePlantAcres(int(acresToPlant))
        except Exception as ex:
            print(str(ex))
            self.UIReadAcresToPlant()

    # function that takes the raw input from user and sends it to another function in the UI for processing
    def UIReadAcresToBuy(self):
        acresToBuy = input("Acres to buy/sell(+/-)->")
        self.UIBuyAcres(acresToBuy)

    # function that takes the raw input from user and sends it to another function in the UI for processing
    def UIReadUnitsToFeed(self):
        unitsToFeed = input("Units to feed the population->")
        self.UIFeedPopulation(unitsToFeed)

    # function that takes the raw input from user and sends it to another function in the UI for processing
    def UIReadAcresToPlant(self):
        acresToPlant = input("Acres to plant->")
        self.UIPlantAcres(acresToPlant)

    # starting the game
    def startGame(self):
        for i in range(4):
            self.UIReadAcresToBuy()
            self.UIReadUnitsToFeed()
            self.UIReadAcresToPlant()
            print("\n")
            self.service.newYear()
            print(str(self.service.currentYear))
            if self.service.gameLost:
                print("You failed your people")
                return
        if self.service.currentYear.acres >= 1000 and self.service.currentYear.population >= 100:
            print("GG")
        else:
            print("You Fail")

class Year:
    def __init__(self):
        self.year = 1
        self.newPeople = 0
        self.rip = 0
        self.population = 100
        self.acres = 1000
        self.harvest = 3
        self.rats = 200
        self.landPrice = 20
        self.grain = 2800
        self.plantedAcres = 0

    def __str__(self):
        printString = "In year " + str(self.year) + ", " + str(self.rip) + " people starved.\n"
        printString += str(self.newPeople) + " people came to the city.\n"
        printString += "City population is " + str(self.population) + "\n"
        printString += "City owns " + str(self.acres) + " acres of land.\n"
        printString += "Harvest was " + str(self.harvest) + " units per acre.\n"
        printString += "Rats ate " + str(self.rats) + " units.\n"
        printString += "Land price is " + str(self.landPrice) + " units per acre.\n\n"
        printString += "Grain stocks are " + str(self.grain) + " units."
        return printString


year = Year()
print(year)

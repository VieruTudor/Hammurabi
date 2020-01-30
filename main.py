from UI import *
from service import *
from domain import Year

startingYear = Year()
gameService = Service(startingYear)
gameUI = UI(gameService)
gameUI.startGame()

#Challenge 1
class Car:
    pass
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def printDetails(self):
        print("Model: ", self.model)
        print("Color: ", self.color)
class SedanEngine:
    pass
    def start(self):
        print("Car has started.")
    def stop(self):
        print("Car has stopped.")

class Sedan(Car):
    pass
    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()
    def setStart(self):
        self.engine.start()
    def setStop(self):
        self.engine.stop()

#Challende 2
car1 = Sedan("Toyota","Grey")
car1.setStart()
car1.printDetails()
car1.setStop()


class Player:
    pass
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName
# Team class contains a list of Player
# Objects
class Team:
    pass
    def __init__(self, name):
        self.name = name
        self.players = []
    def addPlayer(self, player):
        self.players.append(player)
    def getNumberOfPlayers(self):
        return len(self.players)

# School class contains a list of Team
# objects.
class School:
    pass
    def __init__(self, name):
        self.name = name
        self.teams = []
    def addTeam(self, team):
        self.teams.append(team)
    def getTotalPlayersInSchool(self):
        totalPlayers = 0
        for team in self.teams:
            totalPlayers = totalPlayers + team.getNumberOfPlayers()
        return totalPlayers

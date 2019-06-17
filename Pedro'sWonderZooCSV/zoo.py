class WonderZoo:

  def __init__(self, name, allExibs):
    self.name = name
    self.isActive = True
    self.allExibs = allExibs
    self.currentExib =  allExibs['one']


  def leave(self):
    self.isActive = False

  def goToExib(self, stallID):
    self.currentExib = self.allExibs[stallID]

class Exhibit:

  def __init__(self, stallID, name, neighbors, animalHere, hasExit):
    self.stallID = stallID
    self.name = name
    self.neighbors = neighbors
    self.hasExit = hasExit
    self.animalHere = animalHere

class Animal:

  def __init__(self, kind, sound, info):
    self.kind = kind
    self.sound = sound
    self.info = info
  def whatKindOfAnimal(self):
    return "This is a " + self.kind

  def animalSound(self):
    return "The sound a " + self.kind + " makes is " + str(self.sound)

  def animalInfo(self):
    return "The information on the " + self.kind + " is " + str(self.info)

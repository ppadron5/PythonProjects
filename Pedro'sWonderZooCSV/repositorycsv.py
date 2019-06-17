import zoo

def getWonderZoo():
  return zoo.WonderZoo('Pedros Wonder Zoo', getAllShops(None))

def getAllShops(forShopID):
  dictOfShops = {}
  file = open('location.csv', 'r')
  for line in file:
    fields = line.rstrip().split(',')
    if len(fields) == 4:
      shopID = fields[0]
      shopName = fields[1]
      shopFood = getFood(fields[2])
      shopExit = eval(fields[3])
      shopNeighbors = getNeighbors(shopID)
      if (forShopID == None or shopID == forShopID):
        dictOfShops[shopID] = zoo.Exhibit(shopID, shopName, shopNeighbors, shopFood, shopExit)
  file.close()
  return dictOfShops

def getNeighbors(forShopID):
  neighbors = {}
  file = open('neighbors.csv', 'r')
  for line in file:
    fields = line.rstrip().split(',')
    if len(fields) == 3:
      forShop = fields[0]
      direction = fields[1]
      toShop = fields[2]
      if forShop == forShopID:
        neighbors[direction] = toShop
  file.close()
  return neighbors

def getFood(foodID):
  foundFood = None
  file = open('animal.csv', 'r')
  for line in file:
    fields = line.rstrip().split(',')
    if len(fields) == 4:
      if foodID == fields[0]:
        animalKind = fields[1]
        animalSound = fields[2]
        animalInfo = fields[3]
        foundFood = zoo.Animal(animalKind, animalSound, animalInfo)
  file.close()
  return foundFood

def getAllFoods():
  foundFoods = []
  file = open('food.csv', 'r')
  for line in file:
    fields = line.rstrip().split(',')
    if len(fields) == 3:
      foodKind = fields[1]
      foodPrice = fields[2]
      foundFoods.append(zoo.Animal(fields[0], foodKind, foodPrice))
  file.close()
  return foundFoods
